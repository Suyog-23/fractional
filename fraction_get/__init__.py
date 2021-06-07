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
    

