"# hello from c lang" 
import ctypes
import pathlib

path = pathlib.Path().absolute() / "c2.so"
print(path)
c = ctypes.CDLL(path)
# c.add()
print(dir(c))