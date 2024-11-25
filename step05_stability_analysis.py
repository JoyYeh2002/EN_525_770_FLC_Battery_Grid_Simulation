import numpy as np
import matplotlib.pyplot as plt

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

# Define the hypothetical goal for power output
goal_power_output = 0.95  # Desired power output in p.u.
time_steps = 200  # Number of time steps to simulate
power_outputs = []  # To store power outputs over time

# Define EV scenario parameters
initial_soc = np.random.uniform(0.1, 0.5)  # Random SOC between 0.1 and 0.5
voltage_rating = 0.9  # Example voltage rating in p.u.
num_vehicles = 25  # Number of vehicles
energy_capacity = 10  # Energy capacity of each vehicle in kWh

# Create EV group and scenario
ev_group = EV_group(SOC=initial_soc * 100, energy_rating=energy_capacity, N=num_vehicles)  # Scale SOC to percentage
ev_scenario = EV_scenario(ev_group01, ev_group02, ev_group03)
import numpy as np
import matplotlib.pyplot as plt

# Define the hypothetical goal for power output
goal_power_output = 0.95  # Desired power output in p.u.
time_steps = 200  # Number of time steps to simulate
power_outputs = []  # To store power outputs over time

# Define EV scenario parameters
initial_soc = np.random.uniform(0.1, 0.5)  # Random SOC between 0.1 and 0.5
voltage_rating = 0.9  # Example voltage rating in p.u.
num_vehicles = 25  # Number of vehicles
energy_capacity = 10  # Energy capacity of each vehicle in kWh

# Create EV group and scenario
ev_group = EV_group(SOC=initial_soc * 100, energy_rating=energy_capacity, N=num_vehicles)  # Scale SOC to percentage
ev_scenario = EV_scenario(ev_group)

# Simulate over time
for t in range(time_steps):
    # Introduce oscillatory behavior in SOC
    if t % 20 < 10:
        # Charging phase
        ev_group.SOC += np.random.uniform(1.0, 2.0)  # Increase SOC more aggressively
    else:
        # Discharging phase
        ev_group.SOC -= np.random.uniform(0.5, 1.5)  # Decrease SOC more aggressively

    # Ensure SOC stays within bounds
    ev_group.SOC = max(0, min(100, ev_group.SOC))

    # Fuzzify inputs
    voltage_memberships = fuzzify(flc_voltage.membership_functions, voltage_rating)
    soc_memberships = fuzzify(flc_SOC.membership_functions, ev_group.SOC / 100)  # Normalize SOC for fuzzification

    # Calculate power output based on current SOC and voltage
    energy_csc, energy_desired = calculate_output_components_and_power(voltage_memberships, soc_memberships, fuzzy_lookup_csc(), flc_energy_csc)
    energy_memberships = fuzzify(flc_energy_csc.membership_functions, energy_desired)
    output_components, power_output = calculate_output_components_and_power(voltage_memberships, energy_memberships, fuzzy_lookup_v2g(), flc_energy_v2g)

    power_outputs.append(power_output)

# Visualization of charging state vs. time
plt.figure(figsize=(10, 5))
plt.plot(range(time_steps), power_outputs, label='Power Output', color='blue')
plt.axhline(y=goal_power_output, color='red', linestyle='--', label='Goal Power Output (0.95 p.u.)')
plt.title('Charging State vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Output Power (p.u.)')
plt.ylim(-1, 1)  # Set y-axis range to visualize charging/discharging
plt.legend()
plt.grid(True)
plt.savefig(f"outputs/charging_state_vs_time.png")
print("SUCCESS: Charging state simulation completed and saved as charging_state_vs_time.png")