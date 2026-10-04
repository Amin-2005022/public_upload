"""Lab 2 - DDA and Bresenham line algorithms (pure Python, no OpenGL).

Each function returns the list of pixels (x, y) the algorithm turns on,
so students can print and check them against their hand-worked tables.
"""
import math


def round_half_up(v):
    """Round the way we do in class: 0.5 always rounds up (2.5 -> 3)."""
    return math.floor(v + 0.5)


def direct_line_simple(x1, y1, x2, y2):
    """Direct method WITHOUT checking m: always step x, y = m*x + b."""
    if x1 == x2:                        # vertical line: m is undefined
        return [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    step = 1 if x2 >= x1 else -1
    return [(x, round_half_up(m * x + b)) for x in range(x1, x2 + step, step)]


def direct_line(x1, y1, x2, y2):
    """Direct method WITH checking m: step along x if |m| <= 1, else along y."""
    dx, dy = x2 - x1, y2 - y1
    if abs(dx) >= abs(dy):              # |m| <= 1: y = m*x + b
        return direct_line_simple(x1, y1, x2, y2)
    m = dy / dx if dx != 0 else None    # |m| > 1: x = (y - b) / m
    step = 1 if y2 >= y1 else -1
    pixels = []
    for y in range(y1, y2 + step, step):
        x = x1 if m is None else x1 + (y - y1) / m
        pixels.append((round_half_up(x), y))
    return pixels


def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    if steps == 0:                      # both end points are the same
        return [(x1, y1)]
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x1, y1
    pixels = []
    for _ in range(steps + 1):
        pixels.append((round_half_up(x), round_half_up(y)))
        x += x_inc
        y += y_inc
    return pixels


def bresenham_line(x1, y1, x2, y2):
    """Basic Bresenham from the lecture: only for 0 <= m <= 1 and x1 < x2."""
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx                     # d1
    inc1 = 2 * dy                       # added when we choose S
    inc2 = 2 * (dy - dx)                # added when we choose T
    x, y = x1, y1
    pixels = [(x, y)]
    while x < x2:
        if d < 0:                       # S: y stays
            d += inc1
        else:                           # T: y goes up by 1
            d += inc2
            y += 1
        x += 1
        pixels.append((x, y))
    return pixels


def bresenham_any(x1, y1, x2, y2):
    """Bresenham for every slope and direction (swap roles of x and y when steep)."""
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1
    x, y = x1, y1
    pixels = [(x, y)]
    if dx >= dy:                        # gentle: step x, decide y
        d = 2 * dy - dx
        for _ in range(dx):
            if d < 0:
                d += 2 * dy
            else:
                d += 2 * (dy - dx)
                y += sy
            x += sx
            pixels.append((x, y))
    else:                               # steep: step y, decide x
        d = 2 * dx - dy
        for _ in range(dy):
            if d < 0:
                d += 2 * dx
            else:
                d += 2 * (dx - dy)
                x += sx
            y += sy
            pixels.append((x, y))
    return pixels


if __name__ == "__main__":
    print("Direct, no m check (10,10)-(18,45):", direct_line_simple(10, 10, 18, 45))
    print("Direct, m checked  (10,10)-(18,45):", direct_line(10, 10, 18, 45))
    print("DDA (6,9)-(11,12):      ", dda_line(6, 9, 11, 12))
    print("Bresenham (1,1)-(8,5):  ", bresenham_line(1, 1, 8, 5))
    print("Bresenham (20,10)-(30,18):", bresenham_line(20, 10, 30, 18))
    print("Any slope (2,1)-(5,8):  ", bresenham_any(2, 1, 5, 8))
