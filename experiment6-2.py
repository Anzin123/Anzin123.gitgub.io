# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 10:11:36 2022

@author: Anzin
"""
import numpy as np
import matplotlib.pyplot as plt
#Windows
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体为黑体
#mpl.rcParams['font.sans-serif']=['SimSun'] #【"SimSun"字体也可以，如果电脑中没有黑体字库】
mpl.rcParams['axes.unicode_minus'] = False #解决将负号'-'显示为方块的问题

N=5
class1=[72,89,75,92,85,98,82,89,75,75,67,84,69,60,71,63,84,82,67,74,89,56,76,81,70,59,68,95,76,100,68,76,74,87,85,80,77,87,85,79]
class2=[78,80,86,76,65,69,91,80,68,78,79,57,96,80,89,85,65,76,68,69,85,75,99,67,46,69,75,43,88,79,83,84,78,74,73,80,92,68,69,78]
class3=[87,85,91,80,76,84,89,79,69,78,94,82,79,85,88,69,60,92,95,88,83,85,90,92,69,74,75,59,89,85,97,85,89,94,90,84,69,84,89,94]

num1=0
num2=0
num3=0
num4=0
num5=0
for i in class1:
    if i<60:
        num1+=1
    elif i<70 and i>=60:
        num2+=1
    elif i>=70 and i<80:
        num3+=1
    elif i<90 and i>=80:
        num4+=1
    elif i<=100 and i>=90:
        num5+=1
list1=[num1,num2,num3,num4,num5]

num21=0
num22=0
num23=0
num24=0
num25=0
for j in class2:
    if j<60:
        num21+=1
    elif j<70 and j>=60:
        num22+=1
    elif j>=70 and j<80:
        num23+=1
    elif j<90 and j>=80:
        num24+=1
    elif j<=100 and j>=90:
        num25+=1
list2=[num21,num22,num23,num24,num25]            

num31=0
num32=0
num33=0
num34=0
num35=0
for h in class3:
    if h<60:
        num31+=1
    elif h<70 and h>=60:
        num32+=1
    elif h>=70 and h<80:
        num33+=1
    elif h<90 and h>=80:
        num34+=1
    elif h<=100 and h>=90:
        num35+=1
list3=[num31,num32,num33,num34,num35]


x = np.arange(N)
width = 0.25
rects1 = plt.bar(x, list1, width, color = 'r',label="class1")
rects2 = plt.bar(x+width, list2, width, color='y',label="class2")
rects3 = plt.bar(x+width+width, list3, width, color = 'b',label="class3")


#美化图表
plt.ylim(0,25)
plt.legend()
plt.xlabel("分数")
plt.ylabel('人数')
plt.title('班级人数分段成绩表 张三 2022xxxxxx')
#设置横轴记号的标签
plt.xticks (x+width/2,('x<60','60≤x<70', '70≤x<80', '80≤<90', '90≤x≤100'))
#plt.xticks(x) #设置横轴记号的标签【显示的记号是数值】，等效于不写此语句


plt.show()

