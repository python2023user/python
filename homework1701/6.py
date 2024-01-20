# 6. *. Create a single decorator: add_tag, which will take a tag name/type as an input parameter
# and will wrap a text returned from a function with the chosen tag, using the same syntax as the
# previous task. In essence it’s a single decorator that does everything and more as task #5.

# TEST CODE:
# @add_tag("b")
# @add_tag("em")
# @add_tag("u")
# def greet(name):
# return f"Hello, {name}"
# print(greet("Peter"))

# OUTPUT:
# "<b><em><u>Hello, Peter</u></em></b>"

def add_tag(tag):
    def decorator(func):
        def wrapper(text):
            text = func(text)
            return f"<{tag}>{text}</{tag}>"
        return wrapper
    return decorator

@add_tag("b")
@add_tag("em")
@add_tag("u")
def greet(name):
    return f"Hello, {name}"
print(greet("Peter"))