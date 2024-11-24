# Setup an EV_scenario object and print results
from util.ev_scenario import EV_scenario
from util.ev_group import EV_group

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

