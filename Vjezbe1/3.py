while True:
    try:
        x1 = int(input("Unesite x koordinatu prve tocke: "))
        y1 = int(input("Unesite y koordinatu prve tocke:  "))
        x2 = int(input("Unesite x koordinatu druge tocke:  "))
        y2 = int(input("Unesite y koordinatu druge tocke:  "))
        break
    except NameError:
        print("Molim vas ponovno unesite koordinate: ")   

k = (y2-y1)/(x2-x1)
l = y1-k*x1
if l < 0:
    print("y = {}x{}".format(k, l))
if l > 0:
    print("y = {}x+{}".format(k, l))
