### Задания по ООП


**1. Кофемашина**

Допишите класс CoffeeMachine так, чтобы код ниже заработал.


```python
class CoffeeMachine:
    milk_size = 10
    water_size = 10
    coffee_size = 10
    
    def __init__(self):
        self.milk = 0
        self.coffee = 0
        self.water = 0
    # makeCup -> bool, addWater, addMilk, addCoffee, hasMilk -> bool, hasWater -> bool, hasCoffee -> bool


    
machine = CoffeeMachine()

while True:
    
    print("status:")
    if machine.hasMilk():
        print("milk - OK")
        
    if machine.hasWater():
        print("water - OK")
        
    if machine.hasCoffee():
        print("coffee - OK")
        
    print("")
    
    print("1 - refill water")
    print("2 - refill coffee")
    print("3 - refill milk")
    print("4 - make cup")
    
    try:
        command = int(input())
        
        if command < 1 or command > 4:
            raise Exception()
        
        if command == 1:
            machine.addWater()
        if command == 2:
            machine.addCoffee()
        if command == 3:
            machine.addMilk()
        if command == 4:
            if machine.makeCup():
                print("here is your cup...")
            else:
                print("Insufficient supplies...")
        
    except:
        print("Invalid command...")
        
```

**2. Воды слонам!**


Опишите класс **"кулер"**, который обладает следующими свойствами: 
* количество воды;
* объем бутылки.

Также добавьте следующие методы:
* налить 200мл воды.
* заменить бутылку.


**3. Страховые манипуляции.**


* Создайте класс `InsurancePolicy`, конструктор которого принимает один аргумент - стоимость застрахованного объекта.
* Создайте класс `VehicleInsurance`, который наследуется от первого класса и определите в нем метод класса get_rate, который возвращает 0.1% от стоимости машины.
* Создайте класс `HomeInsurance`, который наследуется от первого класса и определите в нем метод класса `get_rate`, который возвращает 0.005% от стоимости дома.
* Создайте экземпляр второго и третьего класса и для каждого вызовите `get_rate()`.

**4. Стремление к порядку.**

* Напишите класс `SortedList`, который наследуется от встроенного класса `list`.
* Переопределите метод append - ваш класс должен сначала делать `.append()`, но после добавления каждого элемента сортировать список. Чтобы использовать методы родительского класса, можно использовать `super().`
* Дополните конструктор вашего класса, чтобы он сортировал список, который в него приходит.

**5. Национальная сборная.**

* Создайте класс `Team`, конструктор должен брать два аргумента sport (в каком виде спорта выступает команда) и `players` (список имен игроков).
* Переопределите функцию \_\_len\_\_, чтобы при вызове от экземпляра класса Team она возвращала количество игроков в команде.
* Переопределите функцию \_\_contains\_\_, чтобы конструкция \_\_\_ in {экземпляр Team} показывала наличие игрока в команде.
* Переопределите строковое представление вашего класса. Строка должна содержать вид спорта, в котором выступает команда.
