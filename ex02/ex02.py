def multiply_all(*args: int) -> int:

    result = 1
    for arg in args:
        result *= arg
    return result
    

print(multiply_all(1,2,3,4,5))