import math
from rx import medications

print(medications)

class Patient():
    
     def __init__(self, first_name, last_name, gender, age, weight, height, ethnicity, albumin_units, serum_creatine_units, 
          cystatin_c, blood_urine_nitrogen, mic_of_organism):
          self.first_name = first_name
          self.last_name = last_name
          self.age = age
          self.gender = gender
          self.weight = weight
          self.height = height
          self.ethnicity = ethnicity
          self.albumin_units = albumin_units
          self.serum_creatine_units = serum_creatine_units
          self.cystatin_c = cystatin_c
          self.blood_urine_nitrogen = blood_urine_nitrogen
          self.mic_of_organism = mic_of_organism
          Patient.print_calculated_patient_info(self)
     
     def print_patient_info(self):
          print(f"""
          ******************************************************************************************
          First Name: {self.first_name.title()}
          Last Name: {self.last_name.title()}
          Age: {self.age}
          Gender: {self.gender.title()}
          Weight(kg) {self.weight}
          Height(in) {self.height}
          Ethnicity: {self.ethnicity.title()}
          Albumin: {self.albumin_units}
          Serum Creatine: {self.serum_creatine_units}
          Cystatin C(mg/dl): {self.cystatin_c}
          Blood Urine Nitrogen(BUN)(mg/dl): {self.blood_urine_nitrogen}
          Actual or presumed MIC of organism: {self.mic_of_organism}
          ******************************************************************************************
          """)

     def calc_bmi(self):
         self.bmi = (self.weight / (self.height * 0.0254) ** 2)
     #     print(f'BMI: {self.bmi}')
         return self.bmi
     
     def calc_ideal_body_weight(self):
          if self.gender == 'female':
               if self.height >= 60:
                    self.ideal_body_weight = 45 + 2.3 * (self.height - 60)
               else:
                    self.ideal_body_weight = 45.5 - ((60 - self.height) * 0.76)
          else:
               if self.height >= 60:
                    self.ideal_body_weight = 50 + 2.3 * (self.height - 60)
               else:
                    self.ideal_body_weight = 50 - ((60 - self.height) * 0.83)
          # print(f'Ideal Body Weight: {self.ideal_body_weight}')
          return self.ideal_body_weight
     
     def calc_adjusted_body_weight(self):
          self.adjusted_body_weight = (self.weight - self.ideal_body_weight) * 0.4 + self.ideal_body_weight
          # print(f'Adjusted Body Weight: {self.adjusted_body_weight}')
          return self.adjusted_body_weight

     def calc_grubb_equation(self):
          self.grubb_equation = 83.93 * (self.cystatin_c ** -1.676)
          # print(f'Grubb Equation: {self.grubb_equation}')
          return self.grubb_equation

     def calc_larsonns_equation(self):
         self.larsson_equation = 77.239 * (self.cystatin_c ** -1.2623)
     #     print(f'Larssons Equation: {self.larsson_equation}')
         return self.larsson_equation

     def calc_cockcroft_gault(self):
          # Need to come back and verify these with a variety of weights + gender 
          if self.gender == 'male':
               gender = 1
          else:
               gender = 0.85
          
          if self.weight < self.ideal_body_weight:
               weight = self.weight
          elif (self.weight >= self.ideal_body_weight) >= 1.4:
               weight = self.adjusted_body_weight
          else:
               weight = self.adjusted_body_weight

          if self.albumin_units >= 3:
               albumin = 0
          else:
               albumin = -15
          self.cc = ((140 - self.age) * weight /(72 * self.serum_creatine_units) + albumin) * gender

          # print(f'Modified Cockcroft Gault: {self.cc}')
          return self.cc
     
     def calc_mdmr6(self):
          if self.gender == 'male':
               gender = 1
          else:
               gender = 0.85

          if self.ethnicity == 'african american'          :
               ethnicity = 1.18
          else:
               ethnicity = 1
          
          self.mdmr = 170 * (self.serum_creatine_units ** -0.999) * (self.age ** -0.176) * (self.blood_urine_nitrogen ** -0.17) * (self.albumin_units ** 0.318) * (gender) * (ethnicity)
          # print(f'MDMR: {self.mdmr}')
          return self.mdmr
     
     def print_calculated_patient_info(self):
          print(f"""
          ******************************************************************************************
          BMI: {self.calc_bmi()}
          Grubb equation: {self.calc_grubb_equation()}
          Larson's Equation: {self.calc_larsonns_equation()}
          Ideal Body Weight: {self.calc_ideal_body_weight()}
          Adjusted Body Weight: {self.calc_adjusted_body_weight()}
          Modified Cockcroft Gault: {self.calc_cockcroft_gault()}
          MDMR6: {self.calc_mdmr6()}
          ******************************************************************************************
          """)

     class Medication():
          # Variables that should auto add
          # liters, slope, non_renal_clearance, clearance_used, half_life, fcpss
          def __init__(self, dose, infusion_time, frequency, liters, slope, non_renal_clearance, clearance_used, half_life, fcpss):
               self.dose = dose
               self.infusion_time = infusion_time
               self.frequency = frequency
               self.liters = liters
               self.slope = slope
               self.non_renal_clearance = non_renal_clearance
               self.clearance_used = clearance_used
               self.half_life = half_life
               self.fcpss = fcpss
          
          def request_medicine(self):
               self.patient_rx = input('Which medication would you like to use?\n')
               for rx in medications:
                    if self.patient_rx.lower() == rx['medication']:
                              self.patient_rx = rx['medication']
                              self.patient_rx_liters = rx['liters']
                              self.patient_rx_slope = rx['slope']
                              self.patient_rx_non_renal_clearance = rx['non_renal_clearance']
                              self.patient_rx_half_life = rx['half_life']
                              self.patient_rx_fcpss = rx['fcpss']
                              break
                    else:
                         print('No medication found')
                         continue
               return [self.patient_rx, self.patient_rx_liters, self.patient_rx_slope, self.patient_rx_non_renal_clearance, self.patient_rx_half_life, self.patient_rx_fcpss]
          
          def calc_rate(self):
               self.rate = ((24 / self.frequency) * self.dose) / 24
               print(f'Rate(mg/hr) {self.rate}')
               return self.rate

          def calc_drug_clearance_ml_min(self):
               self.drug_clearance_ml_min = (self.slope * self.clearance_used) + self.non_renal_clearance
               print(f'Drug Clearance (mL/min): {self.drug_clearance_ml_min}')      
               return self.drug_clearance_ml_min
          
          def calc_drug_clearance_l_hr(self):
               self.drug_clearance_l_hr = self.drug_clearance_ml_min * 0.06
               print(f'Drug Clearance (L/hr): {self.drug_clearance_l_hr}')
               return self.drug_clearance_l_hr

          def calc_volume_of_distribution(self):
               adjbw = patient.calc_adjusted_body_weight()
               self.volume_distribution = self.liters * adjbw
               print(f'VD: {self.volume_distribution}')
               return self.volume_distribution
          
          # What do these values stand for? k hr -1
          def calc_k_hr_1(self):
               self.k_hr_1 = self.drug_clearance_l_hr / self.volume_distribution
               print(f'K hr-1: {self.k_hr_1}')
               return self.k_hr_1
          
          # In half life calc, what is 0.693? What should the variable be called?
          def calc_half_life(self):
               self.half_life_calculated = self.half_life / self.k_hr_1
               print(f'Half-life(hr): {self.half_life_calculated}')

          def calc_cpss_with_cl(self):
               self.cpss_with_cl = (self.dose / self.frequency) / self.drug_clearance_l_hr
               print(f'CpSS with Cl: {self.cpss_with_cl}')
               return self.cpss_with_cl

          def calc_cpss_max(self):
               self.cpss_max = (self.dose / self.infusion_time) * (1 - math.exp(-self.k_hr_1 * (self.infusion_time))) / (self.volume_distribution * self.k_hr_1 * (1 - math.exp(-self.k_hr_1 * self.frequency)))
               print(f'CpSS(Max): {self.cpss_max}')
               return self.cpss_max

          def calc_cpss_min(self):
               self.cpss_min = self.cpss_max * math.exp(-self.k_hr_1 * (self.frequency - self.infusion_time))
               print(f'CpSS(Min): {self.cpss_min}')
               return self.cpss_min

          # Tissue concentration
          # What is the variable being subtracted by 1 called?
          def calc_fcpss_ave_or_cl(self):
               self.fcpss_calculated = (1 - self.fcpss) *self.cpss_with_cl
               print(f'fCpSS(ave or Cl): {self.fcpss_calculated}')
               return self.fcpss_calculated

          def calc_fcpss_max(self):
               self.fcpss_max = (1 - self.fcpss) * self.cpss_max
               print(f'fCpSS(Max): {self.fcpss_max}')
               return self.fcpss_max

          def calc_fcpss_min(self):
               self.fcpss_min = (1 - self.fcpss) * self.cpss_min
               print(f'fCpSS(Min): {self.fcpss_min}')
               return self.fcpss_min
          

patient = Patient('andre', 'lonardo', 'male', 20, 60, 65, 'african american', 3.2, 0.7, 1.5, 41, 8.0)
piperacillin = patient.Medication(2000, 1, 12, 0.3, 1.36,105, 150, 0.693, 0.16)

piperacillin.calc_rate()
piperacillin.calc_volume_of_distribution()
piperacillin.calc_drug_clearance_ml_min()
piperacillin.calc_drug_clearance_l_hr()
piperacillin.calc_k_hr_1()
piperacillin.calc_half_life()
piperacillin.calc_cpss_with_cl()
piperacillin.calc_cpss_max()
piperacillin.calc_cpss_min()
piperacillin.calc_fcpss_ave_or_cl()
piperacillin.calc_fcpss_max()
piperacillin.calc_fcpss_min()


