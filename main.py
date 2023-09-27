def rectangle_area(width , height):
    if width>0 and height>0:
        Ploshad = width * height
        return Ploshad
print (rectangle_area(width = int(input("Введите 1 сторону ")), height = int(input("Введите 2 сторону "))))

def is_even(number):
    if (number % 2) == 0:
        return True
    else:
        return False
print(is_even(number = int(input("Введите число "))))

def sum_digits(number):
    sum = 0
    if number >= 0:
        while number > 0:
            sum += number % 10
            number //= 10
        return sum
print (sum_digits(number = int(input("Введите число "))))
