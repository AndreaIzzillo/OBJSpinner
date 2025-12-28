class Point2D:
    """
    A class representing a 2D point in Cartesian coordinates.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
    """
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

class Point3D:
    """
    A class representing a 3D point in Cartesian coordinate space.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
        z (float): The z-coordinate of the point.
    """
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z