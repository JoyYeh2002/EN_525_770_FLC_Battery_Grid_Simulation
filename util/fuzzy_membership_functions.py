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
            triangularMF("VL", [(0, 1), (0.8, 1), (0.875, 0)]),
            triangularMF("L", [(0.8, 0), (0.875, 1), (0.95, 0)]),
            triangularMF("M", [(0.875, 0), (0.95, 1), (1.025, 0)]),
            triangularMF("H", [(0.95, 0), (1.025, 1), (1.1, 0)]),
            triangularMF("VH", [(1.025, 0), (1.1, 1), (1.2, 1)])
        ]

    def get_membership_function(self, name):
        for mf in self.membership_functions:
            if mf.name == name:
                return mf
        return None  # Return None if not found
    
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
            triangularMF("VL", [(0, 1), (0.1, 1), (0.325, 0)]),
            triangularMF("L", [(0.1, 0), (0.325, 1), (0.55, 0)]),
            triangularMF("M", [(0.325, 0), (0.55, 1), (0.775, 0)]),
            triangularMF("H", [(0.55, 0), (0.775, 1), (1, 0)]),
            triangularMF("VH", [(0.775, 0), (1, 1), (1.1, 1)])
        ]

    def get_membership_function(self, name):
        for mf in self.membership_functions:
            if mf.name == name:
                return mf
        return None  # Return None if not found
    
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
N_categories_csc = 9
increment_csc = 2 / N_categories_csc
arr01 = np.arange(-1, 1+increment_csc-1e-8, increment_csc)

class FLC_energy_csc:
    def __init__(self):
        self.membership_functions = [
            triangularMF("VNH", [(-1.1, 1), (-1, 1), (arr01[1], 0)]),
            triangularMF("NH", [(-1, 0), (arr01[1], 1), (arr01[2], 0)]),
            triangularMF("NM", [(arr01[1], 0), (arr01[2], 1), (arr01[3], 0)]),
            triangularMF("NL", [(arr01[2], 0), (arr01[3], 1), (arr01[4], 0)]),
            triangularMF("VNL", [(arr01[3], 0), (arr01[4], 1), (arr01[5], 0)]),
            triangularMF("VPL", [(arr01[4], 0), (arr01[5], 1), (arr01[6], 0)]),
            triangularMF("PL", [(arr01[5], 0), (arr01[6], 1), (arr01[7], 0)]),
            triangularMF("PM", [(arr01[6], 0), (arr01[7], 1), (arr01[8], 0)]),
            triangularMF("PH", [(arr01[7], 0), (arr01[8], 1), (arr01[9], 0)]),
            triangularMF("VPH", [(arr01[8], 0), (arr01[9], 1), (1.1, 1)])
        ]

    def get_membership_function(self, name):
        for mf in self.membership_functions:
            if mf.name == name:
                return mf
        return None  # Return None if not found
    
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
N_categories_v2g = 12
increment_v2g = 2 / (N_categories_v2g - 1)
arr02 = np.arange(-1, 1+increment_v2g-1e-8, increment_v2g)

class FLC_energy_v2g:
    def __init__(self):
        self.membership_functions = [
            triangularMF("VNH", [(-1.1, 1), (-1, 1), (arr02[1], 0)]),
            triangularMF("NH", [(-1, 0), (arr02[1], 1), (arr02[2], 0)]),
            triangularMF("NM", [(arr02[1], 0), (arr02[2], 1), (arr02[3], 0)]),
            triangularMF("VNM", [(arr02[2], 0), (arr02[3], 1), (arr02[4], 0)]),
            triangularMF("NL", [(arr02[3], 0), (arr02[4], 1), (arr02[5], 0)]),
            triangularMF("VNL", [(arr02[4], 0), (arr02[5], 1), (arr02[6], 0)]),
            triangularMF("VPL", [(arr02[5], 0), (arr02[6], 1), (arr02[7], 0)]),
            triangularMF("PL", [(arr02[6], 0), (arr02[7], 1), (arr02[8], 0)]),
            triangularMF("PM", [(arr02[7], 0), (arr02[8], 1), (arr02[9], 0)]),
            triangularMF("VPM", [(arr02[8], 0), (arr02[9], 1), (arr02[10], 0)]),
            triangularMF("PH", [(arr02[9], 0), (arr02[10], 1), (arr02[11], 0)]),
            triangularMF("VPH", [(arr02[10], 0), (arr02[11], 1), (1.1, 1)])
        ]

    def get_membership_function(self, name):
        for mf in self.membership_functions:
            if mf.name == name:
                return mf
        return None  # Return None if not found
    
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