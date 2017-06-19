#coding:utf-8
__author__ = 'jun'
from sympy import *
x = Symbol('x')
y = Symbol('y')

#print solve(x * 2 - 4 ,x) #第一个参数为要解的方程，方程要求右边等于0第二参数是要解的未知数
print solve([2*x-y-3,3*x+y-7],[x,y])