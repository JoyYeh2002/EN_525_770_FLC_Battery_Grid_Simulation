class FLC:
    def __init__(self):
        # Membership function type
        self.MF_type = 'triangular'  # default to triangular membership function
        
        # Inference method
        self.inference_method = min  # default to min() function
        
        # Defuzzification method
        self.defuzzification_method = 'center of gravity'  # default to CoG method
        
        # Linguistic variables
        self.linguistic_variables = {
            'voltage': ['Very low (VL)', 'Low (L)', 'Medium (M)', 'High (H)', 'Very high (VH)'],
            'charge/discharge energy': [
                'Very negative high (VNH)', 'Negative high (NH)', 'Negative medium (NM)', 
                'Negative low (NL)', 'Very negative low (VNL)', 'Very positive low (VPL)', 
                'Positive low (PL)', 'Positive medium (PM)', 'Positive high (PH)', 
                'Very positive high (VPH)'
            ]
        }