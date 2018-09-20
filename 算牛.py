# -*- coding: utf-8 -*-
dict={'A':1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,'J':10,'Q':10,"K":10}
a=[]
n=0
while n < 5:
    b=input("please input your card: ")
    if b not in dict.keys():
        print("请输入正确的牌")
    else:
        b=dict[b]
        a.append(b)
    n=n+1
if (a[2]+a[1]+a[0])%10==0:
    if a[3]+a[4] >=10:
        print("您的牌是牛 %s" % abs((a[3]+a[4])-10))
    else:
        print("您的牌是牛 %s" % abs((a[3]+a[4])))
elif (a[2]+a[3]+a[4])%10==0:
    if a[1]+a[0] >=10:
        print("您的牌是牛 %s" % abs((a[1]+a[0])-10))
    else:
        print("您的牌是牛 %s" % abs((a[1]+a[0])))
elif (a[2]+a[1]+a[3])%10==0:
    if a[0]+a[4] >=10:
        print("您的牌是牛 %s" % abs((a[0]+a[4])-10))
    else:
        print("您的牌是牛 %s" % abs((a[0]+a[4])))
elif (a[2]+a[1]+a[4])%10==0:
    if a[3]+a[0] >=10:
        print("您的牌是牛 %s" % abs((a[3]+a[0])-10))
    else:
        print("您的牌是牛 %s" % abs((a[3]+a[0])))
elif (a[2]+a[3]+a[0])%10==0:
    if a[1]+a[4] >=10:
        print("您的牌是牛 %s" % abs((a[1]+a[4])-10))
    else:
        print("您的牌是牛 %s" % abs((a[1]+a[4])))
elif (a[0]+a[1]+a[3])%10==0:
    if a[2]+a[4] >=10:
        print("您的牌是牛 %s" % abs((a[2]+a[4])-10))
    else:
        print("您的牌是牛 %s" % abs((a[2]+a[4])))
elif (a[0]+a[1]+a[4])%10==0:
    if a[3]+a[2] >=10:
        print("您的牌是牛 %s" % abs((a[3]+a[2])-10))
    else:
        print("您的牌是牛 %s" % abs((a[3]+a[2])))
elif (a[0]+a[3]+a[4])%10==0:
    if a[1]+a[2] >=10:
        print("您的牌是牛 %s" % abs((a[1]+a[2])-10))
    else:
        print("您的牌是牛 %s" % abs((a[1]+a[2])))
elif (a[1]+a[3]+a[4])%10==0:
    if a[0]+a[2] >=10:
        print("您的牌是牛 %s" % abs((a[0]+a[2])-10))
    else:
        print("您的牌是牛 %s" % abs((a[0]+a[2])))
elif (a[2]+a[4]+a[0])%10==0:
    if a[3]+a[1] >=10:
        print("您的牌是牛 %s" % abs((a[3]+a[1])-10))
    else:
        print("您的牌是牛 %s" % abs((a[3]+a[1])))
else:
    print("此牌无牛")
