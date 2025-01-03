calls = 0

def count_calls ():
    global calls
    calls += 1

def string_info (string):
    count_calls()
    str_tuple = (len(string), string.upper(), string.lower())
    return str_tuple

def is_contains (string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        exists = string.lower() in list_to_search[i].lower()
        if exists == False:
            continue
        else:
            break
    return exists

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)