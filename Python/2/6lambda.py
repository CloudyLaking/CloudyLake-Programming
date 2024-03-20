#lambda就像数学中的y=λx，是函数的数学型表达（匿名函数）
y = lambda a ,b: a + b
print(y(5,6))

#我们可以将匿名函数封装在一个函数内，这样可以使用同样的代码来创建多个匿名函数
def myfunc(n):
  return lambda a : a * n

