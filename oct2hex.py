def oct2hex(oct):
    dec = 0
    potencia = 0

    # oct a dec
    for digito in reversed(oct):
        dec += int(digito) * (8 ** potencia)
        potencia += 1

    # dec a hex
    hex = hex(dec)[2:]

    return hex