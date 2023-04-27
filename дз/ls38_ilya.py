#1
def italic_string(origin_func):
    def wrapper_func(*args):
        print('<i>' + str(*args) + '</i>')
        return origin_func(*args)
    return wrapper_func



#2
def strong_string(origin_func):
    def wrapper_func(*args):
        print('<strong>' + str(*args) + '</strong>')
        return origin_func(*args)
    return wrapper_func



#3
@italic_string
def stringtoitalics(*args):
    return

@strong_string
def strongstring(*args):
    return

stringtoitalics('smth')
strongstring('lol')

#4
def decorated_func(original_func):
    def wrapper_func(*args):
        original_func.__doc__='''First and Last name'''
        print(f'Text:{str(*args)}\nAuthor:{original_func.__doc__}')
        return original_func(*args)
    return wrapper_func

@decorated_func
def display(*args):
    return
display('ai;uhrgeihrguiewrgeuhg')