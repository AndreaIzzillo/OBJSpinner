import settings

import pygame
import math

from point import Point2D, Point3D

def clear(s: pygame.Surface) -> None:
    """
    Clears the screen by filling it with the background color.

    Args:
        s (pygame.Surface): The surface to clear.
    """
    s.fill(settings.background)

def point(s: pygame.Surface, p: Point2D) -> None:
    """
    Draws a point on the screen.

    Args:
        s (pygame.Surface): The surface to draw on.
        p (Point2D): The position of the point.
    """
    size = 10
    pygame.draw.rect(s, settings.foreground, (int(p.x - size / 2), int(p.y - size / 2), size, size))

def line(s: pygame.Surface, p1: Point2D, p2: Point2D) -> None:
    """
    Draws a line between two points on the screen.

    Args:
        s (pygame.Surface): The surface to draw on.
        p1 (Point2D): The starting point of the line.
        p2 (Point2D): The ending point of the line.
    """
    pygame.draw.line(s, settings.foreground, (int(p1.x), int(p1.y)), (int(p2.x), int(p2.y)), 1)

def screen_vertices(vs, angle, dx, dy, dz):
    """
    Transform 3D vertices to 2D screen coordinates with rotation and translation.
    
    Applies a rotation around the Y axis, translates the vertices in 3D space,
    performs perspective projection, and converts the result to screen coordinates.
    
    Args:
        vs (list): List of 3D points (with x, y, z attributes) to transform.
        angle (float): Rotation angle in radians around the Y axis.
        dx (float): Translation distance along the X axis.
        dy (float): Translation distance along the Y axis.
        dz (float): Translation distance along the Z axis.
    
    Returns:
        list: List of Point2D objects representing the transformed vertices in screen coordinates.
    
    Note:
        - Handles division by zero by clamping z values close to zero.
        - Uses perspective projection (dividing by z) to create depth effect.
        - Converts normalized device coordinates (NDC) to screen pixel coordinates.
    """
    c = math.cos(angle)
    s = math.sin(angle)

    screen_points = []
    for p in vs:
        # Rotate around Y axis and translate
        x = p.x * c - p.z * s + dx
        y = p.y + dy
        z = p.x * s + p.z * c + dz

        z = max(z, 0.01)

        # Normalize to NDC
        x_ndc = x / z if z > 0 else -x / z
        y_ndc = y / z if z > 0 else -y / z

        # Convert to screen coordinates
        x_screen = (x_ndc + 1) / 2 * settings.width
        y_screen = (1 - (y_ndc + 1) / 2) * settings.height

        screen_points.append(Point2D(x_screen, y_screen))
    return screen_points