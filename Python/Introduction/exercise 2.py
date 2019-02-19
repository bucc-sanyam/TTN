# Question 1
print("Question 1 : \n")
for i in range(7):
    if(i==3 or i==6):
        continue
    print(str(i)+", ",end=" ")
print("\b\b\b \n\n")


# Question 2

print("Question 2 : \n")
m=int(input("Enter m :"))
n=int(input("Enter n :"))
arr=[[(i*j) for j in range(n)]for i in range(m)]
print(arr)
print("\n")


# Question 3

print("Question 3 : \n")
initial_list=[1,2,3,4,5,6,7,8,9,10]
my_list=list(filter(lambda x: (x%2==0), initial_list))
print(my_list)
print("\n")


# # Question 4

print("Question 4 : \n")
my_list=list(map(lambda x: x**2, initial_list))
print(my_list)
print("\n")


# Question 5

print("Question 5 : \n")
def disp(*args):
    for i in args:
        print("name "+i['name'])
        print("age "+str(i['age']))
disp({'name': 'abhi', 'age': 22},{'name': 'vikas', 'age': 21})