
def jedn_pravca1( x1 = int(input(" ")),  y1 = int(input(" ")),  x2 = int(input(" ")),  y2 = int(input(" "))):

    k = (y2-y1)/(x2-x1)
    l = y1-k*x1
    if l < 0:
        print("y = {}x{}".format(k, l))
    if l > 0:
        print("y = {}x+{}".format(k, l))
    return k,l

jedn_pravca1()




