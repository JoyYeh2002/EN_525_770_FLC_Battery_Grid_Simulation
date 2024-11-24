# import util.fuzzy_logic_controller
# import util.ev_scenario

# FLC = util.fuzzy_logic_controller.FLC()
# print(FLC)

import numpy as np
import matplotlib.pyplot as plt

class triangularMF:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def compute_membership(self, x_array):
        y_array = np.zeros_like(x_array)
        for i in range(len(self.points) - 1):
            x1, y1 = self.points[i]
            x2, y2 = self.points[i + 1]
            mask = (x_array >= x1) & (x_array <= x2)
            y_array[mask] = y1 + (y2 - y1) * (x_array[mask] - x1) / (x2 - x1)
        return y_array

class FLC_voltage:
    def __init__(self):
        self.membership_functions = [
            triangularMF("Very Low (VH)", [(0, 1), (0.8, 1), (0.875, 0)]),
            triangularMF("Low (L)", [(0.8, 0), (0.875, 1), (0.95, 0)]),
            triangularMF("Medium (M)", [(0.875, 0), (0.95, 1), (1.025, 0)]),
            triangularMF("High (H)", [(0.95, 0), (1.025, 1), (1.1, 0)]),
            triangularMF("Very High (VH)", [(1.025, 0), (1.1, 1), (1.2, 1)])
        ]
    
    def plot_membership_functions(self):
        # Generate x values for plotting
        x_values = np.linspace(0.75, 1.2, 500)

        # Compute and plot membership functions
        plt.figure(figsize=(10, 6))

        for mf in self.membership_functions:
            y_values = mf.compute_membership(x_values)
            plt.plot(x_values, y_values, label=mf.name, linewidth=2)

        # Plot formatting
        plt.title("Fuzzy Membership Functions for Voltage", fontsize=14)
        plt.xlabel("Voltage (p.u.)", fontsize=14)
        plt.ylabel("Membership Degree", fontsize=14)
        plt.legend(fontsize=14)
        plt.grid(True)
        plt.show()


class FLC_SOC:
    def __init__(self):
        self.membership_functions = [
            triangularMF("Very Low (VH)", [(0, 1), (10, 1), (32.5, 0)]),
            triangularMF("Low (L)", [(10, 0), (32.5, 1), (55, 0)]),
            triangularMF("Medium (M)", [(32.5, 0), (55, 1), (77.5, 0)]),
            triangularMF("High (H)", [(55, 0), (77.5, 1), (100, 0)]),
            triangularMF("Very High (VH)", [(77.5, 0), (100, 1), (110, 1)])
        ]
    
    def plot_membership_functions(self):
        # Generate x values for plotting
        x_values = np.linspace(0, 110, 500)

        # Compute and plot membership functions
        plt.figure(figsize=(10, 6))

        for mf in self.membership_functions:
            y_values = mf.compute_membership(x_values)
            plt.plot(x_values, y_values, label=mf.name, linewidth=2)

        # Plot formatting
        plt.title("Fuzzy Membership Functions for SOC", fontsize=14)
        plt.xlabel("State of Charge (%)", fontsize=14)
        plt.ylabel("Membership Degree", fontsize=14)
        plt.legend(fontsize=14)
        plt.grid(True)
        plt.show()

# Generate an array from -1 to 1 with increments of 2/9
N_energy_categories = 10
increment = 2 / (N_energy_categories - 1)
arr = np.arange(-1, 1+increment-1e-8, increment)
# [-1.         -0.77777778 -0.55555556 
# -0.33333333 -0.11111111  0.11111111
#   0.33333333  0.55555556  0.77777778  
# 1.          1.22222222]

