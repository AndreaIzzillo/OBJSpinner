import trimesh

from point import Point3D

def load_obj(obj_path: str):
    """
    Load a 3D mesh from an OBJ file.
    
    Args:
        obj_path (str): The file path to the OBJ file to load.
    
    Returns:
        tuple: A tuple containing:
            - vs (list[Point3D]): List of vertices as Point3D objects with (x, y, z) coordinates.
            - fs (list[tuple]): List of faces as tuples representing the unique edges of the mesh.
    
    Raises:
        FileNotFoundError: If the specified OBJ file does not exist.
        ValueError: If the file is not a valid mesh format.
    """
    mesh = trimesh.load(obj_path, force="mesh", process=False)

    vs = [Point3D(x, y, z) for (x, y, z) in mesh.vertices]
    fs = [tuple(e) for e in mesh.edges_unique]

    return vs, fs