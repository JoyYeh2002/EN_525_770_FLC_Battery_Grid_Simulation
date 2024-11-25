import numpy as np
import matplotlib.pyplot as plt

# Create time points
t = np.linspace(0, 0.5, 500)

# Create a simple discharge curve
power = -30000 * np.ones_like(t)  # Base level
power = power - 40000 * np.exp(-t/0.05)  # Add exponential decay

# Add some random noise
noise = np.random.normal(0, 1000, len(t))
power = power + noise

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(t, power/10000, 'b-', linewidth=1)

# Add labels and formatting
plt.xlabel('Time(seconds)')
plt.ylabel('Power(W)')
plt.grid(True, alpha=0.3)

# Set axis limits
plt.ylim(-8, -2)
plt.xlim(0, 0.5)

# Add text annotation
plt.text(0.35, -3, '70 kW', fontsize=10)

# Show plot
plt.tight_layout()
plt.show()