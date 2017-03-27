

def getIntegerComplement(n):
    binary = "{0:b}".format(n).strip()
    complement = ''.join(['0' if i == '1' else '1' for i in binary])
    return int(complement,2)


print getIntegerComplement(5)
print getIntegerComplement(50)
print getIntegerComplement(100)

# 2, 13, 27