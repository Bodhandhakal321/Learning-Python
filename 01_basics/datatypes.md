<!-- >>>   a =3
>>>  a = 'chai aur code'
>>> a = 3.14
>>> 
>>> a = 'chai aur code'
>>> a = 2.14
>>> a = 5
>>> b = 2
>>> a= a+2
>>> a
7
>>> myListOne = [1,2,3]
>>> myListTwo = myListOne
>>> myListOne = 'chai'
>>> myListTwo
[1, 2, 3]
>>> myListOne = [1,2,3] 
>>> myListTwo
[1, 2, 3]
>>> myListOne             
[1, 2, 3]
>>> myListOne [0] = 33
>>> myListOne
[33, 2, 3]
>>> myListTwo 
[1, 2, 3]
>>>
 -->

 <!-- >>> l1 = [1,2,3]
>>> l2 = l1  just only one refrences
>>> l1
[1, 2, 3]
>>> l2
[1, 2, 3]
>>> l1[0] = 44
>>> l1
[44, 2, 3]
>>> l2
[44, 2, 3]
>>>  -->
<!-- //mutable immutable -->
<!-- >>> p1 = [1,2,3]
>>> p2 =p1
>>> p2 = [1,2,3]
>>> p1[0] =55
>>> p1
[55, 2, 3]
>>> p2
[1, 2, 3]
>>>  -->


<!-- learning numbers -->
>>> x = 2
>>> y =3
>>> z =4
>>> x+y
5
>>> int(2.34)
2
>>> float(40)
40.0
>>> 'chai'+ 'code' 
'chaicode'
>>> 

<!-- to read repr(), string(), priint() -->

>>> x=2
>>> y=3
>>> z=4
>>> x,y,z
(2, 3, 4)
>>> y%2
1
>>> z**2
16
>>> 100 **2
10000
>>> 2 **100
1267650600228229401496703205376
>>> 2 **1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
>>> repr('chai') 
"'chai'"
>>> str('chai')
'chai'
>>> print('chai')
chai
>>> 1<2
True
>>> 2<1
False
>>> x<y and y<z
True
>>>
>>> import math
>>> math.floor(4.9) 
4
>>> math.trunc(2.9)
2
>>> math.trunc(2.9)
2
>>> math.trunc(-2.9) 
-2
>>> 2+1j
(2+1j)
>>> (2+1j)*3
(6+3j)
>>>
<!-- >>> 0o20 octal --> 

16
<!-- >>> int('64', 8)
52
>>> to octal easy -->
>>> 0x16  
22
>>> 0xFF
255
>>> 0b1000
8
>>>
<!-- bitwise
>>> x=1
>>> x << 2
4
>>> --> 
<!-- learning for decimal
>>> import random  
>>> l1 = ['masala tea', 'milktea']
>>> random.choice(l1)\
... random.choice(l1) 
  File "<stdin>", line 2
    random.choice(l1)
    ^^^^^^
SyntaxError: invalid syntax
>>> random.choice(l1)
'masala tea'
>>>
>>> random.shuffle(l1)
>>> l1
['milktea', 'masala tea']
>>> l1
['milktea', 'masala tea']
>>>
>>> l1
['milktea', 'masala tea']
>>> 0.1 + 0.1 + 0.4
0.6000000000000001
>>> 0.1+0.1 + 0.1
0.30000000000000004
>>> 0.1+0.1 + 0.1 - 0.3
5.551115123125783e-17
>>> (0.1+0.1 + 0.1) - 0.3 
5.551115123125783e-17
>>> from decimal import decimal
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'decimal' from 'decimal' (C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2032.0_x64__qbz5n2kfra8p0\Lib\decimal.py)
>>> from decimal import Decimal
>>> Decimal('0.1') + Decimal ('0.1') + Decimal('0.1')
Decimal('0.3')
>>> Decimal('0.1') + Decimal ('0.1') + Decimal('0.1') -Decimal ('0.3')
Decimal('0.0')
>>> -->
<!-- sets opearions
>>> setone = {1,2,3,4} 
>>> setone &{1,3}
{1, 3}
>>> setone|{1,3}  
{1, 2, 3, 4}
>>> setone - {1,2,3,4}
set()
>>> type({})
<class 'dict'>
>>> --> 
<!-- python treats true by 1 false by 0  
>>> type(True)
<class 'bool'>
>>> True ==1
True
>>> False ==0
True
>>> True is 1
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
False
>>> True 
True
>>> True +4
5
>>>-->
<!-- string slicing

>>> chai = "masala chai"
>>> first_chai = chai[0]
>>> print(first_chai)
m
>>> chai 
'masala chai'
>>> slice_chai = chai[0:6]
>>> print(slice_chai)
masala
>>> -->
<!-- stripping 
>>> chai = "masala chai"
>>> first_chai = chai[0]
>>> print(first_chai)
m
>>> chai 
'masala chai'
>>> slice_chai = chai[0:6]
>>> print(slice_chai)
masala
>>> num_list = "0123456789"
>>> num_list[:] 
'0123456789'
>>> num_list[3:] 
'3456789'
>>> num_list[:7]  
'0123456'
>>> num_list[0:7:3] 
'036'
>>> chai           
'masala chai'
>>> print(chai.lower()) 
masala chai
>>> print(chai.upper()) 
MASALA CHAI
>>> chai
'masala chai'
>>> chai = "   MASALA CHAI  "
>>> chai
'   MASALA CHAI  '
>>> print(chai.strip()) 
MASALA CHAI

>>>
>>> chai  = "lemon , ginger, masala, mint" 
>>> print(chai.split("," )) 
>>> chai = "masala chai" 
>>> print(chai.find("chai"))
7
>>> print(chai.find("Chai")) 
-1 negone for not found
>>>
 -->
 <!-- findind count by using count 
 >>> chai = "masala chai chai chai"
