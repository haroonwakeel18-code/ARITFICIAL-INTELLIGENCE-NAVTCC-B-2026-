def calculate_bmi(weight_in_kg, height_in_m):
    return weight_in_kg / (height_in_m * height_in_m)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"