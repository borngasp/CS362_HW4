
def average(numlist):

    if (len(numlist) > 0):
       
        test = True

        for x in numlist:
            if(type(x) != int and type(x) != float):
                test = False

        if test:
            total = 0
            for x in numlist:
                total += x
        
            return total/len(numlist)
        
        else:
            return "Not a valid list"

    else:
        return "Not a valid list"