def dec2bin(dec):
    resultado = ""
    while dec >= 2:
        resto = dec % 2
        dec = dec // 2
        div = str(resto)
        resultado += div
        if dec == 1:
            resultado += "1"
        else:
            resultado += "0"
            if len(resultado)<8:
                cantidad = 8-len(resultado)
                resultado += "0"*cantidad
                total = resultado[::-1]
                return total

def dec2oct(dec):
    resultado = ""
    while dec >= 8:
        resto = dec % 8
        dec = dec // 8
        div = str(resto)
        resultado += div
        resultado += str(dec)
        octal = resultado[::-1]
        return octal

def dec2hex(dec):
    resultado = ""
    hex_dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    while dec >= 16:
        resto = dec % 16
        dec = dec // 16
    
    if resto in hex_dict:
        div = hex_dict[resto]
    else:
        div = str(resto)
    resultado += div
    if dec in hex_dict:
        resultado += hex_dict[dec]
    else:
        resultado += str(dec)
        hexadecimal = resultado[::-1]
    return hexadecimal

