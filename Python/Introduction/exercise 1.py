#Question 1

my_string = 'Hello Python!'
rev_string = my_string[-2::-1]
print(rev_string, end = "")
print(my_string[-1])


# Question 2

my_string = "Information"
print(my_string[2::2])


#Question 3

# string.format is used to import a given variable in a print statement given that the variable is defined
# in the print statement only, whereas f-string is a new interpolation technique in python which can be used
# to import any variable in the given .py file or code. f-string is an upgraded technique of string.format
# which is faster and simpler to use.

name = "Sanyam"
age = 22

print("Name : {name} \nAge : {age}".format(name = "Aayush",age = "21"))
print(f"Name : {name} \nAge : {age}")


#Question 4

# No, the dictionaries can not be sorted as they are a kind pf mapping and mapping are orderless.
# However, the keys or the values of the dictionary can be sorted if extracted in the form of a list,
# and then can be sorted.


# Question 5

d={'simple_key':'hello'}

print(d['simple_key'])



d = {'k1':{'k2':'hello'}}

print(d['k1']['k2'])



d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d['k1'][0]['nest_key'][1][0])



d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print(d['k1'][2]['k2'][1]['tough'][2][0])