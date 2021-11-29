import math
import time


def decorator(function):
    def wrapper(*args):
        start_time = time.time()
        function()
        print("--- %s seconds ---" % (time.time() - start_time))

    return wrapper


@decorator
def landarea(*args):
    ac = 0.000022957
    area = float(landheight) * float(landwidth) * float(ac)
    print("Площадь участка земли в акрах: " + str(area))


@decorator
def freefall(*args):
    g = 9.8
    v = 0
    u = math.sqrt(math.pow(v, 2) + 2 * float(g) * float(h))
    print("Скорость объекта с высоты: " + str(h) + "м при ускорении " + str(g) + "м/с^2 равна: " + str(u))


landheight = input("Введите длину участка в футах: ")
landwidth = input("Введите ширину участка в футах: ")
landarea(landheight, landwidth)


h = input("Введите высоту: ")
freefall(h)