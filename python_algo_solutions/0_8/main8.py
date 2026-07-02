
#integer to roman numeral converter
def inttostr(num):
    #max num = 3999 and min = 0
    thousands = int((num // 1000))
    hundreds = int(((num % 1000) // 100))
    tens = int(((num % 100) // 10))
    ones = num % 10

    print(thousands, hundreds, tens, ones)

    th = ""
    if thousands == 0:
        pass
    elif thousands > 0 and thousands <= 3:
        th = "M" * thousands

    h = ""
    if hundreds == 0:
        pass
    elif hundreds > 0 and hundreds <= 3:
        h = "C" * hundreds
    elif hundreds > 3 and hundreds < 5:
        h = "CD"
    elif hundreds == 5:
        h = "D"
    elif hundreds > 5 and hundreds <= 8:
        h = "D"+str("C"*(hundreds-5))
    elif hundreds > 8 and hundreds < 10:
        h = str("C"*(10-hundreds)) + "M"
    
    t = ""
    if tens == 0:
        pass
    elif tens > 0 and tens <= 3:
        t = "X" * tens
    elif tens > 3 and tens < 5:
        t = "XL"
    elif tens == 5:
        t = "L"
    elif tens > 5 and tens <= 8:
        t = "L"+str("X"*(tens-5))
    elif tens > 8 and tens < 10:
        t = str("X"*(10-tens)) + "C"

    o = ""
    if ones == 0:
        pass
    elif ones > 0 and ones <= 3:
        o = "I" * ones
    elif ones > 3 and ones < 5:
        o = "IV"
    elif ones == 5:
        o = "V"
    elif ones > 5 and ones <= 8:
        o = "V"+str("I"*(ones-5))
    elif ones > 8 and ones < 10:
        o = str("I"*(10-ones)) + "X"

    res = th + str(h) +str(t) + str(o)

    return res

print(inttostr(3749))  # MMMDCCXLIX MMMDCCXLIX