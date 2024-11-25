import numpy as np
import os
import matplotlib.pyplot as plt
from util.fuzzy_lookup_tables import fuzzy_lookup_v2g, fuzzy_lookup_csc
import util.fuzzy_membership_functions as fmf
from util.fuzzy_algorithms import fuzzify, calculate_output_components_and_power

# Setup an EV_scenario object and print results
from util.ev_scenario import EV_scenario
from util.ev_group import EV_group


# Example usage
flc_voltage = fmf.FLC_voltage()
flc_SOC = fmf.FLC_SOC()
flc_energy_csc = fmf.FLC_energy_csc()
flc_energy_v2g = fmf.FLC_energy_v2g()

# Initialize scenario 1 from the paper
ev_group01 = EV_group(SOC=30, energy_rating=10, N=25)
ev_group02 = EV_group(SOC=60, energy_rating=16, N=25)
ev_group03 = EV_group(SOC=90, energy_rating=20, N=50)

ev_scenario01 = EV_scenario(ev_group01, ev_group02, ev_group03)
ev_scenario01.print_scenario()

print("\n")

# Initialize scenario 2 from the paper
ev_group01 = EV_group(SOC=20, energy_rating=10, N=20)
ev_group02 = EV_group(SOC=40, energy_rating=16, N=30)
ev_group03 = EV_group(SOC=80, energy_rating=20, N=50)

ev_scenario02 = EV_scenario(ev_group01, ev_group02, ev_group03)
ev_scenario02.print_scenario()

print("\n")


if __name__ == "__main__":
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    # Define grid energy requirement
    grid_energy_requirement = 0.4 # Example value, adjust as needed
    time_steps = 100  # Number of time steps to simulate
    power_outputs_stability = []  # To store power outputs over time

    # Random starting point for EV scenario 1
    plt.figure(figsize=(10, 5))
    for initial_soc in [20, 30, 40, 50, 60, 70, 80]:
        time_steps = 100  # Number of time steps to simulate
        power_outputs_stability = []  # To store power outputs over time

        initial_soc = initial_soc / 100  # Convert SOC to percentage
        initial_soc = round(initial_soc, 2)  # Round to 2 decimal places
        print(f"Initial SOC: {initial_soc}")
        print("\n")
        ev_group01 = EV_group(SOC=initial_soc * 100, energy_rating=10, N=25)  # Scale SOC to percentage
        ev_scenario03 = EV_scenario(ev_group01, ev_group01, ev_group01)
        ev_scenario03.print_scenario()

        # Simulate over time
        for t in range(time_steps):
            actual_soc = round(initial_soc + (t * 0.01) % 0.1, 2) # Example SOC variation over time
            voltage_memberships = fuzzify(flc_voltage.membership_functions, grid_energy_requirement)
            soc_memberships = fuzzify(flc_SOC.membership_functions, actual_soc)
            
            # Calculate power output based on current SOC and grid requirement
            energy_csc, energy_desired = calculate_output_components_and_power(voltage_memberships, soc_memberships, fuzzy_lookup_csc(), flc_energy_csc)
            energy_memberships = fuzzify(flc_energy_csc.membership_functions, energy_desired)
            output_components, power_output = calculate_output_components_and_power(voltage_memberships, energy_memberships, fuzzy_lookup_v2g(), flc_energy_v2g)
            
            power_outputs_stability.append(power_output)
        
        # Plot the power output for each initial_soc
        plt.plot(range(time_steps), power_outputs_stability, label=f'Initial SOC: {initial_soc}')
        
        del time_steps, power_outputs_stability

    # Visualization of stability analysis
    plt.title(f'Stability Analysis of Power Output Over Time: Grid Energy Requirement = {grid_energy_requirement} p.u.')
    plt.xlabel('Time Steps')
    plt.ylabel('Power Output (p.u.)')
    plt.ylim(-1, 0)  # Set y-axis range to [-1, 1]


    plt.legend()
    plt.grid(True)
    plt.savefig(f"outputs/energy_req_{grid_energy_requirement}_all.png")
    print("SUCCESS: Stability analysis completed and saved as energy_req_0.4_all.png")
