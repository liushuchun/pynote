#pythonic建议

##python is 与 ==
```
Python中的对象包含三要素：id、type、value
其中id用来唯一标识一个对象,type标识对象的类型,value是对象的值
is判断的是a对象是否就是b对象,是通过id来判断的
==判断的是a对象的值是否和b对象的值相等,是通过value来判断的
如下代码或许可以帮助你理解.

>>> a = 1
>>> b = 1.0
>>> a is b
False
>>> a == b
True
>>> id(a)
12777000
>>> id(b)
14986000
>>> a = 1
>>> b = 1
>>> a is b
True
>>> a == b
True
>>> id(a)
12777000
>>> id(b)
12777000
```

##p is None 比 p==None更快
```
在python中,is检查两个对象是否是同一个对象,而==检查他们是否相等. 例如： 
p = [1]q = [1]p is q # False 因为他们不是同一个对象p == q # True 因为他们的值相等但是有且仅有一个None,他们总是相同的,所以会返回True. p = Noneq = Nonep is q # True 因为他们都指向同一个"None"a='test'b=ac=ab is c #True 因为他们都指向相同的对象a所以如果你要比较两个值是否相同就用==,如果比较是否是同一个对象就用is. 其实python中的is比较的对象很像C语言中的指针,只有地址相同的指针才是同一个指针.
```
