name=input("What's your name?: ")
age=input("How old are you?: ")
fav_num=input("What's your favourite number?: ")

age=int(age)
fav_num=int(fav_num)

ten_age=age+10
square_num=fav_num**2

if fav_num%2==0:
    value="even"
else:
    value="odd"

print(f"Hi {name}! in 10 years you will be {ten_age}. Your favourite number squared is {square_num}, and it is {value}.")

#Reflection question--> Because python accepts and understands the value in input as text.