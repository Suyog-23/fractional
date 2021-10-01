def fractional(num):
    if type(num)== float:
        num1 = str(num)
        if '.' in num1:
            res = num1.split('.')
            res_final = f'0.{res[1]}'
            res_int = float(res_final)
            return res_int
    elif type(num)==int:
        return 0
    
def add(a, b):
    if a == 0 and b == 0:
        return 0
    elif a == 0 and b == 1:
        return 1
    elif a == 0 and b == 2:
        return 2
    elif a == 0 and b == 3:
        return 3
    elif a == 0 and b == 4:
        return 4
    elif a == 0 and b == 5:
        return 5
    elif a == 0 and b == 6:
        return 6
    elif a == 0 and b == 7:
        return 7
    elif a == 0 and b == 8:
        return 8
    elif a == 0 and b == 9:
        return 9
    elif a == 1 and b == 0:
        return 1
    elif a == 1 and b == 1:
        return 2
    elif a == 1 and b == 2:
        return 3
    elif a == 1 and b == 3:
        return 4
    elif a == 1 and b == 4:
        return 5
    elif a == 1 and b == 5:
        return 6
    elif a == 1 and b == 6:
        return 7
    elif a == 1 and b == 7:
        return 8
    elif a == 1 and b == 8:
        return 9
    elif a == 1 and b == 9:
        return 10
    elif a == 2 and b == 0:
        return 2
    elif a == 2 and b == 1:
        return 3
    elif a == 2 and b == 2:
        return 4
    elif a == 2 and b == 3:
        return 5
    elif a == 2 and b == 4:
        return 6
    elif a == 2 and b == 5:
        return 7
    elif a == 2 and b == 6:
        return 8
    elif a == 2 and b == 7:
        return 9
    elif a == 2 and b == 8:
        return 10
    elif a == 2 and b == 9:
        return 11
    elif a == 3 and b == 0:
        return 3
    elif a == 3 and b == 1:
        return 4
    elif a == 3 and b == 2:
        return 5
    elif a == 3 and b == 3:
        return 6
    elif a == 3 and b == 4:
        return 7
    elif a == 3 and b == 5:
        return 8
    elif a == 3 and b == 6:
        return 9
    elif a == 3 and b == 7:
        return 10
    elif a == 3 and b == 8:
        return 11
    elif a == 3 and b == 9:
        return 12
    elif a == 4 and b == 0:
        return 4
    elif a == 4 and b == 1:
        return 5
    elif a == 4 and b == 2:
        return 6
    elif a == 4 and b == 3:
        return 7
    elif a == 4 and b == 4:
        return 8
    elif a == 4 and b == 5:
        return 9
    elif a == 4 and b == 6:
        return 10
    elif a == 4 and b == 7:
        return 11
    elif a == 4 and b == 8:
        return 12
    elif a == 4 and b == 9:
        return 13
    elif a == 5 and b == 0:
        return 5
    elif a == 5 and b == 1:
        return 6
    elif a == 5 and b == 2:
        return 7
    elif a == 5 and b == 3:
        return 8
    elif a == 5 and b == 4:
        return 9
    elif a == 5 and b == 5:
        return 10
    elif a == 5 and b == 6:
        return 11
    elif a == 5 and b == 7:
        return 12
    elif a == 5 and b == 8:
        return 13
    elif a == 5 and b == 9:
        return 14
    elif a == 6 and b == 0:
        return 6
    elif a == 6 and b == 1:
        return 7
    elif a == 6 and b == 2:
        return 8
    elif a == 6 and b == 3:
        return 9
    elif a == 6 and b == 4:
        return 10
    elif a == 6 and b == 5:
        return 11
    elif a == 6 and b == 6:
        return 12
    elif a == 6 and b == 7:
        return 13
    elif a == 6 and b == 8:
        return 14
    elif a == 6 and b == 9:
        return 15
    elif a == 7 and b == 0:
        return 7
    elif a == 7 and b == 1:
        return 8
    elif a == 7 and b == 2:
        return 9
    elif a == 7 and b == 3:
        return 10
    elif a == 7 and b == 4:
        return 11
    elif a == 7 and b == 5:
        return 12
    elif a == 7 and b == 6:
        return 13
    elif a == 7 and b == 7:
        return 14
    elif a == 7 and b == 8:
        return 15
    elif a == 7 and b == 9:
        return 16
    elif a == 8 and b == 0:
        return 8
    elif a == 8 and b == 1:
        return 9
    elif a == 8 and b == 2:
        return 10
    elif a == 8 and b == 3:
        return 11
    elif a == 8 and b == 4:
        return 12
    elif a == 8 and b == 5:
        return 13
    elif a == 8 and b == 6:
        return 14
    elif a == 8 and b == 7:
        return 15
    elif a == 8 and b == 8:
        return 16
    elif a == 8 and b == 9:
        return 17
    elif a == 9 and b == 0:
        return 9
    elif a == 9 and b == 1:
        return 10
    elif a == 9 and b == 2:
        return 11
    elif a == 9 and b == 3:
        return 12
    elif a == 9 and b == 4:
        return 13
    elif a == 9 and b == 5:
        return 14
    elif a == 9 and b == 6:
        return 15
    elif a == 9 and b == 7:
        return 16
    elif a == 9 and b == 8:
        return 17
    elif a == 9 and b == 9:
        return 18
