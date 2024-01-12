#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add ,sub ,mul ,div
    a = 10
    b = 5
    R = add(a, b)
    S = sub(a, b)
    P = mul(a, b)
    D = div(a, b)
    print("{} + {} = {}".format(a ,b ,R))
    print("{} - {} = {}".format(a ,b ,S))
    print("{} * {} = {}".format(a ,b ,P))
    print("{} / {} = {}".format(a ,b ,D))
