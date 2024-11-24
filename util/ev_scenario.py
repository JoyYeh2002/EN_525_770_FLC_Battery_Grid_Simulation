# Import the EV_group class from ev_config
from util.ev_group import EV_group

# Initialize an object of the EV_group class
class EV_scenario:
    def __init__(self, EV_group01, EV_group02, EV_group03):
        self.ev_group01 = EV_group01
        self.ev_group02 = EV_group02
        self.ev_group03 = EV_group03
        self.total_energy_charging = EV_group01.tot_energy_charging + EV_group02.tot_energy_charging + EV_group03.tot_energy_charging
        self.total_energy_discharging = EV_group01.tot_energy_discharging + EV_group02.tot_energy_discharging + EV_group03.tot_energy_discharging
    
    def print_scenario(self):
        print(f"Total Energy Charging: {self.total_energy_charging} kWh")
        print(f"Total Energy Discharging: {self.total_energy_discharging} kWh")
        print("EV Group Information:")
        print(f"EV Group 01 - N: {self.ev_group01.N}, SOC: {self.ev_group01.SOC}%, Energy Rating: {self.ev_group01.energy_rating} kWh, charging: {self.ev_group01.tot_energy_charging} kWh, discharging: {self.ev_group01.tot_energy_discharging} kWh")
        print(f"EV Group 02 - N: {self.ev_group02.N}, SOC: {self.ev_group02.SOC}%, Energy Rating: {self.ev_group02.energy_rating} kWh, charging: {self.ev_group02.tot_energy_charging} kWh, discharging: {self.ev_group02.tot_energy_discharging} kWh")
        print(f"EV Group 03 - N: {self.ev_group03.N}, SOC: {self.ev_group03.SOC}%, Energy Rating: {self.ev_group03.energy_rating} kWh, charging: {self.ev_group03.tot_energy_charging} kWh, discharging: {self.ev_group03.tot_energy_discharging} kWh")