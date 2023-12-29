def manipulation_table():
    try:
        n = int(input("Enter number of rows: "))
        m = int(input("Enter number of columns: "))
    except:
        print("Input is invalid")

    rows = []
    columns = []

    for i in range(n):
        for j in range(m):
            columns.append((i+1)*(j+1))
        
        rows.append(columns)
        columns = []
    
    for row in rows:
        print(row)

manipulation_table()