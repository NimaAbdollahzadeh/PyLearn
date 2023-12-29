def triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        triangle.append(row)
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle

def pascal_triangle(triangle):
    for row in triangle:
        row_str = ""
        for num in row:
            row_str += str(num) + " "
        print(row_str.strip())

n = int(input())
print("")
Triangle = triangle(n)
pascal_triangle(Triangle)