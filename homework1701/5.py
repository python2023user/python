# 5. Create three decorators: make_bold, make_italic, and make_underline,
# which will have to wrap a text returned from a function in
# <b></b>, <i></i> and <u></u> respectively.

# TEST CODE:
# @make_bold
# @make_italic
# @make_underline
# def greet(name):
# return f"Hello, {name}"
# print(greet("Peter"))

# OUTPUT:
# "<b><i><u>Hello, Peter</u></i></b>"

def make_bold(func):
    def wrapper(text):
        name = func(text)
        return f"<b>{name}</b>"
    return wrapper

def make_italic(func):
    def wrapper(text):
        name = func(text)
        return f"<i>{name}</i>"
    return wrapper

def make_underline(func):
    def wrapper(text):
        name = func(text)
        return f"<u>{name}</u>"
    return wrapper

@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"
print(greet("Peter"))
