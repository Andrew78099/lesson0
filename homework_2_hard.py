def prov_del(n):
    seq = []
    for j in range(1,20):
        for i in range(1,20):
            s = j + i
            if n % s == 0 and j < i:
                seq.append(j)
                seq.append(i)
    result = str()
    for b in seq:
        result = result + str(b)
    print("Результат:",result)
n = input("Введите число от 3 до 20:")
n = int(n)
print(n)
while n < 3 or n > 20:
    n = input("Введите другое число:")
    n = int(n)
prov_del(n)
