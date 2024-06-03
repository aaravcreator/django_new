def mul(a,b):
    return a*b

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def divide(a,b):
    # return a/b
    try:
        return a/b
    except Exception as e:
        print("Exception is ",e)
        # raise Exception("CANT PERFORM THIS DIVISION")
        return None