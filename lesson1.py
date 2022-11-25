# int (integer)
# str (string)
# float (100.3;14.5)

apples = 5  # int
price_per_apple = 17  # int
tax = 1.18  # float

result = (apples * price_per_apple)  # 85, скобки  не  несут  значения
fin_result = (tax * result)  # 100.3

char = '@'  # char
currency = "$"  # str
text = "Total price:"

print(text, result, currency)  # вывод результата
print(text, "with tax", fin_result, currency)  # вывод результата с налогом

numb1 = int(input("Enter a first number ="))  # First number
numb2 = int(input("Enter a second number ="))  # Second number

print("_____________________________")  # CTLR+D
print("_____________________________")
print("_____________________________")
print(numb1+numb2, numb1-numb2, numb1*numb2, numb1/numb2, numb1**2, numb1//numb2)

print(numb1, "+", numb2, "=", numb1+numb2)
print(numb1, "*", numb2, "=", numb1*numb2)
print(numb1, "-", numb2, "=", numb1-numb2)
print(numb1, "//", numb2, "=", numb1//numb2)
print(numb1, "/", numb2, "=", numb1/numb2)
print(numb1, "**2", "=", numb1**2)

