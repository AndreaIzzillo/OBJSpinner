import settings

import os
import sys
import math
import pygame

from screen import clear, line, screen_vertices
from mesh import load_obj

def frame(s, vs, fs, angle, dx, dy, dz):
    clear(s)
    screen_vertices_list = screen_vertices(vs, angle, dx, dy, dz)
    for a, b in fs:
        line(s, screen_vertices_list[a], screen_vertices_list[b])

def main():
    filename = "./assets/objects/sample_car.obj"

    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            if sys.argv[i] in ("-f", "--file") and i + 1 < len(sys.argv):
                filename = sys.argv[i + 1]
                i += 1
            if sys.argv[i] in ("-F", "--fps") and i + 1 < len(sys.argv):
                settings.fps = int(sys.argv[i + 1])
                i += 1
            if sys.argv[i] in ("-h", "--help"):
                print("Usage: python main.py [-f filename] [-F fps]")
                sys.exit(0)

    if not os.path.exists(filename):
        print(f"Error: File {filename} not found.")
        sys.exit(1)

    vs, fs = load_obj(filename)

    pygame.init()

    s = pygame.display.set_mode((settings.width, settings.height))
    pygame.display.set_caption(f"OBJSpinner - {os.path.basename(filename)}")
    clock = pygame.time.Clock()

    dx = 0.0
    dy = -1.0
    dz = 5.0
    angle = 0.0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: running = False
                if event.key == pygame.K_UP:     dz -= 0.5 if dz > 1.0 else 0.0
                if event.key == pygame.K_DOWN:   dz += 0.5
                if event.key == pygame.K_LEFT:   dx += 0.5
                if event.key == pygame.K_RIGHT:  dx -= 0.5
                if event.key == pygame.K_SPACE:  dy -= 0.5
                if event.key == pygame.K_LSHIFT: dy += 0.5
                if event.key == pygame.K_r:      dx, dy, dz = 0.0, -1.0, 5.0
                if event.key == pygame.K_c:
                    settings.color_idx = (settings.color_idx + 1) % len(settings.color_list)
                    settings.foreground = settings.color_list[settings.color_idx]
            if event.type == pygame.DROPFILE:
                try:
                    vs, fs = load_obj(event.file)
                    pygame.display.set_caption(f"OBJSpinner - {os.path.basename(event.file)}")
                except Exception as e:
                    print(f"Error loading {event.file}: {e}")

        dt = clock.get_time() / 1000.0
        angle += math.pi * dt / 2.0

        frame(s, vs, fs, angle, dx, dy, dz)

        pygame.display.flip()
        clock.tick(settings.fps)

    pygame.quit()

if __name__ == "__main__":
    main()
