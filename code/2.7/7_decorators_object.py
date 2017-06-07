
def hi(name="yasoob"):
    return "hi" + name

print(hi())


greet = hi

print(greet())


del hi

print(greet())


print(hi())
