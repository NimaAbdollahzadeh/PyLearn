def diamond(n):
    if n % 2 == 0:
        n += 1
    for i in range(1, n+1 , 2):
        spaces =  " " * ((n - i) // 2)
        stars = "*" * i
        print(spaces + stars)
    
    for i in range(n- 2, 0, -2):
        spaces = " " * ((n - i) // 2)
        stars = "*" * i
        print(spaces + stars)

diamond(8)