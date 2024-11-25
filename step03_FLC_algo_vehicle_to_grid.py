import numpy as np
import matplotlib.pyplot as plt
from util.fuzzy_lookup_tables import fuzzy_lookup_v2g, fuzzy_lookup_csc
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
actual_soc = 0.24
actual_energy = 0.227  # Energy level -> found with fuzzy controller with voltage and SOC

voltage_memberships = fuzzify(flc_voltage.membership_functions, actual_voltage)
soc_memberships = fuzzify(flc_SOC.membership_functions, actual_soc)

energy_memberships = fuzzify(flc_energy_csc.membership_functions, actual_energy)

print("Fuzzified Voltage Memberships:")
for key, value in voltage_memberships.items():
    print(f"  {key}: {value:.2f}")

print("\nFuzzified SOC Memberships:")
for key, value in soc_memberships.items():
    print(f"  {key}: {value:.2f}")

print("\nFuzzified Energy Memberships:")
for key, value in energy_memberships.items():
    print(f"  {key}: {value:.2f}")

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

        # Extract the triangle parameters
        triangle = [round(point[0], 2) for point in output_mf.points] 
        triangles.append(tuple(triangle))

        # Get the output weights
        output_components[(voltage_input, energy_input)]["output_mf"] = output_mf
        output_weight = round(min(input01[voltage_input], input02[energy_input]), 2)
        weights.append(output_weight)

    # Calculate the defuzzified output
    power_output = round(defuzz.center_of_gravity(triangles, weights), 2)
    return output_components, power_output


energy_csc, energy_desired = calculate_output_components_and_power(voltage_memberships, soc_memberships, fuzzy_lookup_csc(), flc_energy_csc)
print(f"\nenergy desired (SOC): {energy_desired}")

output_components, power_output = calculate_output_components_and_power(voltage_memberships, energy_memberships, fuzzy_lookup_v2g(), flc_energy_v2g)
print(f"Defuzzified Output (COG): {power_output}")


