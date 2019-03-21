# for...in循环打印九九乘法表
for i in range(1,10):
   for j in range(1,i+1):
      print("{}*{}={:<4}".format(i,j,i*j),end =" ")
   print("")

# while 循环实现99乘法表（去掉偶数列）
i=1
while(i<=9):
   j=1
   while j<=i:
      while(i%2 !=0):
         print("{}*{}={:<2}".format(i,j,i * j),end = " ")
      else:
         print(end='\n')
      break
   j += 1
i += 1
print("")