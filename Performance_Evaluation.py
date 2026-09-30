import os
import time
import math
import psutil
import platform
import tempfile
from statistics import mean

def get_system_info():
    return {
        "OS": platform.system() + " " + platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Physical Cores": psutil.cpu_count(logical=False),
        "Logical Cores": psutil.cpu_count(logical=True),
        "Total RAM (GB)": round(psutil.virtual_memory().total / (1024**3), 2),
        "Disk Total (GB)": round(psutil.disk_usage('/').total / (1024**3), 2)
    }

def measure_idle_utilization(duration=5):
    cpu_samples = []
    mem_samples = []

    print(f"\n[1] Measuring idle CPU and RAM usage for {duration} seconds...")
    for _ in range(duration):
        cpu_samples.append(psutil.cpu_percent(interval=1))
        mem_samples.append(psutil.virtual_memory().percent)

    return {
        "Average CPU Utilization (%)": round(mean(cpu_samples), 2),
        "Average RAM Utilization (%)": round(mean(mem_samples), 2)
    }

def cpu_benchmark(limit=50000):
    print("\n[2] Running CPU benchmark...")
    start = time.perf_counter()
    count = 0

    # Prime counting test
    for num in range(2, limit):
        is_prime = True
        root = int(math.sqrt(num)) + 1
        for i in range(2, root):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1

    end = time.perf_counter()
    elapsed = end - start
    throughput = limit / elapsed

    return {
        "CPU Benchmark Time (s)": round(elapsed, 3),
        "Primes Found": count,
        "CPU Throughput (numbers/sec)": round(throughput, 2)
    }

def response_time_test():
    print("\n[3] Measuring response time...")
    start = time.perf_counter()

    # Simple quick operation
    total = sum(range(1000000))

    end = time.perf_counter()
    response_time = end - start

    return {
        "Response Time for Quick Task (s)": round(response_time, 6),
        "Dummy Result": total
    }

def disk_speed_test(file_size_mb=100):
    print(f"\n[4] Running disk write/read speed test with {file_size_mb} MB file...")
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, "perf_test_file.bin")
    data = os.urandom(1024 * 1024)  # 1 MB random block

    # Write test
    start_write = time.perf_counter()
    with open(file_path, "wb") as f:
        for _ in range(file_size_mb):
            f.write(data)
    end_write = time.perf_counter()

    write_time = end_write - start_write
    write_speed = file_size_mb / write_time

    # Read test
    start_read = time.perf_counter()
    with open(file_path, "rb") as f:
        while f.read(1024 * 1024):
            pass
    end_read = time.perf_counter()

    read_time = end_read - start_read
    read_speed = file_size_mb / read_time

    # Clean up
    os.remove(file_path)

    return {
        "Disk Write Time (s)": round(write_time, 3),
        "Disk Read Time (s)": round(read_time, 3),
        "Disk Write Speed (MB/s)": round(write_speed, 2),
        "Disk Read Speed (MB/s)": round(read_speed, 2)
    }

def current_disk_usage():
    usage = psutil.disk_usage('/')
    return {
        "Disk Used (%)": usage.percent,
        "Free Disk Space (GB)": round(usage.free / (1024**3), 2)
    }

def network_stats():
    net = psutil.net_io_counters()
    return {
        "Bytes Sent (MB)": round(net.bytes_sent / (1024**2), 2),
        "Bytes Received (MB)": round(net.bytes_recv / (1024**2), 2)
    }

def print_report(title, data):
    print("\n" + "="*50)
    print(title)
    print("="*50)
    for k, v in data.items():
        print(f"{k}: {v}")

def main():
    print("\nWINDOWS PERFORMANCE EVALUATION TOOL")
    print("=" * 50)

    sys_info = get_system_info() 
    idle_stats = measure_idle_utilization(duration=5)
    cpu_stats = cpu_benchmark(limit=50000)
    response_stats = response_time_test()
    disk_stats = disk_speed_test(file_size_mb=100)
    disk_usage = current_disk_usage()
    net_stats = network_stats()

    print_report("SYSTEM INFORMATION", sys_info)
    print_report("UTILIZATION METRICS", idle_stats)
    print_report("CPU BENCHMARK RESULTS", cpu_stats)
    print_report("RESPONSE TIME RESULTS", response_stats)
    print_report("DISK PERFORMANCE RESULTS", disk_stats)
    print_report("DISK USAGE", disk_usage)
    print_report("NETWORK STATISTICS", net_stats)

    print("\n" + "="*50)
    print("INTERPRETATION")
    print("="*50)
    print("1. Lower CPU Benchmark Time = better CPU performance")
    print("2. Higher CPU Throughput = system processes more work per second")
    print("3. Lower Response Time = faster system response")
    print("4. Higher Disk Read/Write Speed = better storage performance")
    print("5. Very high idle CPU/RAM usage may indicate background load")
    print("="*50)

if __name__ == "__main__":
    main()


# pip install psutil
# python performance_evaluation.py