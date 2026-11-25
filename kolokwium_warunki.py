import math
# # zadanie 1
# number = eval(input("podaj liczbe zmiennoprzecinkową: "))
#
# print("abs tej liczby to: ", abs(number))
#
# # zadanie 2
# number_f = eval(input("podaj liczbe zmiennoprzecinkową: "))
# number_s = eval(input("podaj liczbe zmiennoprzecinkową: "))
#
# if number_s != 0:
#     print(number_f / number_s)
# else:
#     print("nie mozna dzielic prez zero")
#
# #zadanie 3
# number_1 = eval(input("podaj 1 liczbe zmiennoprzecinkową: "))
# number_2 = eval(input("podaj 2 liczbe zmiennoprzecinkową: "))
# number_3 = eval(input("podaj 3 liczbe zmiennoprzecinkową: "))
#
#
# if number_1 > number_2 > number_3:
#     print("największa to: ", number_1, "najmniejsza to: ", number_3)
# elif number_1 > number_3 > number_2:
#     print("największa to: ", number_1, "najmniejsza to: ", number_2)
# elif number_2 > number_1 > number_3:
#     print("największa to: ", number_2, "najmniejsza to: ", number_3)
# elif number_2 > number_3 > number_1:
#     print("największa to: ", number_2, "najmniejsza to: ", number_1)
# elif number_3 > number_1 > number_2:
#     print("największa to: ", number_3, "najmniejsza to: ", number_2)
# elif number_3 > number_2 > number_1:
#     print("największa to: ", number_3, "najmniejsza to: ", number_1)


#zadanie 4
boki_trojkata = []

boki_trojkata.append(eval(input("podaj 1 bok trójkąta")))
boki_trojkata.append(eval(input("podaj 2 bok trójkąta")))
boki_trojkata.append(eval(input("podaj 3 bok trójkąta")))

boki_trojkata.sort()
print(boki_trojkata)

if boki_trojkata[0] + boki_trojkata[1] > boki_trojkata[2]:
    obwod = sum(boki_trojkata)
    print("obwód trójkata to: ", obwod )

    p = obwod/2

    pole = math.sqrt(p*(p - boki_trojkata[0]) * (p - boki_trojkata[1]) * (p - boki_trojkata[2]))
    print(pole)
else:
    print("To nie są boki trojkąta koncze program!!!")
