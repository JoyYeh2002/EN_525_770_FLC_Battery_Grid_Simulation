import numpy as np
import matplotlib.pyplot as plt
from util.fuzzy_lookup_tables import fuzzy_lookup_v2g, fuzzy_lookup_csc
import util.fuzzy_membership_functions as fmf
from util.fuzzy_algorithms import fuzzify, calculate_output_components_and_power

# Example usage
flc_voltage = fmf.FLC_voltage()
flc_SOC = fmf.FLC_SOC()
flc_energy_csc = fmf.FLC_energy_csc()
flc_energy_v2g = fmf.FLC_energy_v2g()

# flc_voltage.plot_membership_functions()
# flc_SOC.plot_membership_functions()
# flc_energy_csc.plot_membership_functions()
# flc_energy_v2g.plot_membership_functions()

# Start with voltage and SOC
actual_voltage = 0.93  # Voltage in p.u.
actual_soc = 0.24

voltage_memberships = fuzzify(flc_voltage.membership_functions, actual_voltage)
soc_memberships = fuzzify(flc_SOC.membership_functions, actual_soc)

print("Fuzzified Voltage Memberships:")
for key, value in voltage_memberships.items():
    print(f"  {key}: {value:.2f}")

print("\nFuzzified SOC Memberships:")
for key, value in soc_memberships.items():
    print(f"  {key}: {value:.2f}")

energy_csc, energy_desired = calculate_output_components_and_power(voltage_memberships, soc_memberships, fuzzy_lookup_csc(), flc_energy_csc)
print(f"\nenergy desired (SOC): {energy_desired}")

actual_energy = energy_desired  # Energy level -> found with fuzzy controller with voltage and SOC
energy_memberships = fuzzify(flc_energy_csc.membership_functions, actual_energy)

print("\nFuzzified Energy Memberships:")
for key, value in energy_memberships.items():
    print(f"  {key}: {value:.2f}")

output_components, power_output = calculate_output_components_and_power(voltage_memberships, energy_memberships, fuzzy_lookup_v2g(), flc_energy_v2g)
print(f"Defuzzified Output (COG): {power_output}")

