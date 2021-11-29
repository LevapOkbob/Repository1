import math
import time


def decorator(function):
    def wrapper():
        start_time = time.time()
        function()
        print("--- %s seconds ---" % (time.time() - start_time))

    return wrapper


@decorator
def landarea():
    ac = 0.000022957
    landheight = input("Введите длину участка в футах: ")
    landwidth = input("Введите ширину участка в футах: ")
    area = float(landheight) * float(landwidth) * float(ac)
    print("Площадь участка земли в акрах: " + str(area))


@decorator
def freefall():
    g = 9.8
    v = 0
    h = input("Введите высоту: ")
    u = math.sqrt(math.pow(v, 2) + 2 * float(g) * float(h))
    print("Скорость объекта с высоты: " + str(h) + "м при ускорении " + str(g) + "м/с^2 равна: " + str(u))


decorator(freefall())