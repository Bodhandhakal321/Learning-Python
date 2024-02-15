<!-- learning behind the seen of loops
>>> open('chai.py') 
<_io.TextIOWrapper name='chai.py' mode='r' encoding='cp1252'>
>>> f = open('chai.py') 
>>> f.readline() 
'import time\n'
>>> f.readline()
'print ("chai is herr")\n'
>>> f.readline()
'\n'
>>> f.readline()
'username = "bodhan"\n'
>>> f.readline()
'print(username)'
>>> f.readline()
''
>>> -->
<!-- loop 
>>> for line in open('chai.py'):
...     print(line,end='')     
...
import time
print ("chai is herr")

username = "bodhan"
print(username)>>> -->
<!-- iter keyword
>>> myList = [1,2,3,4]
>>> I = iter(myList) 
>>> I
<list_iterator object at 0x000001DD2FCEACB0>
>>> 
>>> I. __next__()
1
>>> I. __next__()
2
>>> I. __next__()
3
>>> I. __next__()
4
>>> I. __next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>-->