
# Skeleton code for a lookup table function with 50 rules
class fuzzy_lookup_csc:
    def __init__(self):
        # Define the lookup table as a dictionary
        self.rules = {
            ('VL', 'VL'): 'VPL',
            ('VL', 'L'): 'PL',
            ('VL', 'M'): 'PM',
            ('VL', 'H'): 'PH',
            ('VL', 'VH'): 'VPH',

            ('L', 'VL'): 'VPL',
            ('L', 'L'): 'PL',
            ('L', 'M'): 'PM',
            ('L', 'H'): 'PH',
            ('L', 'VH'): 'PH',
            
            ('M', 'VL'): 'VNL',
            ('M', 'L'): 'VPL',
            ('M', 'M'): 'PL',
            ('M', 'H'): 'PM',
            ('M', 'VH'): 'PM',

            ('H', 'VL'): 'VNH',
            ('H', 'L'): 'NH',
            ('H', 'M'): 'NM',
            ('H', 'H'): 'NL',
            ('H', 'VH'): 'VNL',

            ('VH', 'VL'): 'VNH',
            ('VH', 'L'): 'NH',
            ('VH', 'M'): 'NM',
            ('VH', 'H'): 'NL',
            ('VH', 'VH'): 'VNL',
        }

    def get_output(self, voltage, soc):
        """
        Retrieve the output based on the given voltage and energy inputs.
        
        Args:
            voltage (str): Voltage linguistic label (e.g., 'VL', 'L', 'M', etc.)
            soc (str): State of charge linguistic label (e.g., 'VNH', 'NH', 'PL', etc.)
        
        Returns:
            str: The output linguistic label (e.g., 'VPL', 'PL', etc.)
                  Returns None if the combination is not found in the rules.
        """
        return self.rules.get((voltage, soc), None)
    
class fuzzy_lookup_v2g:
    def __init__(self):
        # Define the lookup table as a dictionary
        self.rules = {
            ('VL', 'VNH'): 'VPL',
            ('VL', 'NH'): 'VPL',
            ('VL', 'NM'): 'VPL',
            ('VL', 'NL'): 'VPL',
            ('VL', 'VNL'): 'VPL',
            ('VL', 'VPL'): 'VNL',
            ('VL', 'PL'): 'VNL',
            ('VL', 'PM'): 'NH',
            ('VL', 'PH'): 'VNH',
            ('VL', 'VPH'): 'VNH',
            
            ('L', 'VNH'): 'PL',
            ('L', 'NH'): 'PL',
            ('L', 'NM'): 'PL',
            ('L', 'NL'): 'PL',
            ('L', 'VNL'): 'PL',
            ('L', 'VPL'): 'VNL',
            ('L', 'PL'): 'NL',
            ('L', 'PM'): 'VNH',
            ('L', 'PH'): 'VH',
            ('L', 'VPH'): 'NH',

            ('M', 'VNH'): 'PM',
            ('M', 'NH'): 'VPM',
            ('M', 'NM'): 'PM',
            ('M', 'NL'): 'PM',
            ('M', 'VNL'): 'VNL',
            ('M', 'VPL'): 'NL',
            ('M', 'PL'): 'NM',
            ('M', 'PM'): 'NM',
            ('M', 'PH'): 'NM',
            ('M', 'VPH'): 'VNM',

            ('H', 'VNH'): 'VPM',
            ('H', 'NH'): 'PH',
            ('H', 'NM'): 'VPM',
            ('H', 'NL'): 'PH',
            ('H', 'VNL'): 'NL',
            ('H', 'VPL'): 'PL',
            ('H', 'PL'): 'NM',
            ('H', 'PM'): 'NL',
            ('H', 'PH'): 'NL',
            ('H', 'VPH'): 'VNL',

            ('VH', 'VNH'): 'PH',
            ('VH', 'NH'): 'VPH',
            ('VH', 'NM'): 'PH',
            ('VH', 'NL'): 'VPH',
            ('VH', 'VNL'): 'NM',
            ('VH', 'VPL'): 'VPL',
            ('VH', 'PL'): 'VNM',
            ('VH', 'PM'): 'VNL',
            ('VH', 'PH'): 'VNL',
            ('VH', 'VPH'): 'VNL',

        }

    def get_output(self, voltage, energy):
        """
        Retrieve the output based on the given voltage and energy inputs.
        
        Args:
            voltage (str): Voltage linguistic label (e.g., 'VL', 'L', 'M', etc.)
            energy (str): Energy linguistic label (e.g., 'VNH', 'NH', 'PL', etc.)
        
        Returns:
            str: The output linguistic label (e.g., 'VPL', 'PL', etc.)
                  Returns None if the combination is not found in the rules.
        """
        return self.rules.get((voltage, energy), None)