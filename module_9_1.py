


def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        b = func(int_list)
        a = str(func.__name__)
        results.update({a : b})
    print(results)






print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))