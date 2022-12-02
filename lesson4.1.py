# age = int(input("Enter your age"))
# role = input("Enter your role")
#
# if age >=18:
#     if role == "student" or role == "intern":
#         print("you are allowed")
#         print("you are a student")
#     elif role == "teacher":
#         print("you are allowed")
#         print("you are a teacher")
#     elif role == "guest":
#         print("you are allowed")
#         print("your are a guest")
#     else:
#         print("you are not allowed")
#         print("you are", role)
# else:
#     print("you are not allowed")

# numb1 = int(input("Enter first number="))
# action = input("choose action +,-,/,%,*")
# numb2 = int(input("Enter second number="))
#
#
# if action == "+":
#     print(numb1+numb2)
# elif action == "*":
#     print(numb1*numb2)
# elif action == "/" and numb2 != 0:
#     print(numb1 / numb2)
# elif action == "-":
#     print(numb1-numb2)
# elif action == "%":
#     print(numb1%numb2)
# else:
#     print("вы попытались поделить на 0, по законам математики это невозможно")


# numb = int(input("Enter first number="))
# if numb > 100:
#     print("вы ввели знаение больше ста")
# elif numb % 3 == 0 and numb % 5 > 0:
#     print("fizz")
# elif numb % 5 == 0 and numb % 3 > 0:
#     print("buzz")
# elif numb % 3 == 0 and numb % 5 == 0:
#     print("fizz  buzz")
# else:
#     print(numb)



manager1 = int(input("введите зарплату1="))
manager2 = int(input("введите зарплату2="))
manager3 = int(input("введите зарплату3="))

zarplata = 200
result = 0
result1 = 0
result2 = 0
if manager1 > 1000:
    result = zarplata + (manager1 / 100) * 8
    print(zarplata + (manager1/100)*8)
elif 500 < manager1 <= 1000:
    result = zarplata + (manager1 / 100) * 5
    print(zarplata + (manager1/100)*5)
else:
    result = zarplata + (manager1 / 100) * 3
    print(zarplata + (manager1 / 100) * 3)

if manager2 > 1000:
    result1 = zarplata + (manager2 / 100) * 8
    print(zarplata + (manager2/100)*8)
elif 500 < manager1 <= 1000:
    result1 = zarplata + (manager2 / 100) * 5
    print(zarplata + (manager2/100)*5)
else:
    result1 = zarplata + (manager2 / 100) * 3
    print(zarplata + (manager2 / 100) * 3)

if manager3 > 1000:
    result2 = zarplata + (manager3 / 100) * 8
    print(zarplata + (manager3/100)*8)
elif 500 < manager3 <= 1000:
    result2 = zarplata + (manager3 / 100) * 5
    print(zarplata + (manager3/100)*5)
else:
    result2 = zarplata + (manager3 / 100) * 3
    print(zarplata + (manager3 / 100) * 3)

if manager1 > manager2 and manager1 > manager3:
    print("the best manager is number 1")
    print(result+200)
elif manager2 > manager1 and manager2 > manager3:
    print("the best manager is number 2")
    print(result1 + 200)
elif manager3 > manager1 and manager3 > manager2:
    print("the best manager is number 3")
    print(result2 + 200)
else:
    print("у нас есть несколько победителей так что премии не будет")







