def c_to_f (c):
    f = (c * 9/5) + 32
    return f

def f_to_c (f):
    c = (f-32)*5/9
    return c

print("=====temperature conversion=====")
print("1.Celcius to Fahrenheit")
print("2.Fahrenheit to Celcius")

choice= input("Select the desired conversion (type 1 or 2):")

if choice == "1":
    initial_temperature=float(input("Enter the temperature in Celsius:"))
    final_temperature=c_to_f(initial_temperature)
    print(final_temperature)

if choice == "2":
    initial_temperature=float(input("Enter the temperature in fehrenheit:"))
    final_temperature=f_to_c(initial_temperature)
    print(final_temperature)

else:
    ("Enter numbers, not letters!")