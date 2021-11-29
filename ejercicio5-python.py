def impuestos():

    renta = float(input('Ingrese su renta $: '))

    if renta < 0:
        print('Valor no válido')
        return



    if renta <10000:
        print("Impuesto:  {0:2f}".float(renta * 0.05))
    elif renta < 20000:
        print("Impuesto:  {0:2f}".float(renta * 0.15))
    elif renta <35000:
        print("Impuesto:  {0:2f}".float(renta * 0.20))
    elif renta <= 60000:
        print("Impuesto:  {0:2f}".float(renta * 0.30))
    else:
        print("Impuesto:  {0:2f}".float(renta * 0.45))



impuestos()