name = input("Как тебя зовут? ")
age = input("Сколько тебе лет? ")
has_laptop = input("У тебя есть ноутбук? (да/нет): ")

age = int(age)

if age >= 18:
    if has_laptop == "да":
        print(name, "Добро пожаловать на биржу!")
    else:
        print("Купи ноутбук, без него не сможешь работать.")
else:
    print("Приходи когда исполниться 18.")