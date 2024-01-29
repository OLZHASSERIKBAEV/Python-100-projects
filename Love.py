print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
c = name1 + name2
d = c.lower()
t=d.count('t')
r=d.count('r')
u=d.count('u')
e=d.count('e')
l=d.count('l')
o=d.count('o')
v=d.count('v')
e=d.count('e')
q=t+r+u+e
m=l+o+v+e
final= str(q)+str(m)
p= int(final)

if p <10 or p > 90:
    print(f"Your score is {p}, you go together like coke and mentos.")
elif p >=40 and p <=50 :
    print(f"Your score is {p}, you are alright together.")
else:
    print(f"Your score is {p}.")