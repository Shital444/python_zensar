print("hello python")
userVar=input("Enter string:");y=50
print(f"y={y}")
print("y=",y)
floatX=float(input("Enter float value:"))
print(f"float value is {floatX}")
a=b=c=80
print(f"a={a}, b={b}, c={c}")
ax,bx,cx=50,20,3.5
print(f"ax={ax},bx={bx},cx={cx}")
a=3
b=5
sum=a+b
print(f"sum is{sum}")
int_var=10
float_var=20.5
string_var="hello"
bool_var=True
list_var=[44,55,888,"hello",8.6]
print(f"list={list_var}");print(f"list index1={list_var[1]}")
print(f"list={list_var[:]}");print(f"list inde1to3={list_var[1:4]}")
print(f"list last index={list_var[-1]}")
tuple_var=(11,77,22,44)
set_var={44,88,22}
dict_var={1:'A','B':2}

print(f"list={list_var[:]}");print(f"list in reverse order is={list_var[::-1]}")

print(f"list middle number is:{list_var[2]}")
list_var.append(7)
print(f"modified list is:{list_var}")
list_var.extend([32,66,43,234])
print(f"modified list is:{list_var}")
list_var.insert(3,234)
print(f"modified list is:{list_var}")
list_var.remove(234)
print(f"modified list is:{list_var}")
list_var.pop(5)
print(f"modified list is:{list_var}")
list_var.reverse()
print(f"modified list is:{list_var}")
tuple_var=(11,77,22,44)
print(tuple_var+(12,55))
set_var={44,88,22};print(f"{set_var}")
dict_var={1:'A','B':2};print(f"{dict_var}")
print(f"Type of set_var={type(set_var)}")
set_var.add(5);print(f"{set_var}")
set_var.discard(88);print(f"{set_var}")

dict_var={1:'A',2:'B'};print(f"{dict_var}")
dict_var['c']=3;print(f"Added new key value in dictionary={dict_var}")
dict_var[1]=44;print(f"Updated dictionary key 1={dict_var}")
dict_var.pop('c');print(f"Remove dictionary key c={dict_var}")
keys=dict_var.keys();print(f" dictionary keys are={keys}")
values=dict_var.values();print(f" dictionary values are={values}")
items=dict_var.items();print(f" dictionary items are={items}")