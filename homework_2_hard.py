def prov_del(n):
    seq = []
    for j in range(1,20):
        for i in range(1,20,1):
            s = j + i
            if n % s == 0 and j < i:
                if j != 0:
                    seq.append(j)
                if i != 0:
                    seq.append(i)
    result = str()
    for b in seq:
        result = result + str(b)
    print("Результат:",result)
n = input("Введите число от 3 до 20:")
n = int(n)
prov_del(n)