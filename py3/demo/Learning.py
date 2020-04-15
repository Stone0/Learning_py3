print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
# 构建L
print('----- 构建任意类型列表L -----')
L = [1, 'a', 3.5, [0, 'a']]
print('L:', L)
print()

print('----- 构建列表L -----')
L = ['a', 'b', 'c']
print('L:', L)
print('L[0]:', L[0])
print()

# 负数表示倒序访问
print('----- 倒序访问 -----')
print('L[1]:', L[1], ' --- L[-2]:', L[-2])
print()

# 添加元素append()
print('----- 添加元素到尾部 -----')
print('L:', L)
L.append('new')
print('new L:', L)
print()

# 插入元素insert()
print('----- 插入元素到某个元素前面 -----')
print('L:', L)
L.insert(0, 'you')
print('new L:', L)
print()

# 删除元素pop()
print('----- 删除最后一个元素 -----')
print('L:', L)
L.pop()
print('new L:', L)
print()

# 删除指定元素pop()
print('----- 删除指定元素 -----')
print('L:', L)
L.pop(3)
print('new L:', L)
print()

# 替换元素
print('----- 替换元素 -----')
print('L:', L)
L[-1] = 'last'
print('new L:', L)
print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
print()
print();print();print();

print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
# 构建Tuple
print('----- 构建元组Tuple, 不可修改 -----')
T = (1, 'a', 3.5, [0, 'a'])
print('tuple:', T)

# 访问元素
print('----- 访问元素 -----')
print('T[2]:', T[2])
print()

# 构建单元素Tuple
print('----- 构建单元素元组, 必须加逗号')
TS = (2333,)
print('TS:', TS)
print('TS[0]:', TS[0], ' --- ', 'TS[-1]:', TS[-1])
print()

# "修改"Tuple
print('''
----- 通过修改list元素达到修改元组的目的
      实际上是修改了元组元素list的指向
      元组元素指向不可变 list指向可变 -----''')
print('T:', T)
print('T_list:', T[-1])
T_L = T[-1]
print('T_L:', T_L)
T_L.insert(1, 'tl')
T_L.pop()
T_L[0] = 100
print('T_L:', T_L)
print('T_list:', T[-1])
print('T:', T)
print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
print()
print();print();print();

print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
# if 具有相同缩进的代码被视为代码块, if语句后接表达式, 然后用:表示代码块开始
print('----- 条件判断if -----')
age = 18
print('age:', age)
if age < 20:
    print('age < 20')
print()

# if-else else后面有个:
print('----- 两层判断if-else -----')
age = 20
print('age:', age)
if age < 18:
    print('age < 18')
else:
    print('age > 18')
print()

# if-elif-else
print('----- 多层判断if-elif-else -----')
age = 30
print('age:', age)
if age < 20:
    print('age < 30')
elif age == 30:
    print('age = 30')
else:
    print('age > 30')
print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
print()
print();print();print();

print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
# for
print('----- 循环for -----')
print('L:', L)
for l in L:
    print(l)
print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
print()
print();print();print();

print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
# while
print('----- 循环while -----')
i = 0
print('L:', L)
print('L.len:', L.__len__())
while i < L.__len__():
    print(L[i])
    i = i+1
print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
print()
print();print();print();

print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
# break 退出循环
print('----- 退出循环break -----')
i = 0
while True:
    print(i)
    i = i+1
    if i == 5:
        break
print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
print()
print();print();print();

print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
# continue 跳过循环
print('----- 跳过循环continue -----')
L = [75, 98, 59, 81, 66, 43, 69, 85]
print('L:', L)
sum = 0.0
avg = 0.0
n = 0
for l in L:
    sum = sum+l
    n = n+1
avg = sum/n
print('sum:', sum, ' --- ', 'avg:', avg)
sum = 0.0
n = 0
for x in L:
    if x < 60:
        continue
    sum = sum+x
    n = n+1
avg = sum/n
print('sum(60↑):', sum, ' --- ', 'avg(60↑):', avg)
print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
print()
print();print();print();

print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
# Dict键值对集合
print('----- 构建键值对集合dict(k,v) -----')
D = {'a': 17, 'b': 18, 0: 19}
print('D:', D)
print()

# 访问Dict
print('----- 访问dict -----')
print('D[\'a\']:', D['a'])
print('D[0]:', D[0])
print()

print('----- 通过get访问防止异常 -----')
print(''' <<<'D[\'xxx\']:', D['xxx'] ''')
print(''' >>>KeyError:'xxx' ''')
print('D.get(\'a\'):', D.get('a'))
print('D.get(\'xxx\'):', D.get('xxx'))
print()

'''
Dict特点:
1. 查找速度快, 无论量级多少(10个元素, 10万个元素)都一样, list随元素增加查找速度下降
2. 缺点是占用内存大, 浪费很多内存, list占用内存小
3. key不可重复, 不可修改, 故不可用list作为key, tuple可以
'''
print('----- key不可修改, 故list不可为key, tuple可以 -----')
D = {(1, 2): 'aaa', ('a', 'b'): 'a,b'}
print('D:', D)
print('D[(1, 2)]:', D[(1, 2)])
print()

