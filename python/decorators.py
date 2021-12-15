def f1(func):
    def wrapper(*args, **kwargs):
        print("[+] Started.")
        func(*args, **kwargs)
        print("[+] Ended.")

    return wrapper

@f1 # <--- This is the same as f = f1()()
def f(a):
    print(a)

f("Text added by function f")