# Напишите программу, где я ввожу логин и пароль. И если данные были введены верно,
# то мы выводим Authentication completed, иначе Invalid login or password.
# (Логин должен быть user, пароль - qwerty) 
log=input("Login: ")
pswd=input("Password: ")
if log=="user" and pswd=="qwerty":
    print("Authentication completed")
else:
    print("Invalid login or password")


# Напишите программу обмена валют, где я ввожу сумму в тенге и выбираю на какую
# валюту хочу перевести. (Курс USD – 420, EUR – 510, RUB - 5.8).
am=int(input("Insert amount in KZT: "))
print("Choose currency: \n[1] USD\n[2] EUR\n[3] RUB")
cur=int(input())
if cur==1:
    print(am/420, "USD")
elif cur==2:
    print(am/510, "EUR")
elif cur==3:
    print(am/5.8, "RUB")
else:
    print("incorrect input!")