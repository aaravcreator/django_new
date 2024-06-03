print("THIS IS PYTHON")

my_data = "2.03"

amount = float(my_data)
print(type(amount))

print(my_data)
print(type(my_data))


'''
data = input("WHAT IS YOUR NAME? ") 
print(data)
'''

'''
condition = False
age = int(input("Enter your age: "))
if condition == True or age >= 18:
    print("THIS IS TRUE")
    print("hhhe")
elif condition == True or age >= 12:
    print("NEARLY TRUE")
else:
    print("THIS IS FALSE")


print("hhhe outer")
'''


mero_list = ['a','e','i','o','u']
print(mero_list[0])


my_tuple = ('apple','banana','cat')
print(my_tuple)
# a = my_tuple[0]
# b = my_tuple[1]
# c = my_tuple[2]
(a,b,c) = my_tuple
print(a,b,c)

mero_tuple = ('apple','banana','cat','dog','egg','fish','gun')
(a,b,*c) = mero_tuple
print(a,b,c)

my_set = {"manago","papaya"}
my_set.add("guava")
print(my_set)
my_set.remove("manago")
print(my_set)
next_set = {
    'apple','orange'
}
my_set.update(next_set)
print(my_set)


name = "HARI"
gender = "MALE"
job = "DATA ENGINEER"
print("Hello ",name," you are ",gender," and you are ",job)


message = f"Hello {name} you are {gender} and you are {job}"
print(message)

print("Hello {} you are {} and you are {}".format(name,gender,job))


for i in range(1,5):
    print(i)
    print("INSIDE FOR")

fruit_list = ['apple','banana','cat','dog','egg','fish','gun']



for i in fruit_list:
    print(i)

print("OUTSIDE")


for i, value in enumerate(fruit_list,1):
    print(i,value)


def print_name(*a,fname="N/A",lname):
    print(a[0])
    return f"FIRST NAME :{fname}",f" LAST NAME :{lname}"
    # print(f"PERSON NAME IS {fname} and last name is {lname}")

first_name , lastname = print_name(1,2,3,lname="SHARMA")
print("FROM ",first_name,lastname)



cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=lambda item: item['year'],reverse=True)
print(cars)


items  = ['apple','banana','cat','apple','egg','fish','egg','egg']
items_dict = {}
for item in items:
    if item in items_dict:
        items_dict[item] += 1
    else:
        items_dict[item] = 1
    print(items_dict)

unique_items = []
for key,value in items_dict.items():
    print(key,value)
    if value == 1:
        unique_items.append(key)
print(unique_items)

try:
    result = 3/0
    print(result)
except ZeroDivisionError:
    print("cant divide with zero")




