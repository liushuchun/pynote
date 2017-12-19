# 随机数种子
`random.seed(1)`

## random.random()

`random.random()`用于生成一个0到1的随机符点数: `0 <= n < 1.0`
## random.uniform(a, b)

random.uniform的函数原型为：random.uniform(a, b)，用于生成一个指定范围内的随机符点数。如果a > b，则生成的随机数n: b <= n <= a。如果 a <b， 则 a <= n <= b.

## random.randint(a, b)

　　random.randint()的函数原型为：random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b

## random.choice(sequence)
　　random.choice从序列中获取一个随机元素。其函数原型为：random.choice(sequence)。参数sequence表示一个有序类型。这里要说明 一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence。有关sequence可以查看python手册数据模型这一章，也可以参考：http://www.17xie.com/read-37422.html 。
`print random.choice("学习Python")`   

## random.sample(sequence, k)
　　random.sample的函数原型为：random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列，而是返回一个新list。

```python
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
    slice = random.sample(list, 5)  #从list中随机获取5个元素，作为一个片断返回  
    print slic
```

## random.shaffle
random.shuffle的函数原型为：random.shuffle(x[, random])，用于将一个列表中的元素打乱。

Note: shuffle 只是将传入数组打乱，返回值为None。

```
p = ["Python", "is", "powerful", "simple", "and so on..."]  
    random.shuffle(p)  
    print p  
    #['powerful', 'simple', 'is', 'Python', 'and so on...']  
```



