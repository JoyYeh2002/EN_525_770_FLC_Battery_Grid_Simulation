# Fuzzification and inference process
import numpy as np


def fuzzify(membership_functions, input_value):
    memberships = {}
    for mf in membership_functions:
        membership_result = mf.compute_membership(np.array([input_value]))[0]
        if membership_result > 0:
            memberships[mf.name] = membership_result
    return memberships


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


def calculate_output_components_and_power(input01, input02, flc_lookup_table, flc_target_object):
    output_components = {}
    for voltage_input in input01.keys():
        for energy_input in input02.keys():
            output = flc_lookup_table.get_output(voltage_input, energy_input)
            output_weights = round(min(input01[voltage_input], input02[energy_input]), 2)
            output_components[(voltage_input, energy_input)] = {"output": output, "output_weights": output_weights}

    # print(f"\nOutput Components:{output_components}")

    triangles = []
    weights = []
    for _, (voltage_input, energy_input) in enumerate(output_components.keys()):
        output = output_components[(voltage_input, energy_input)]
        output_mf = flc_target_object.get_membership_function(output["output"])

    
        if output_mf is None:
            print(f"Warning: No membership function found for output: {output['output']}")
            continue  # Skip this iteration if output_mf is None

        # Extract the triangle parameters
        triangle = [round(point[0], 2) for point in output_mf.points] 
        triangles.append(tuple(triangle))

        # Get the output weights
        output_components[(voltage_input, energy_input)]["output_mf"] = output_mf
        output_weight = round(min(input01[voltage_input], input02[energy_input]), 2)
        weights.append(output_weight)

    # Calculate the defuzzified output
    power_output = round(center_of_gravity(triangles, weights), 2)
    return output_components, power_output

