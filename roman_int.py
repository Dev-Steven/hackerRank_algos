
def romanToInt(s):
    dict = {
        'I': 1,
        'IV': 4,
        'IX': 9,
        'V': 5,
        'X': 10,
        'XL': 40,
        'XC': 90,
        'L': 50,
        'C': 100,
        'CD': 400,
        'CM': 900,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    i = 0
    
    while i < len(s):
        if i+1<len(s) and s[i:i+2] in dict:
            total += dict[s[i:i+2]]
            i+=2
        else:
            total += dict[s[i]]
            i+=1
    return total

        