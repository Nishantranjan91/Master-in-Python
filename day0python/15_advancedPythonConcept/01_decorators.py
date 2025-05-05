def decorator(func):
    def wrapper():
        print("I am about to print hello....")
        func()
        print("I have executed this function....")

def say_hello():
    print("hello!")
say_hello()
f = decorator(say_hello)
()            
    