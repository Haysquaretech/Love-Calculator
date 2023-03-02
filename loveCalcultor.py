firstName = input("What is your name? ")
secondName = input("What is your spouse name? ")
combine = firstName + secondName
lowerCase = combine.lower()

t = lowerCase.count('t')
r = lowerCase.count('r')
u = lowerCase.count('u')
e = lowerCase.count('e')
true = t + r + u + e

l = lowerCase.count('l')
o = lowerCase.count('o')
v = lowerCase.count('v')
e = lowerCase.count('e')
love = l + o + v + e

score = int(str(true) + str(love))
if score < 10 or score > 90:
    print(f"Your score is {score} and you are great with each other")
elif score >= 40 and score <= 50:
    print(f"Your score is {score} and you are good together")
else:
    print(f"Your love score is {score}")
