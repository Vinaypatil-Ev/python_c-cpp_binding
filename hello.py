"# hello from c lang" 
import ctypes
import pathlib

path = pathlib.Path().absolute() / "c2.so"
print(path)
c = ctypes.CDLL("e:\\2AI\\1_ai\\_2020\\_github\\python\\python c binding\\c2.so")
# c.add()s