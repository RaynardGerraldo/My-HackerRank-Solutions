def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            leap = True
            return leap
        elif year % 100 == 0 and not year % 400 == 0:
            return leap
        
        else:
            leap = True
            return leap

    if not year % 4 == 0:
        return leap

