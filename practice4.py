weight = float(input("please enter your weight (KG): "))
height = float(input("please enter your height (M): "))

height = height / 100
bmi = weight / (height*height )
print(bmi)