class FLC_energy_csc:
    def __init__(self):
        self.membership_functions = [
            triangularMF("Very Negative High (VNH)", [(-1.1, 1), (-1, 1), (arr[1], 0)]),
            triangularMF("Negative High (NH)", [(-1, 0), (arr[1], 1), (arr[2], 0)]),
            triangularMF("Negative Medium (NM)", [(arr[1], 0), (arr[2], 1), (arr[3], 0)]),
            triangularMF("Negative Low (NL)", [(arr[2], 0), (arr[3], 1), (arr[4], 0)]),
            triangularMF("Very Negative Low (VNL)", [(arr[3], 0), (arr[4], 1), (arr[5], 0)]),
            triangularMF("Very Positive Low (VPL)", [(arr[4], 0), (arr[5], 1), (arr[6], 0)]),
            triangularMF("Positive Low (PL)", [(arr[5], 0), (arr[6], 1), (arr[7], 0)]),
            triangularMF("Positive Medium (PM)", [(arr[6], 0), (arr[7], 1), (arr[8], 0)]),
            triangularMF("Positive High (PH)", [(arr[7], 0), (arr[8], 1), (arr[9], 0)]),
            triangularMF("Very Positive High (VPH)", [(arr[8], 0), (arr[9], 1), (1.1, 1)])
        ]
    
    def plot_membership_functions(self):
        # Generate x values for plotting
        x_values = np.linspace(-1.1, 1.1, 500)

        # Compute and plot membership functions
        plt.figure(figsize=(10, 6))

        for mf in self.membership_functions:
            y_values = mf.compute_membership(x_values)
            plt.plot(x_values, y_values, label=mf.name, linewidth=2)

        # Plot formatting
        plt.title("Fuzzy Membership Functions for Energy", fontsize=14)
        plt.xlabel("Energy Level", fontsize=14)
        plt.ylabel("Membership Degree", fontsize=14)
        plt.legend(fontsize=9)
        plt.grid(True)
        plt.show()


# Generate an array from -1 to 1 with increments of 2/9
N_energy_categories = 12
increment = 2 / (N_energy_categories - 1)
arr = np.arange(-1, 1+increment-1e-8, increment)


class FLC_energy_v2g:
    def __init__(self):
        self.membership_functions = [
            triangularMF("Very Negative High (VNH)", [(-1.1, 1), (-1, 1), (arr[1], 0)]),
            triangularMF("Negative High (NH)", [(-1, 0), (arr[1], 1), (arr[2], 0)]),
            triangularMF("Negative Medium (NM)", [(arr[1], 0), (arr[2], 1), (arr[3], 0)]),
            triangularMF("Very Negative Medium (VNM)", [(arr[2], 0), (arr[3], 1), (arr[4], 0)]),
            triangularMF("Negative Low (NL)", [(arr[3], 0), (arr[4], 1), (arr[5], 0)]),
            triangularMF("Very Negative Low (VNL)", [(arr[4], 0), (arr[5], 1), (arr[6], 0)]),
            triangularMF("Very Positive Low (VPL)", [(arr[5], 0), (arr[6], 1), (arr[7], 0)]),
            triangularMF("Positive Low (PL)", [(arr[6], 0), (arr[7], 1), (arr[8], 0)]),
            triangularMF("Positive Medium (PM)", [(arr[7], 0), (arr[8], 1), (arr[9], 0)]),
            triangularMF("Very Positive Medium (VPM)", [(arr[8], 0), (arr[9], 1), (arr[10], 0)]),
            triangularMF("Positive High (PH)", [(arr[9], 0), (arr[10], 1), (arr[11], 0)]),
            triangularMF("Very Positive High (VPH)", [(arr[10], 0), (arr[11], 1), (1.1, 1)])
        ]
    def plot_membership_functions(self):
        # Generate x values for plotting
        x_values = np.linspace(-1.1, 1.1, 500)

        # Compute and plot membership functions
        plt.figure(figsize=(10, 6))

        for mf in self.membership_functions:
            y_values = mf.compute_membership(x_values)
            plt.plot(x_values, y_values, label=mf.name, linewidth=2)

        # Plot formatting
        plt.title("Fuzzy Membership Functions for Energy Output (V2G)", fontsize=14)
        plt.xlabel("Energy Level", fontsize=14)
        plt.ylabel("Membership Degree", fontsize=14)
        plt.legend(fontsize=9)
        plt.grid(True)
        plt.show()

# Example usage
flc_voltage = FLC_voltage()
flc_SOC = FLC_SOC()
flc_energy_csc = FLC_energy_csc()
flc_energy_v2g = FLC_energy_v2g()

# flc_voltage.plot_membership_functions()
# flc_SOC.plot_membership_functions()
# flc_energy_csc.plot_membership_functions()
# flc_energy_v2g.plot_membership_functions()