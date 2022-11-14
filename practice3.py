#name = (input("pls enter your name: "))
#family = (input("pls enter your family: "))

score1 = float(input(" enter your score1: "))
score2 = float(input(" enter your score2: "))
score3 = float(input(" enter your score3: "))

average = (score1 + score2 + score3) / 3
print(average)

if average >= 17:
    print("great")

elif average <= 17 and average >= 12:
    print("normal")

elif 12 >= average:
    print("fail")   