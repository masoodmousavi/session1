import math





print("")
print ("welcome to my calculator <3")

print("------------")
print("+")
print("-")
print("*")
print("/")
print("sin")
print("cos")
print("tan")
print("cot")
print("factorial")
print("sqrt")
print("------------")
operator = input("please choise your operator:")

if operator == "+" or operator == "-" or operator == "*" or operator == "/":
    a = float(input("pls enter first nubmer:"))
    b = float(input("pls enter second number:"))

else:
     a = float(input("pls enter your nubmer:"))


if operator == "-" or operator == "menha" or operator == "minus" or operator == "منها":
    print(a-b)

elif operator == "+" or operator ==  "jam" or operator ==  "sum" or operator ==  "جمع":
    print(a+b)

elif operator == "*" or operator ==  "zarb" or operator ==  "mul" or operator ==  "ضرب":
    print(a*b)

elif operator == "/" or operator ==  "taqsim" or operator ==  "taghsim" or operator ==  "div" or operator ==  "تقسیم" :
    if b == 0:
        print("cannot divide by zero")
    else:
        print(a/b)    

elif operator == "cos" or operator == "cosinus" or operator == "کسینوس":
    a * 0.0174532925
    print(math.cos(a))

elif operator == "sin"or operator == "sinus" or operator == "سینوس":  
    a * 0.0174532925
    print(math.sin(a))

elif operator == "tan"or operator == "tangente" or operator == "تانژانت":   
    a * 0.0174532925
    print(math.tan(a))

elif operator == "cot"or operator == "cotgente" or operator == "کتانژانت":   
    a * 0.0174532925
    print(1 / math.tan(a))

elif operator == "sqrt" or operator == "square root" or operator == "ریشه دوم":
    print(math.sqrt(a))    