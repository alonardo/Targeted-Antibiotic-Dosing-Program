class Patient():
    
     def __init__(self, first_name, last_name, gender, age, weight, height, ethnicity, albumin_units, serum_creatine_units, cystatin_c, blood_urine_nitrogen, mic_of_organism):
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
     
     def print_patient_info(self):
          print(f'First Name: {self.first_name}'.title())
          print(f'Last Name: {self.last_name}'.title())
          print(f'Age: {self.age}')   
          print(f'Gender: {self.gender}'.title())
          print(f'Weight(kg): {self.weight}')
          print(f'Height(in): {self.height}')
          print(f'Ethnicity: {self.ethnicity}'.title())
          print(f'Albumin: {self.albumin_units}')
          print(f'Serum Creatine: {self.serum_creatine_units}')
          print(f'Cystatin C(mg/dL): {self.cystatin_c}')
          print(f'Blood Urine Nitrogen(BUN)(mg/dl): {self.blood_urine_nitrogen}')
          print(f'Actual or presumed MIC of organism: {self.mic_of_organism}')
          print('*********************************************')

     def calc_bmi(self):
         self.bmi = (self.weight / (self.height * 0.0254) ** 2)
         print(f'BMI: {self.bmi}')
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
          print(f'Ideal Body Weight: {self.ideal_body_weight}')
          return self.ideal_body_weight
     
     def calc_adjusted_body_weight(self):
          self.adjusted_body_weight = (self.weight - self.ideal_body_weight) * 0.4 + self.ideal_body_weight
          print(f'Adjusted Body Weight: {self.adjusted_body_weight}')
          return self.adjusted_body_weight

     def calc_grubb_equation(self):
          self.grubb_equation = 83.93 * (self.cystatin_c ** -1.676)
          print(f'Grubb Equation: {self.grubb_equation}')
          return self.grubb_equation

     def calc_larsonns_equation(self):
         self.larsson_equation = 77.239 * (self.cystatin_c ** -1.2623)
         print(f'Larssons Equation: {self.larsson_equation}')
         return self.larsson_equation

     def cockcroft_gault(self):
          if self.gender == 'male':
            temp = 140 - self.age




andre = Patient('andre', 'lonardo', 'male', 20, 116, 65, 'african american', 3.2, 0.7, 1.5, 41, 8.0)

andre.print_patient_info()
andre.calc_bmi()
andre.calc_grubb_equation()
andre.calc_larsonns_equation()
andre.calc_ideal_body_weight()
andre.calc_adjusted_body_weight()
