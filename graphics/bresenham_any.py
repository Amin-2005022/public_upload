"""Bresenham for every slope and direction (swap roles of x and y when steep)."""


def bresenham_any(x1, y1, x2, y2):
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
    print(bresenham_any(2, 1, 5, 8))
