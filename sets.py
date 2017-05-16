s = {10,20,10,30,50}
print(s)
ch = set("Hello")
print(ch)
lst=[1,2,4,4,3]
s=set(lst)
print(s)
s.update([50,60])
print('new after update:',s)
s.remove(50)
print(s)
k=frozenset(s)
print(k)