# 更新Dict
print('----- 更新Dict -----')
print('D[\'newKey\'] = \'newValue\'')
D['newKey'] = 'newValue'
print('D:', D)
print()

# 遍历Dict
print('----- 遍历Dict -----')
print('D:', D)
for key in D:
    print('D[', key, ']:', D.get(key))
print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
print()
print();print();print();

print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
# Set无序集合
print('----- 构建Set集合 -----')
S = {'a', 1, 0, 'b'}
print('S = {\'a\', 1, 0, \'b\'}')
print('S:', S)
print()

# 访问Set
print('----- 由于Set无序, 只能通过判断来访问Set, 区分大小写 -----')
print('S = {\'a\', 1, 0, \'b\'}')
print('\'xxx\' in S')
print('xxx是否在S中:', 'xxx' in S)
print('0是否在S中:', 0 in S)
print()

# 遍历Set
print('----- for遍历Set -----')
print('S = {\'a\', 1, 0, \'b\'}')
for s in S:
    print(s)
print()

# 更新Set
print('''
----- 更新Set
      使用add()添加元素, 若存在则无效
      使用remove()删除元素, 若不存在则报错-----''')
print('S = {\'a\', 1, 0, \'b\'}')
S.add('newValue')
print('S:', S)
S.add(0)
print('S:', S)
S.remove(1)
print('S:', S)
print(''' <<<S.remove(10) ''')
print(''' >>>KeyError: 10 ''')
print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
print()
print();print();print();

print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
# 函数
print('''
----- 定义函数
def 方法名 (参数):
    方法体

def hello (name):
    print('hello', name)
-----''')
def hello (name):
    print('hello', name)
print()

print('----- 调用函数, 方法名(参数), hello(\'xxx\') -----')
hello('xxx')
print()

# 返回多个值
print('----- 函数返回多个值, 实际上返回一个tuple -----')
def d (x, y):
    x = x+1
    y = y+5
    return x, y
r = d(5, 5)
a, b = d(5, 5)
print('d(5, 5):', d(5, 5))
print('r = d(5, 5):', r)
print('a, b = d(5, 5):', a, b)
print()

# 递归函数
print('----- 递归函数, 通过if-return跳出递归 -----')
def recursion (n):
    if n == 1:
        return 1
    return recursion(n-1)*n
r = recursion(3)
print('r = recursion(3):', r)
print()

# 定义默认参数
print('''
----- 给函数设定默认参数
默认参数只能在必须参数后面
输入一个参数则另一个默认
输入两个参数则覆盖默认参数
-----''')
def getBirthday (b1, b2=(1, 1)):
    print('Birthday:', b1, b2)

print('输入一个参数 getBirthday((7, 19)):')
getBirthday((7, 19))
print()
print('输入两个参数 getBirthday((7, 19), (3, 21)):')
getBirthday((7, 19), (3, 21))
print()

# 定义可变参数
print('----- 给函数定义可变参数, 能接受任意个参数 -----')
def getName (*names):
    print(names)

print('不输入参数 getName():')
getName()
print()
print('输入一个参数 getName(\'you\'):')
getName('you')
print()
print('输入两个参数 getName(\'you\', 0):')
getName('you', 0)
print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
print()
print();print();print();

print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
# 切片
print('----- 通过切片取list的部分元素 -----')
print('L:', L)
print('L[0:3]:', L[0:3])
print('L[2:5]:', L[2:5])
print()

print('----- 只用:表示从头到尾 -----')
print('L[:]:', L[:])
print()

print('----- 指定三个参数表示每N个取一个 -----')
print('L[::3]:', L[::3])
print()

print('----- tuple也可切片 -----')
print('T:', T)
print('T[0:2]:', T[0:2])
print('T[:]:', T[:])
print()

# 倒序切片
print('----- 倒序切片 -----')
print('L:', L)
print('L[-1:]:', L[-1:])
print('L[:-2]:', L[:-2])
print('L[-3:-1]:', L[-3:-1])
print()

# 字符串切片
print('----- 字符串也可看成list进行切片 -----')
S = 'abcdefg'
print('S:', S)
print('S[:3]:', S[:3])
print('S[-1:]:', S[-1:])
print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
print()
print();print();print();

print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
# 迭代
print('''
----- 只要是集合都可以用for...in迭代
有序集合: list, tuple, str, unicode
无序集合: set
无序集合并且具有 key-value 对: dict
-----''')
print('''
----- 索引迭代 enumerate() 
实际上是把List['a', 'b']的元素转换为Tuple[(0, 'a'), (1, 'b')]
-----''')
print('L:', L)
for index, name in enumerate(L):
    print('index:', index.__str__() + ' --- L[' + index.__str__() + ']:', name)
print()

# 迭代Dict
print('----- 迭代Dict的value values() -----')
print('D:', D)
print('D.values():', D.values())
print()
for v in D.values():
    print('Dv:', v)
print()

# 迭代kv
print('----- 迭代Dict的kv -----')
print('D:', D)
print('D.items():', D.items())
for k, v in D.items():
    print('k:', k, '- v:', v)
print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
print()
print();print();print();

print('# # # # # # # # # # # # # # # # # # # # # # # # # ')
