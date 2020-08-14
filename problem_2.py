
a = [1,2,3,4]
b = [1,4,9,16]
c = [1,4,5,6]
d = [1,4,4,2]
e = [1,16,9,4]
f = [1,2,3,4,5]

def some_function(a, b):
    dict_a = {}
    dict_b = {}
    boolean_stop = False

    if len(a) == len(b):

        for i in a:
            dict_a[i] = i
        for k in b:
            dict_b[k] = k

        for x in dict_a:
            for y in dict_b:
                if (dict_a[x]**2) == dict_b[y]:
                    boolean_return = True
                    break
                else:
                    boolean_return = False
                    
        boolean_stop = boolean_return
    return False



print(some_function(a,e))


#def function_2(a, b):
#    for k in 
#    if (a**2) in b:
#        pass
#    else:
#        return False

    

