a = [{ 'main_color': 'red', 'second_color':'blue'},
     { 'main_color': 'yellow', 'second_color':'green'},
     { 'main_color': 'yellow', 'second_color':'blue'}]

def in_dictlist(key, value, my_dictlist):
    for entry in my_dictlist:
        if entry[key] == value:
            return entry
    return False

print(in_dictlist('main_color','red', a))