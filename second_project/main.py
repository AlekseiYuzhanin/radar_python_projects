def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

n = int(input("Введите номер простого числа: "))

count = 0  
number = 2  

while count < n:
    if is_prime(number):
        count += 1
        if count == n:
            print(f"{n}-е простое число: {number}")
            break
    number += 1