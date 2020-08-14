def function_3(a,b):
    if len(a)==len(b):
        pass
    else:
        return False
    
    for char in a:
        if char in b:
            pass
        else:
            return False

    return True
    #dict_a = {}
    #dict_b = {}



a = "pie"
b = "eip"
c = "pies"
d = "pwe"

print(function_3(a,b))