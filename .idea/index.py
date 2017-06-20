#coding:utf-8
__author__ = 'jun'
from sympy import *
x = Symbol('x')
y = Symbol('y')

#print solve(x * 2 - 4 ,x) #第一个参数为要解的方程，方程要求右边等于0第二参数是要解的未知数
#求2X-Y=3和 3X+Y=7 的X和Y
print solve([2*x-y-3,3*x+y-7],[x,y])

#求((n+3)/(n+2))^n 当n趋向于正无穷时的极限
n = Symbol('n')
s = ((n+3)/(n+2))**n
print limit(s, n, oo)

#求积分用 integrate
t = Symbol('t')
x = Symbol('x')
m = integrate(sin(t)/(pi-t),(t,0,x)) #这是fx
n = integrate(m,(x,0,pi)) #这是要求的，m代表式子，x为未知数，0和pi上下限
print n
