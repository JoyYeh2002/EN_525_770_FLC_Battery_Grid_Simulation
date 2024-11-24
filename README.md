# FLC_Battery_Grid_Simulation
Johns Hopkins University, EN.525.770 Intelligent Algorithms
Fall 2024 Semester Final Project: Fuzzy Logic Controller for EV and Voltage-to-Grid Charging

## Project Outline
This repository implements the following:
1. Reproduce the main simulation results of this paper in Python: 
Singh, M., Kumar, P., & Kar, I. (2012). Implementation of vehicle to grid infrastructure using fuzzy logic controller. IEEE Transactions on Smart Grid, 3(1), 565-577.
2. Experiment with more configurations of EVs, in addition to the two presented in the paper
3. Experiment with other inference methods
4. Find the optimal structures in terms of settle time and reuslting power storage optimization thorugh parameter sweeps and visualizaiton

## Code Structure
1. `EV_config`: A Python class that sets up the properties of the group of EVs that interacts with the grid
- `EV_group`: A class representing one spefific EV group, out of 3-5 groups in the whole EV population:
-- `N`: number of EVs
-- `SOC`: state of charge of these EVs(%)
-- `energy_rating`: The energy ratings (kWh)
-- `energy_available`: Available energy for grid support (kWh)
-- `SOC_req_charging`: SOC required for charging (kWh)
-- `SOC_req_discharging`: SOC required for discharging (kWh)
- `tot_energy_charging`: Total energy for charging (kWh)
- `tot_energy_discharging`: Total energy for discharging (kWh)

2. `FLC`: the fuzzy logic controller class
- `MF_type`: default to triangular membership function
- `inference_method`: default to min() function
- `defuzzification_method`: default to center of gravity (CoG) method
- `linguistic_variables`: dictionary key is the of the linguistic variable, value is a list of the categories (very low, medium, high, etc.)
-- voltage: Very low (VL), low (L), medium (M), high (H), very high (VH)
-- charge/discharge energy: Very negative high (VNH), negative high (NH), negative medium (NM), negative low (NL), very negative low (VNL), very positive low (VPL), positive low (PL), positive medium (PM), positive high (PH), very positive high (VPH)




