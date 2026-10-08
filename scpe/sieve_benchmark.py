"""
Lab 02 - System Performance Evaluation Using Benchmarking
Benchmark program: Sieve of Eratosthenes
Course: 0613-310 System Configuration and Performance Evaluation Lab

Measures CPU Time and Wall (Execution) Time over several runs and
prints the average, standard deviation and coefficient of variation.
"""
import math
import time
import platform
import statistics

N = 10_000_000  # find all primes up to N (increase if one run takes < 1 second)
RUNS = 5        # number of times to repeat the benchmark


def sieve(n):
    """Return the number of primes from 2 to n."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for m in range(i * i, n + 1, i):   # cross out multiples of i
                is_prime[m] = False

    return sum(is_prime)


def run_once(n):
    """Run the sieve once and return (prime_count, cpu_time, wall_time)."""
    wall_start = time.perf_counter()     # real clock time
    cpu_start = time.process_time()      # CPU time used by this process

    count = sieve(n)

    cpu_time = time.process_time() - cpu_start
    wall_time = time.perf_counter() - wall_start
    return count, cpu_time, wall_time


def main():
    print("=" * 60)
    print("SIEVE OF ERATOSTHENES BENCHMARK")
    print("=" * 60)
    print(f"System    : {platform.system()} {platform.release()}")
    print(f"Processor : {platform.processor() or platform.machine()}")
    print(f"Python    : {platform.python_version()}")
    print(f"N = {N:,}   Runs = {RUNS}")
    print("-" * 60)
    print(f"{'Run':<6}{'Primes':>12}{'CPU Time (s)':>18}{'Wall Time (s)':>18}")
    print("-" * 60)

    cpu_times = []
    wall_times = []
    for run in range(1, RUNS + 1):
        count, cpu_t, wall_t = run_once(N)
        cpu_times.append(cpu_t)
        wall_times.append(wall_t)
        print(f"{run:<6}{count:>12,}{cpu_t:>18.4f}{wall_t:>18.4f}")

    print("-" * 60)
    for name, values in (("CPU Time", cpu_times), ("Wall Time", wall_times)):
        avg = statistics.mean(values)
        sd = statistics.stdev(values)
        cv = sd / avg * 100
        print(f"{name:<10} Average = {avg:.4f} s   SD = {sd:.4f} s   CV = {cv:.2f} %")

    waiting = statistics.mean(wall_times) - statistics.mean(cpu_times)
    print(f"Average waiting time (Wall - CPU) = {waiting:.4f} s")
    print("=" * 60)


if __name__ == "__main__":
    main()
