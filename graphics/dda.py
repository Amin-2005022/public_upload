"""DDA line algorithm."""
import math


def round_half_up(v):
    return math.floor(v + 0.5)


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


if __name__ == "__main__":
    print(dda_line(6, 9, 11, 12))
