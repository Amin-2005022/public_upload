"""Basic Bresenham from the lecture: only for 0 <= m <= 1 and x1 < x2."""


def bresenham_line(x1, y1, x2, y2):
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


if __name__ == "__main__":
    print(bresenham_line(1, 1, 8, 5))
