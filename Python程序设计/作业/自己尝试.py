import random

x=input('请输入你猜的数字：')
x=int(x)
y=random.randint(1, 100)
m=0
while True:
    m+=1
    if m<=6:
      if x<y:
        print(f'你个哈麻批，猜小了，你就只有{6-m}次机会了')
      elif x>y:
        print(f'你个哈麻批，猜大了，你就只有{6-m}次机会了')
      else:
        print(f'你好勾巴聪明啊，只用了{m}次就猜出来了')
    else:
      print(f'6次都没猜出来，纯纯哈皮')