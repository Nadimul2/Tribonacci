def tribonacci(signature, n):
    num1 = signature[0]
    num2 = signature[1]
    num3 = signature[2]
    trilist = [num1, num2, num3, ]
    num4 = num1 + num2 + num3
    trilist.append(num4)
    result = 0
    for num in range(4, n):
        result = sum(trilist[-3:])
        trilist.append(result)
    return trilist

n = input('Enter range: ')
tribonacci([1, 1, 2], n)
