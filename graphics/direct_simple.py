"""Direct method WITHOUT checking m: always step x, y = m*x + b."""
import math


def round_half_up(v):
    return math.floor(v + 0.5)


def direct_line_simple(x1, y1, x2, y2):
    if x1 == x2:                        # vertical line: m is undefined
        return [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    step = 1 if x2 >= x1 else -1
    return [(x, round_half_up(m * x + b)) for x in range(x1, x2 + step, step)]


if __name__ == "__main__":
    print(direct_line_simple(10, 10, 18, 45))
