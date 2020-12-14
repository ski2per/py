def yell(text):
    return text.upper() + '!'

print(yell('hello'))

bark = yell
print(bark('woof'))

# >>> del yell
# >>> yell('hello?')
# NameError: name 'yell' is not defined
# >>> bark('hey')
# HEY

print(bark.__name__)


funcs = [bark, str.lower, str.capitalize]
print(funcs)
for f in funcs:
    print(f, f("hi there"))

print(funcs[0]("yo man"))

def greet(func):
    greeting = func("Hi, I'm Python")
    print(greeting)

greet(yell)

def wisper(text):
    return text.lower() + '...'

greet(wisper)

print(map(yell, ['Hi', 'Hey', 'hi']))
