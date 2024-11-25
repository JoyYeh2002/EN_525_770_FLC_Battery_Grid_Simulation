import numpy as np
import os
import matplotlib.pyplot as plt
from util.fuzzy_lookup_tables import fuzzy_lookup_v2g, fuzzy_lookup_csc
import util.fuzzy_membership_functions as fmf
from util.fuzzy_algorithms import fuzzify, calculate_output_components_and_power

# Example usage
flc_voltage = fmf.FLC_voltage()
flc_SOC = fmf.FLC_SOC()
flc_energy_csc = fmf.FLC_energy_csc()
flc_energy_v2g = fmf.FLC_energy_v2g()

if __name__ == "__main__":
    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    # Grid charging EV (power output positive)
    actual_soc_values = [0.1, 0.15, 0.2, 0.3, 0.35, 0.4, 0.48, 0.5]
    voltage_sweep = np.linspace(0, 1, 500)  # Sweep from 0 to 1 p.u.

    plt.title(f'Grid Charging - Voltage vs. PWR Outputs for various SOC')
    plt.xlabel('Voltage (p.u.)')
    plt.ylabel('Power Output from the Grid (p.u.)')
    plt.xlim(0.7, 1.01)
    plt.ylim(-1, 1)  # Set y-axis range to [-1, 1]
    plt.grid(True)
   
    for actual_soc in actual_soc_values:
        power_outputs = []

        for actual_voltage in voltage_sweep:
            voltage_memberships = fuzzify(flc_voltage.membership_functions, actual_voltage)
            soc_memberships = fuzzify(flc_SOC.membership_functions, actual_soc)
            energy_csc, energy_desired = calculate_output_components_and_power(voltage_memberships, soc_memberships, fuzzy_lookup_csc(), flc_energy_csc)
        
            actual_energy = energy_desired  # Energy level -> found with fuzzy controller with voltage and SOC
            energy_memberships = fuzzify(flc_energy_csc.membership_functions, actual_energy)
            output_components, power_output = calculate_output_components_and_power(voltage_memberships, energy_memberships, fuzzy_lookup_v2g(), flc_energy_v2g)
            
            power_outputs.append(power_output)

        # Visualization
        plt.plot(voltage_sweep, power_outputs, label=f'SOC={actual_soc}')
        
    plt.legend()  # Add legend for SOC values
    plt.savefig(f"outputs/charging_voltage_sweep.png")
    print("SUCCESS: Charging simulation completed and saved as charging_voltage_sweep.png")



    plt.figure()  # Create a new figure for the next plot
    # Grid discharging EV (power output negative)
    actual_soc_values = [0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95]
    voltage_sweep = np.linspace(0, 1, 500)  # Sweep from 0 to 1 p.u.

    plt.title(f'Grid Discharging - Voltage vs. PWR Outputs for various SOC')
    plt.xlabel('Voltage (p.u.)')
    plt.ylabel('Power Output from the Grid (p.u.)')
    plt.xlim(0.7, 1.01)
    plt.ylim(-1, 1)  # Set y-axis range to [-1, 1]
    plt.grid(True)
   
    for actual_soc in actual_soc_values:
        power_outputs = []

        for actual_voltage in voltage_sweep:
            voltage_memberships = fuzzify(flc_voltage.membership_functions, actual_voltage)
            soc_memberships = fuzzify(flc_SOC.membership_functions, actual_soc)
            energy_csc, energy_desired = calculate_output_components_and_power(voltage_memberships, soc_memberships, fuzzy_lookup_csc(), flc_energy_csc)
        
            actual_energy = energy_desired  # Energy level -> found with fuzzy controller with voltage and SOC
            energy_memberships = fuzzify(flc_energy_csc.membership_functions, actual_energy)
            output_components, power_output = calculate_output_components_and_power(voltage_memberships, energy_memberships, fuzzy_lookup_v2g(), flc_energy_v2g)
            
            power_outputs.append(power_output)

        # Visualization
        plt.plot(voltage_sweep, power_outputs, label=f'SOC={actual_soc}')
        
    plt.legend()  # Add legend for SOC values
    plt.savefig(f"outputs/discharging_voltage_sweep.png")
    print("SUCCESS: Disharging simulation completed and saved as charging_voltage_sweep.png")
