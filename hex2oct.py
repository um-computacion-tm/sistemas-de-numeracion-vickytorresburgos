def hex2oct(hex):
    dec = 0
    potencia = 0

    # hex a dec
    for digito in reversed(hex):
        if digito.isdigit():
            dec += int(digito) * (16 ** potencia)
        else:
            dec += (ord(digito.upper()) - ord('A') + 10) * (16 ** potencia)
        potencia += 1

    # dec a oct
    oct = ""
    while dec > 0:
        resto = dec % 8
        oct = str(resto) + oct
        dec = dec // 8

    return oct

