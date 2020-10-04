# g++ -c -fPIC c2.cpp -o c2.o

# g++ -shared -Wl,-soname,c2.so -o c2.so  c2.o


# read -p "Prompt" v1 v2 v3
# echo $v1
# echo $v2
# echo $v3
# echo $1+.cpp

g++ -c -fPIC $1.cpp -o $1.o

g++ -shared -Wl,-soname,$1.so -o $1.so  $1.o

echo "build sucessfully"