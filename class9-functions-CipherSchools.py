def show_loading():
    for _ in range(3):
        print("loading...")


a=5 
b=7
print(a+b)
show_loading()

print(a-b)
show_loading()

print(a*b)
show_loading()


def sheldon_knock(name,time=3):
    for _ in range(3):
        print("knock knock knock", name, time,"times")

sheldon_knock("leonard")

def add(a,b):
    return a+b
a=add(1,2)
print(a)    