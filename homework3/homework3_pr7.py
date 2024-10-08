number = int(input("Введите десятичное число: "))
string=""
while number > 0:
    string+=str(number%9)
    number//=9
print("В девятиричной системе счисления: ",string[::-1])
