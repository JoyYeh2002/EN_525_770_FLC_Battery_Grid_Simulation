
def center_of_gravity(triangles, weights):
    """
    Compute the defuzzified output using the Center of Gravity (COG) method.

    Args:
        triangles (list): A list of tuples, each containing the parameters (a, b, c) of a triangular membership function.
                          (a, b, c) define the start, peak, and end of the triangle, respectively.
        weights (list): A list of weights (membership values) corresponding to the degree of activation for each triangle.

    Returns:
        float: The defuzzified output value.
    """
    if len(triangles) != len(weights):
        raise ValueError("The number of triangles must match the number of weights.")
    
    numerator = 0
    denominator = 0
    
    for triangle, weight in zip(triangles, weights):
        a, b, c = triangle
        # Compute the centroid of the triangle
        centroid = (a + b + c) / 3
        # Add to numerator and denominator
        numerator += centroid * weight
        denominator += weight
    
    # Avoid division by zero
    if denominator == 0:
        raise ValueError("The sum of weights is zero. Cannot compute defuzzified value.")
    
    return numerator / denominator