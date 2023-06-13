def oct2bin(oct):
    bin = ""
    for digito in oct:
        # cada dígito octal a binario
        digito_bin = bin(int(digito))[2:]
        # cada dígito binario tenga 3 bits
        digito_bin = digito_bin.zfill(3)
        bin += digito_bin
    return bin

def hex2bin(hex):
    bin = ""
    for digito in hex:
        # cada dígito hexa a binario
        digito_bin = bin(int(digito, 16))[2:]
        # cada dígito binario tenga 4 bits
        digito_bin = digito_bin.zfill(4)
        bin += digito_bin
    return bin

