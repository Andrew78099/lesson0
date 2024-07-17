calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(s):
    count_calls()
    return ((len(s), s.upper(), s.lower()))


def is_contains(list_to_search, string):
    count_calls()
    flag = bool()
    for i in string:
        if i.lower() == list_to_search.lower():
            flag = True
        else:
            flag = False
    return flag


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
