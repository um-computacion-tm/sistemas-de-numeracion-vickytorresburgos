def bin2oct(bin):
    dec = 0
    potencia = 0

    # bin a dec
    for bit in reversed(bin):
        dec += int(bit) * (2 ** potencia)
        potencia += 1

    # dec a octal
    oct = ""
    while dec > 0:
        resto = dec % 8
        oct = str(resto) + oct
        dec = dec // 8

    return oct

def bin2hex(bin):
    dec = 0
    potencia = 0

    # Convertir el número bin a dec
    for bit in reversed(bin):
        dec += int(bit) * (2 ** potencia)
        potencia += 1

    # Convertir el dec a hexadec
    hex = ""
    while dec > 0:
        resto = dec % 16
        hex = hex(resto)[2:] + hex
        dec = dec // 16

    return hex

