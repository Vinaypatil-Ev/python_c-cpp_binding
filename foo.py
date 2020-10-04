from ctypes import cdll
lib = cdll.LoadLibrary('./foo.so')

# class Foo(object):
#     def __init__(self):
#         self.obj = lib.Foo_new()

#     def bar(self):
#         lib.Foo_bar(self.obj)

# f = Foo()
# f.bar()

print(dir(lib))
lib.printname()