>>> print(chai.count("chai")) 
3
 -->
 <!-- placeholder
 
 >>> chai_type = "Masala chai"
>>> quantity =2
>>> order = "I ordered {} cups of {} chai"
>>> order
'I ordered {} cups of {} chai'
>>> print(order.format(quantity, chai_type))
I ordered 2 cups of Masala chai chai
>>> -->
<!-- string to list using join operation  
>>> chai_variety 
['Lemon', 'MAsala', 'Ginger']
>>> print("".join(chai_variety)) 
LemonMAsalaGinger
>>> print(" ".join(chai_variety)) 
Lemon MAsala Ginger
>>> print(",  ".join(chai_variety)) 
Lemon,  MAsala,  Ginger
>>> print("-  ".join(chai_variety)) 
Lemon-  MAsala-  Ginger
>>>  
->
<!-- length and print each every letter
>>> chai = "masla chai"
>>> print(len(chai)) 
10
>>> chai
'masla chai'
>>> for letter in chai:
...     print(letter)
...
m
a
s
l
a

c
h
a
i
>>>
 --> 
 <!-- use r for raw 
 SyntaxError: invalid syntax
>>> chai="He said,  \"Masal Chai is awesome\" " 
>>> chai="He said,  \"Masal Chai is awesome\" "
>>> chai
'He said,  "Masal Chai is awesome" '
>>> chai = "Masala \nChai"
>>> print(chai)
Masala
Chai
>>> chai = r"Masala\nChai"
>>> print(chai)
Masala\nChai
>>> chai = r"c:\\user\\wdp\\"
>>> print(chai)
c:\\user\\wdp\\
>>> chai = r"c:\user\wdp\"    
  File "<stdin>", line 1
    chai = r"c:\user\wdp\"
           ^
SyntaxError: unterminated string literal (detected at line 1)
>>> chai
'c:\\\\user\\\\wdp\\\\'
>>> chai= r"c:\user\pwd"
>>> print(chai)
c:\user\pwd
>>>
>>> chai = "masla chai"
>>> print("masl" in chai)
True
>>>
 -->

 <!-- learing list in pytho
 
 >>> tea_varieties = ["black", "green", "oolong","White"]
>>> print(tea_varieties)
['black', 'green', 'oolong', 'White']
>>> print(tea_varieties.[0]) 
  File "<stdin>", line 1
    print(tea_varieties.[0])
                        ^
SyntaxError: invalid syntax
>>> print(tea_varieties[0])  
black
>>> 
>>> print(tea_varieties)
['black', 'green', 'oolong', 'Herbal']
>>> tea_varieties[1:2] = "Lemon" 
>>> tea_varieties
['black', 'L', 'e', 'm', 'o', 'n', 'oolong', 'Herbal']
>>> tea_varieties
['black', 'L', 'e', 'm', 'o', 'n', 'oolong', 'Herbal']
>>> tea_varieties = ["black", "green", "oolong","White"]
>>> tea_varieties[1:2]          
['green']
>>> tea_varieties[1:2] = ["Lemon"]
>>> tea_varieties
['black', 'Lemon', 'oolong', 'White']
>>>
>>> tea_varieties[1:3]  
['Lemon', 'oolong']
>>> tea_varieties[1:3] = ["green", "Masala"] 
>>> tea_varieties       
['black', 'green', 'Masala', 'White'] replacing
>>>
  -->
  <!-- insert nothing
  
  >>> tea_varieties       
['black', 'green', 'Masala', 'White']
>>> tea_varieties
['black', 'green', 'Masala', 'White']
>>> tea_varieties[1:1]
[]
>>> tea_varieties[1:1] = ["test", "test"] 
>>> tea_varieties      
['black', 'test', 'test', 'green', 'Masala', 'White']
>>> tea_varieties[1:2] 
['test']
>>> tea_varieties[1:3] 
['test', 'test']
>>> tea_varieties[1:3] = []
>>> tea_varieties           
['black', 'green', 'Masala', 'White']
>>> -->
<!-- basic loops and conditions and append method
>>> tea_varieties           
['black', 'green', 'Masala', 'White']
>>> for tea  in tea_varieties:
...     print(tea)
...
black
green
Masala
White
>>> for tea  in tea_varieties:
...     print(tea, end="-") 
...
black-green-Masala-White->>>
>>> tea_varieties
['black', 'green', 'Masala', 'White']
>>> if "OOlong" in tea_varieties:
...     print("I have oolong tea")
...
>>> tea_varieties.append("OOlong")  //adding on list
>>> tea_varietes
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tea_varietes' is not defined. Did you mean: 'tea_varieties'?
>>> tea_varieties                  
['black', 'green', 'Masala', 'White', 'OOlong']
>>> if "OOlong" in tea_varieties:  
...     print("i have Oolong tea") 
...
i have Oolong tea
>>> tea_varieties.pop()             
'OOlong'
>>> tea_varieties 
>>> tea_varieties.remove("green")
>>> tea_varieties
['black', 'Masala', 'White']
>>> tea_varieties
['black', 'Masala', 'White']
>>> tea_varieties.insert(1, "green")  //insert and delete learning
>>> tea_varieties
['black', 'green', 'Masala', 'White']
>>>
 --> 
 <!-- list comprehension  and learning range [can implement loop on list]
 >>> range(10)                               
range(0, 10)
>>> print(range(10))
range(0, 10)
>>> y = range(10)
>>> y
range(0, 10)
>>> squared_nums = [x**2 for x in range(10)]
>>> squared_nums
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>>
 -->