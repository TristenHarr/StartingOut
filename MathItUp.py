from mpmath import *
mp.dps = 100
from itertools import cycle
def n(x):
    return mp.mpf("{}".format(x))

def polyspand(x):
    my_stuff = []
    valuecount = -1
    my_letters = cycle("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for i in range(x+1):
        value = next(my_letters)
        if value == "A":
            valuecount += 1
        if valuecount > 0:
            my_stuff.append((value + ("'"*valuecount))+"^")
        else:
            my_stuff.append((value+"^"))
    return ["".join(my_stuff), x+1]

def polyfill(my_list):
    my_string = ""
    for i in range(len(my_list)):
        my_string += "{}X^{}+".format(my_list[i], len(my_list)-(i+1))
    return my_string

def polyoperate(values, x=0):
    values = polyfill(values)
    myoperations = values.split("+")
    myoperations.pop()
    for i in range(len(myoperations)):
        myoperations[i] = "(mp.mpf("+myoperations[i].replace("X", ")*mp.power({}".format(str(x))).replace("^",",")+"))"
    answer = "+".join(myoperations)
    exec("globals()['THEOPERATION'] = {}".format(answer))
    return THEOPERATION
print(polyoperate([3,4,0,5],5))




def findzeros(values):
    zero = False
    x = mp.mpf("0")
    x2 = mp.mpf("0")
    previous = 0
    previous2 = 0
    iters = mp.mpf("1/1000")
    while not zero:
        first = previous
        second2 = previous2
        x -= iters
        x2 += iters
        # print(x,x2)
        test = polyoperate(values, x)
        test2 = polyoperate(values, x2)
        previous = (abs(test))
        previous2 = (abs(test2))
        print("I GIVE UP FOR NOW")
        if first < previous:
            ONIT = True
            print(first, previous)
        elif ONIT:
            x -= iters
            iters = mp.mpf(iters/10)
        if second2 < previous2:
            ONIT2 = True
            print(second2, previous2)
        elif ONIT2:
            x2 += iters
            iters = mp.mpf(iters/10)
        # if (test or test2) == 0:
        #     print(test)
        #     zero = True


findzeros([3,5,0])
def factorlist(x):
    my_factors = []
    for i in range(1,int(mp.sqrt(x))+1):
        if x%i == 0:
            my_factors.append(x//i)
            my_factors.append(i)
    return list(set(my_factors))


def findZeros(values):
    my_lista = factorlist(values[-1])
    my_listb = factorlist(values[0])
    my_testcases = []
    for item in my_lista:
        for item2 in my_listb:
            my_testcases.append([item,item2])
    for item in my_testcases:
        value = mp.mpf(item[0])/mp.mpf(item[1])
        equate = polyoperate(values, value)
        print(equate)
        equate = polyoperate(values, -value)
        print(equate)
