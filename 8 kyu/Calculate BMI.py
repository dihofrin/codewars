"""Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"

"""


def bmi(weight, height):
    s = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(s > 18.5) + (s > 25) + (s > 30) ]
