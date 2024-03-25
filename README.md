# goit-algo-hw-10

## Завдання 1

Після використання бібліотеки pulp ми отримали статус задачі Optimal. Це означає, що у нас існують оптимальні рішення цієї задачі. Результати розрахунків наведені в таблиці нижче. Було визначено розмір ресурсів потрібних для максимізації загальної кількості вироблених продуктів ("Лимонад" - 30 та "Фруктовий сік" - 20), дотримуючись заданих обмежень на ресурси. 

```
Статус роботи: Optimal
Лимонаду потрібно виробити: 30.0
Фруктового соку потрібно виробити: 20.0
Загальна кількість продуктів: 50.0
```

## Завдання 2

Метод Монте-Карло є статистичним методом, і його точність залежить від кількості випадкових точок, які використовуються для обчислення. У цьому випадку, результат методу Монте-Карло є досить близьким до аналітичного розрахунку, що свідчить про його ефективність для обчислення інтегралів. Як бачимо з результатів дослідження, точність значно зростає при збільщенні кількості експериментів.

```
Numeric integral:                 2.6666666666666665
Monte Carlo integral (100):       2.64
Monte Carlo integral (1000):      2.728
Monte Carlo integral (10000):     2.6176
Monte Carlo integral (100000):    2.65856
Monte Carlo integral (1000000):   2.663704
Monte Carlo integral (10000000):  2.6648328
```

Обчислення значення інтегралу функції за допомогою методу Монте-Карло дає приблизне значення 2.6648328 для 10000000 елементів. Для порівняння, аналітичний розрахунок інтегралу або результат виконання функції quad надає точне значення 2.6666666666666665