from arithmetic import add, subtract, multiply, divide
from bmi import calculate_bmi, bmi_category
from temperature import c_to_f, f_to_c
from length import meters_to_km, km_to_meters, meters_to_feet, feet_to_meters

def arithmetic_menu():
    while True:
        print("\n--- Arithmetic Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "5":
            break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            if b == 0:
                print("Cannot divide by zero.")
            else:
                print("Result:", divide(a, b))
        else:
            print("Invalid option.")

def bmi_menu():
    print("\n--- BMI Calculator ---")
    weight_in_kg = float(input("Enter weight in kg: "))
    height_in_feet = float(input("Enter height in feet: "))
    height_in_m=height_in_feet*0.3048
    bmi = calculate_bmi(weight_in_kg, height_in_m)
    print("Your BMI:", bmi)
    print("Category:", bmi_category(bmi))

def temperature_menu():
    while True:
        print("\n--- Temperature Converter ---")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            c = float(input("Enter °C: "))
            print("Result:", c_to_f(c), "°F")
        elif choice == "2":
            f = float(input("Enter °F: "))
            print("Result:", f_to_c(f), "°C")
        elif choice == "3":
            break
        else:
            print("Invalid option.")

def length_menu():
    while True:
        print("\n--- Length Converter ---")
        print("1. Meters to KM")
        print("2. KM to Meters")
        print("3. Meters to Feet")
        print("4. Feet to Meters")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            m = float(input("Enter meters: "))
            print("Result:", meters_to_km(m), "km")
        elif choice == "2":
            km = float(input("Enter km: "))
            print("Result:", km_to_meters(km), "m")
        elif choice == "3":
            m = float(input("Enter meters: "))
            print("Result:", meters_to_feet(m), "ft")
        elif choice == "4":
            ft = float(input("Enter feet: "))
            print("Result:", feet_to_meters(ft), "m")
        elif choice == "5":
            break
        else:
            print("Invalid option.")

def main():
    while True:
        print("\n===== Smart Calculator =====")
        print("1. Arithmetic")
        print("2. BMI Calculator")
        print("3. Temperature Converter")
        print("4. Length Converter")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            arithmetic_menu()
        elif choice == "2":
            bmi_menu()
        elif choice == "3":
            temperature_menu()
        elif choice == "4":
            length_menu()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

main()