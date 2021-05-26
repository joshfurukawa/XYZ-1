def lone_sum(a, b, c): 
    if a == b and a == c and b == c:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    elif a >= b:
        return 0
    else:

        return a + b + c 
a=int(input("Input A :"))
b=int(input("Input B :"))
c=int(input("Input C :"))
print(lone_sum(a,b,c) )
