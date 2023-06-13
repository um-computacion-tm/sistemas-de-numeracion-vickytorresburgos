def bin2dec(bin):
    bin = str(bin)
    dec = 0
    potencia = 0
    for i in range(len(bin)-1,-1,-1):
        if bin[i] == "1":
            dec += 2**potencia
        potencia += 1
    dec = str(dec)
    return dec

def oct2dec (oct):
    oct = str(oct)
    dec = 0
    potencia = 0
    for i in range(len(oct)-1,-1,-1):
        dec += int(oct[i]) * 8**potencia
        potencia += 1
    dec = str(dec)
    return dec

def hex2dec(hexadecimal):
    dec = 0
    potencia = 0

    for digito in reversed(hexadecimal):
        if digito.isdigit():
            dec += int(digito) * (16 ** potencia)
        else:
            dec += (ord(digito.upper()) - ord('A') + 10) * (16 ** potencia)
        potencia += 1
    return dec