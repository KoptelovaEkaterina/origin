def create_statistic_function (alphabet): # функция, которая принимает буквенную строчку 
    def statistic_function(s):        
        d = {alpha : 0 for alpha in alphabet} # изначально alpha встречается 0 раз
        for alpha in s:
            if alpha in d:
                d[alpha]+=1
        ln = len(s)    
        for k in sorted(d):
            print(f"{k}: {d[k]}")
    return statistic_function 