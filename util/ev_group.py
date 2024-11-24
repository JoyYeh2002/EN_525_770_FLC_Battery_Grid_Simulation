# ev_config.py
class EV_group:
    def __init__(self, SOC, energy_rating, N, discharge_maintenance_level=50):
        """
        Initialize the EV group with the given parameters.

        :param N: Number of EVs
        :param SOC: State of charge of these EVs (%)
        :param energy_rating: The energy ratings (kWh)
        :param energy_available: Available energy for grid support (kWh)
        :param SOC_req_charging: SOC required for charging (kWh)
        :param SOC_req_discharging: SOC required for discharging (kWh)
        """
        self.N = N
        self.SOC = SOC
        self.energy_rating = energy_rating
        self.tot_energy_charging = N * energy_rating * ((100 - SOC) / 100)  # Total energy for charging (kWh)
        self.tot_energy_discharging = N * energy_rating * ((SOC - discharge_maintenance_level) / 100)  # Total energy for discharging (kWh)

# Example usage
if __name__ == "__main__":
    ev_group = EV_group(N=5, SOC=80, energy_rating=50, energy_available=200, SOC_req_charging=90, SOC_req_discharging=20)
    print(f"Total energy for charging: {ev_group.tot_energy_charging} kWh")
    print(f"Total energy for discharging: {ev_group.tot_energy_discharging} kWh")