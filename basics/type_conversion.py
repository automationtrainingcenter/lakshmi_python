# this program explains conversion one type of data into another type


# any string data is true and empty string is false
# string to boolean conversion
s1 = ""
b1 = bool(s1)
print("s1 is of type:", type(s1))
print("b1 is of type:", type(b1))
print(s1)
print(not b1)

# integer to string conversion
n1 = 200
n2 = 0

str1 = str(n1)
str2 = str(n2)
print("n1 is of type:", type(n1))
print("str1 is of type:", type(str1))
print(n1 + n2)
print(str1 + str2)

# integer to boolean conversion
# any integer number is true and 0 is false
bl1 = bool(n1)
bl2 = bool(n2)
print("n1 is of type:", type(n1))
print("bl1 is of type:", type(bl1))
print(bl1)
print(bl2)

# boolean to integer
bo1 = True
i1 = int(bo1)
i2 = int(not bo1)
print("bo1 of type:", type(bo1))
print("i1 of type:", type(i1))
print("i1 is:", i1)
print("i2 is:", i2)
print(i1 + i2)

# boolean to string
st1 = str(bo1)
st2 = str(not bo1)
print("st1 is of type:", type(st1))
print("bo1 is of type:", type(bo1))
print(st1)
print(st2)
print(st1 + st2)

# float to integer
f1 = 12.321
in1 = int(f1)
print("f1 is of type:", type(f1))
print("in1 is of type:", type(in1))
print(in1)

# integer to float
in2 = 130
f2 = float(in2)
print("in2 is of type:", type(in2))
print("f2 is of type:", type(f2))
print(f2)

# bool to float
f3 = float(bo1)
print("bo1 is of type:", type(bo1))
print("f3 is of type:", type(f3))
print(f3)

# float to string
str3 = str(f1)
print("f1 is of type:", type(f1))
print("str3 is of type:", type(str3))
print(str3 + st1)

# float to bool
b3 = bool(f1)
print("f1 is of type:", type(f1))
print("b3 is of type:", type(b3))
print(b3)

# string to integer
str4 = "12"
i4 = int(str4)
print("str4 is of type:", type(str4))
print("i4 is of type:", type(i4))
print(i4)

# string to float
str5 = "14.03"
f4 = float(str5)
print("str5 is of type:", type(str5))
print("f4 is of type:", type(f4))
print(f4)
