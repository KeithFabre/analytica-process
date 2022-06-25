from datetime import date

today = date.today()
def ageCalc(birthday=None, date=today):   
    
     # to extract from str
    str_birth = str(birthday)
    str_date = str(date)

    # slicing to get fraction and turing to int to calc
    y = int(str_birth[0:4])
    m = int(str_birth[5:7])
    d = int(str_birth[8:10])

    Y = int(str_date[0:4])
    M = int(str_date[5:7])
    D = int(str_date[8:10])
    
    # diff with corrections
    days = (31 + (D - d)) if (D < d) else (D - d)

    months = (12 + (M - m)) if (M < m) else (M - m)
    if (D < d):
        months-=1

    years = (Y - y) if ((M - m) == 0) else ((Y - y) - 1)
    
    return years