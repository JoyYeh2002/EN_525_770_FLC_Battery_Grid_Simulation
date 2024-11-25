# Re-import required libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, step
# Adjust the simulation to include significant oscillations before stabilizing

def simulate_oscillatory_pid_behavior():
    """
    Simulate a PID-like behavior with significant overshoot and undershoot
    before stabilizing.
    """
    # Define a second-order underdamped system to simulate oscillations
    # Transfer function: G(s) = wn^2 / (s^2 + 2*z*wn*s + wn^2)
    wn = 30  # Natural frequency (rad/s)
    zeta = 0.1  # Damping ratio (underdamped)
    
    num = [wn**2]  # Numerator coefficients
    den = [1, 2*zeta*wn, wn**2]  # Denominator coefficients

    system = lti(num, den)  # Create the system
    t = np.linspace(0, 0.6, 1000)  # Time from 0 to 0.6 seconds
    t, y = step(system, T=t)  # Compute the step response

    # Introduce a stabilization point at -1e5 after 0.2 seconds
    y[t >= 0.2] = 1  # Stabilize the response at a normalized value of 1

    return t, y

# Scale and adjust the power signal
def adjust_power_signal_oscillatory(time, signal):
    power = -1.2e5 + (0.2e5) * signal  # Scale to desired range
    power = np.clip(power, -1.2e5, -1e5)  # Ensure limits
    return power

# Simulate the oscillatory PID-like behavior
time, pid_signal = simulate_oscillatory_pid_behavior()
power = adjust_power_signal_oscillatory(time, pid_signal)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(time, power, label="Power (PID-like oscillatory response)", color="b")
plt.axhline(-1e5, color="g", linestyle="--", label="Stabilization point (-100 kW)")

# Add plot details
plt.title("Time vs. Power Plot (Oscillatory PID-like Behavior)", fontsize=14)
plt.xlabel("Time (s)", fontsize=12)
plt.ylabel("Power (W)", fontsize=12)
plt.legend(fontsize=12)
plt.grid()
plt.show()
