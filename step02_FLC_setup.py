import numpy as np
import matplotlib.pyplot as plt
from util.fuzzy_lookup_tables import fuzzy_lookup_v2g
import util.fuzzy_membership_functions as fmf
import util.defuzzification as defuzz

# Example usage
flc_voltage = fmf.FLC_voltage()
flc_SOC = fmf.FLC_SOC()
flc_energy_csc = fmf.FLC_energy_csc()
flc_energy_v2g = fmf.FLC_energy_v2g()

# flc_voltage.plot_membership_functions()
# flc_SOC.plot_membership_functions()
# flc_energy_csc.plot_membership_functions()
# flc_energy_v2g.plot_membership_functions()

# Fuzzification and inference process
def fuzzify(membership_functions, input_value):
    memberships = {}
    for mf in membership_functions:
        membership_result = mf.compute_membership(np.array([input_value]))[0]
        if membership_result > 0:
            memberships[mf.name] = membership_result
    return memberships

actual_voltage = 0.93  # Voltage in p.u.
actual_energy = 0.227  # Energy level

voltage_memberships = fuzzify(flc_voltage.membership_functions, actual_voltage)
energy_memberships = fuzzify(flc_energy_csc.membership_functions, actual_energy)

print("Fuzzified Voltage Memberships:")
for key, value in voltage_memberships.items():
    print(f"  {key}: {value:.2f}")

print("\nFuzzified Energy Memberships:")
for key, value in energy_memberships.items():
    print(f"  {key}: {value:.2f}")

# Test the lookup function
output_components = {}
for voltage_input in voltage_memberships.keys():
    for energy_input in energy_memberships.keys():
        output = fuzzy_lookup_v2g().get_output(voltage_input, energy_input)
        output_weights = round(min(voltage_memberships[voltage_input], energy_memberships[energy_input]), 2)
        output_components[(voltage_input, energy_input)] = {"output": output, "output_weights": output_weights}

print(f"\nOutput Components:{output_components}")

# CoG defuzzification
triangles = []
weights = []
for idx, (voltage_input, energy_input) in enumerate(output_components.keys()):
    output = output_components[(voltage_input, energy_input)]
    output_mf = flc_energy_v2g.get_membership_function(output["output"])

    # Extract the triangle parameters
    triangle = [round(point[0], 2) for point in output_mf.points] 
    triangles.append(tuple(triangle))

    # Get the output wreights
    output_components[(voltage_input, energy_input)]["output_mf"] = output_mf
    output_weight = round(min(voltage_memberships[voltage_input], energy_memberships[energy_input]), 2)
    weights.append(output_weight)

    print(f"\nOutput Component {idx + 1}:")
    print(triangle)
    print(f"Voltage Input: {voltage_input}, Energy Input: {energy_input}, Output Weights: {output_weight} ")

# Calculate the defuzzified output
cog_value = round(defuzz.center_of_gravity(triangles, weights), 2)
print(f"Defuzzified Output (COG): {cog_value}")
