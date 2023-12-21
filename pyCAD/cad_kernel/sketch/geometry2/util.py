import numpy as np


def translate2D(item, dx, dy):
    """
    Translate a 2D point or array of points by (dx, dy).

    Args:
        item: A NumPy array-like object representing the point(s) to be translated.
        dx: The translation amount in the x-axis.
        dy: The translation amount in the y-axis.

    Returns:
        A new NumPy array with the translated point(s).
    """
    return item + np.array([dx, dy])

def rotate2D(item, angle, centerpoint):
    """
    Rotate a 2D point or array of points around a specified center point.

    Args:
        item: A NumPy array-like object representing the point(s) to be rotated.
        angle: The rotation angle in degrees (positive for counterclockwise).
        centerpoint: A NumPy array representing the center point of rotation.

    Returns:
        A new NumPy array with the rotated point(s).
    """
    # Convert the angle to radians
    angle_rad = np.deg2rad(angle)

    # Calculate the coordinates relative to the center point
    relative_coords = item - centerpoint

    # Perform the 2D rotation using a rotation matrix
    rotation_matrix = np.array([[np.cos(angle_rad), -np.sin(angle_rad)],
                                 [np.sin(angle_rad), np.cos(angle_rad)]])
    rotated_coords = np.dot(rotation_matrix, relative_coords)

    # Translate the coordinates back to their original position
    final_coords = rotated_coords + centerpoint

    return final_coords