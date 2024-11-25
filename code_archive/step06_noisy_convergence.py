import numpy as np
import matplotlib.pyplot as plt

# Create time array
t = np.linspace(0, 0.5, 1000)

# Create base power curve
def create_power_curve(t):
    power = np.zeros_like(t)
    
    # Initial fluctuation
    mask1 = t < 0.02
    power[mask1] = -40000 + 10000 * np.sin(2 * np.pi * 50 * t[mask1])
    
    # Steep decline
    mask2 = (t >= 0.02) & (t < 0.15)
    power[mask2] = -40000 - 30000 * (t[mask2] - 0.02) / 0.13
    
    # Stabilization
    mask3 = t >= 0.15
    power[mask3] = -70000
    
    return power

# Generate base power
power = create_power_curve(t)

# Add noise with level 1000 for t = 0 to t = 0.18
noise_levels = np.full(len(t[t <= 0.18]), 700)
noise = np.random.normal(0, noise_levels, len(t[t <= 0.18]))
noisy_power = power.copy()
noisy_power[t <= 0.18] += noise

# Decrease noise from 300 to 0 for t = 0.18 to t = 0.24
mask_decrease_noise = (t > 0.18) & (t <= 0.24)
noise_decrease = np.linspace(300, 150, len(t[mask_decrease_noise]))
noisy_power[mask_decrease_noise] += noise_decrease

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, noisy_power/10000, 'b-', linewidth=1)

# Formatting
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlabel('Time (seconds)')
plt.ylabel('Power (W)')
plt.title('EVs Discharging to the Grid with Noise')

# Set y-axis limits similar to original
plt.ylim(-8, -2)

# Add text annotation for power level
plt.text(0.35, -2.5, '70 kW', fontsize=10)

# Scientific notation on y-axis
plt.gca().yaxis.set_major_formatter(plt.ScalarFormatter(useMathText=True))
plt.gca().ticklabel_format(axis='y', style='sci', scilimits=(0,0))

# Show plot
plt.tight_layout()
plt.show()