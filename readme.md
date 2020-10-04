g++ -c -fPIC c2.cpp -o c2.o
g++ -shared -Wl,-soname,f.so -o libfoo.so  f.o