import math

class Person():
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

    def calculate_bmi(self):
         self.bmi = (self.weight / (self.height * 0.0254) ** 2)
         print(f'BMI: {self.bmi}')
         return self.bmi

    def glomerular_filtration_rate(self):
         self.grubb_equation = 83.93 * (self.cystatin_c ** -1.676)
         self.larsson_equation = 77.239 * (self.cystatin_c ** -1.2623)
         print(f'Grubb Equation: {self.grubb_equation}')
         print(f'Larssons Equation: {self.larsson_equation}')

andre = Person('andre', 'lonardo', 'male', 43, 116, 65, 'african american', 3.2, 1.7, 1.5, 41, 4.0)

andre.calculate_bmi()
andre.glomerular_filtration_rate()