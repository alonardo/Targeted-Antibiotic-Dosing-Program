#  slope is x, non renal clearance is y
# Questions
# Why do some drugs not have a non-renal clearance?
# What do these values stand for? k hr -1
# In half life calc, what is 0.693? What should the variable be called?
medications =  [{
                'medication': 'cefepime',
                'liters': 0.26,
                'slope': 0.96,
                'non_renal_clearance': 10.82,
                'half_life': 0.693,
                'fcpss': 0.16
                },
                {
                'medication': 'piperacillin',
                'liters': 0.3,
                'slope': 1.36,
                'non_renal_clearance': 105,
                'half_life': 0.693,
                'fcpss': 0.16
                },
                {
                'medication': 'meropenem',
                'liters': 0.23,
                'slope': 1.71,
                'non_renal_clearance': 14,
                'half_life': 0.693,
                'fcpss': 0.05
                },    
                {
                'medication': 'ceftazidime',
                'liters': 0.21,
                'slope': 0.95,
                'non_renal_clearance': 6.59,
                'half_life': 0.693,
                'fcpss': 0.05
                },
                {
                'medication': 'ampicillin',
                'liters': 0.28,
                'slope': 2.56,
                'non_renal_clearance': 29.9,
                'half_life': 0.693,
                'fcpss': 0.165
                }                  
            ]


def request_medicine():
    patient_rx = input('Which medication would you like to use?\n')
    for rx in medications:
        if patient_rx.lower() == rx['medication']:
                patient_rx = rx['medication']
                patient_rx_liters = rx['liters']
                patient_rx_slope = rx['slope']
                patient_rx_non_renal_clearance = rx['non_renal_clearance']
                patient_rx_half_life = rx['half_life']
                patient_rx_fcpss = rx['fcpss']
                break
        else:
            print('No medication found')
            continue
    return [patient_rx, patient_rx_liters, patient_rx_slope, patient_rx_non_renal_clearance, patient_rx_half_life, patient_rx_fcpss]
    

request_medicine()