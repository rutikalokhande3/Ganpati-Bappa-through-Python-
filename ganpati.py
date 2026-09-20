import pygame
import cv2
import math
import sys

# -----------------------------
# SETTINGS
# -----------------------------
WIDTH = 700
HEIGHT = 700

BG = (0, 0, 0)
ORANGE = (255, 145, 20)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ganpati Bappa - Python")

clock = pygame.time.Clock()

# -----------------------------
# LOAD GANPATI IMAGE
# -----------------------------
image = cv2.imread("ganpati_outline.png")

if image is None:
    print("ganpati_outline.png file nahi mili!")
    sys.exit()

# Resize image
image = cv2.resize(image, (WIDTH, HEIGHT))

# -----------------------------
# CREATE DRAWING PATHS
# -----------------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Lines ko detect karo
_, threshold = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(
    threshold,
    cv2.RETR_LIST,
    cv2.CHAIN_APPROX_NONE
)

paths = []

for contour in contours:

    if len(contour) < 10:
        continue

    path = []

    for point in contour:
        x, y = point[0]

        # Center/resize adjustment
        x = int(x)
        y = int(y)

        path.append((x, y))

    paths.append(path)


# -----------------------------
# CALCULATE PATH LENGTH
# -----------------------------
def path_length(path):

    total = 0

    for i in range(1, len(path)):

        x1, y1 = path[i - 1]
        x2, y2 = path[i]

        distance = math.sqrt(
            (x2 - x1) ** 2 +
            (y2 - y1) ** 2
        )

        total += distance

    return total


# -----------------------------
# DRAW ANIMATED GANPATI
# -----------------------------
print("Ganpati Bappa drawing started...")

for path in paths:

    if len(path) < 2:
        continue

    for i in range(1, len(path)):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        p1 = path[i - 1]
        p2 = path[i]

        pygame.draw.line(
            screen,
            ORANGE,
            p1,
            p2,
            2
        )

        pygame.display.flip()

        clock.tick(300)


# -----------------------------
# KEEP WINDOW OPEN
# -----------------------------
print("Ganpati Bappa drawing complete!")

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)