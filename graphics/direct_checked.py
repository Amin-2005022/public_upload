"""Direct method WITH checking m: step along x if |m| <= 1, else along y."""
from direct_simple import direct_line_simple, round_half_up


def direct_line(x1, y1, x2, y2):
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


if __name__ == "__main__":
    print(direct_line(10, 10, 18, 45))
