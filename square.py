def area(a):
    if a < 0:
        raise ValueError("Сторона квадрата не может быть отрицательной")
    return a * a

def perimeter(a):
    if a < 0:
        raise ValueError("Сторона квадрата не может быть отрицательной")
    return 4 * a
