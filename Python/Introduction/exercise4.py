#Question 1

def fibonacci(n):
        a=0
        b=1
        c=0
        while(a<=n):
                c=a+b
                yield a
                b=a
                a=c
fib_values=[]
for i in fibonacci(int(input("Enter a number : "))):
        fib_values.append(i)
print(fib_values)


#Question 2

def do_twice(func):
        def fun(name):
                n = int(input("Enter the number of times you want to run the code : "))
                for i in range(0,n):
                        func(name)
        return fun

@do_twice
def printInfo(name):
        print(f"You are running {name}'s code")

do_twice(printInfo('Sanyam'))


# Question 3

from collections import Counter

word_list = []
with open("sample.txt", "w+") as myFile:
        myFile.write("The Joker is a supervillain created by Bill Finger, " +
                     "Bob Kane, and Jerry Robinson who first appeared in the" +
                     " debut issue of the comic book Batman (April 25, 1940), " +
                     "published by DC Comics. Credit for the Joker's creation " +
                     "is disputed; Kane and Robinson claimed responsibility " +
                     "for the Joker's design, while acknowledging Finger's " +
                     "writing contribution. Although the Joker was planned " +
                     "to be killed off during his initial appearance, " +
                     "he was spared by editorial intervention, allowing " +
                     "the character to endure as the archenemy of the superhero Batman.")
        myFile.seek(0)
        for line in myFile:
                for word in line.split():
                        word_list.append(word)
word_list_counter = Counter(word_list)
print(word_list_counter.most_common())



# Question 4

def prime_number_generator(choice):
        n=2
        while(choice == "y"):
                flag = True
                for i in range(2,n):
                        if(n%i==0):
                                flag = False
                                break
                if(flag == True):
                    yield n
                n=n+1
choice = "y"
output = prime_number_generator(choice)
while(1):
        choice = input("Enter your choice (y/n) :")
        if(choice == "y"):
                print(next(output))
        elif(choice == "n"):
                print("Thank You.")
                break
        else:
                print("Wrong Choice. \nEither enter 'y' or 'n'.")


# Question 5

def convert(digit, unit1, unit2):
        unit = {'km' :1000, 'm': 1, 'cm': 0.01, 'mm' : 0.001}
        return digit * (unit[unit1] / unit[unit2])

print("Use \'km\' for kilometers. \nUse \'m\' for meters.\nUse \'cm\' for Centimeters.\nUse \'mm\' for Millimeters.")

unit1 = str(input("Enter the unit you want to use : "))
unit2 = str(input("Enter the unit you want to convert to : "))

digit = float(input("Enter the value to convert : "))

output = convert(digit, unit1, unit2)
print(output)



# Question 6

import re

pattern = str(input("Enter a string here : "))
reg = str(input("Enter the regular expression : "))

r = re.findall(reg, pattern)
print(r)