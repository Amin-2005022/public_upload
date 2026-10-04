"""Lab 2 - Draw a line with DDA and with Bresenham, pixel by pixel.

The window shows a 50 x 50 grid of BIG pixels (each 10 x 10 screen pixels),
so students can see exactly which pixels each algorithm chooses.

Keys:
  1  show DDA (blue)
  2  show Bresenham (green)
  3  show DDA and Bresenham together
  4  direct method WITHOUT checking m (always steps x: steep lines get gaps)
  5  direct method WITH checking m (steps y when |m| > 1: no gaps)
  q  quit
"""
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from algorithms import dda_line, bresenham_any, direct_line_simple, direct_line

GRID = 50          # logical pixels across and down
CELL = 10          # screen pixels per logical pixel
mode = 3           # 1 = DDA, 2 = Bresenham, 3 = both, 4/5 = direct method

# Lines to draw: (x1, y1, x2, y2). Try your own!
LINES = [
    (5, 5, 45, 25),    # gentle slope
    (10, 10, 18, 45),  # steep slope
    (40, 45, 15, 30),  # right to left, negative slope
    (45, 25, 5, 5),    # the FIRST line drawn backwards: look where DDA and Bresenham differ
]


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)     # white background
    glPointSize(CELL - 1)                # one logical pixel = one big square


def draw_grid():
    glColor3f(0.85, 0.85, 0.85)
    glLineWidth(1)
    glBegin(GL_LINES)
    for i in range(GRID + 1):
        glVertex2f(i - 0.5, -0.5); glVertex2f(i - 0.5, GRID - 0.5)
        glVertex2f(-0.5, i - 0.5); glVertex2f(GRID - 0.5, i - 0.5)
    glEnd()


def plot(pixels, r, g, b):
    glColor3f(r, g, b)
    glBegin(GL_POINTS)
    for x, y in pixels:
        glVertex2i(x, y)
    glEnd()


def true_line(x1, y1, x2, y2):
    glColor3f(0.85, 0.3, 0.1)            # orange: the mathematical line
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(x1, y1); glVertex2f(x2, y2)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_grid()
    for (x1, y1, x2, y2) in LINES:
        if mode in (1, 3):
            plot(dda_line(x1, y1, x2, y2), 0.12, 0.31, 0.60)       # blue
        if mode in (2, 3):
            plot(bresenham_any(x1, y1, x2, y2), 0.10, 0.60, 0.30)  # green
        if mode == 4:
            plot(direct_line_simple(x1, y1, x2, y2), 0.55, 0.20, 0.60)  # purple
        if mode == 5:
            plot(direct_line(x1, y1, x2, y2), 0.55, 0.20, 0.60)         # purple
        true_line(x1, y1, x2, y2)
    glFlush()


def keyboard(key, x, y):
    global mode
    if key in (b"1", b"2", b"3", b"4", b"5"):
        mode = int(key)
        glutPostRedisplay()
    elif key == b"q":
        sys.exit(0)


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-0.5, GRID - 0.5, -0.5, GRID - 0.5)   # 1 unit = 1 logical pixel
    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(GRID * CELL, GRID * CELL)
    glutCreateWindow(b"Lab 2: 1 DDA, 2 Bresenham, 3 both, 4 direct (no m), 5 direct (m)")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()


if __name__ == "__main__":
    main()
