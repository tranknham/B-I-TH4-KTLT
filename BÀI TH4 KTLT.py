#BÀI TH4
#1
s=input('nhap chuoi:')
for ch in S:
    print(ch)
#3
string="tran kim nham"
print(string.swapcase())
   
#4
ds=input('danh sách: ').split()
#in cả dãy vừa nhập
print(ds)
#in dãy vừa nhập, mỗi phần tử trên một dòng
for so in ds:
    print(so)
def reversed_string(ds_string):
    return ds_string[::-1]

#5
my_string="dfghjkl"
reversed_string=my_string[::-1]

print(reversed_string)

#6
int pos =0;
for(int i=s.length();i>=0;i--)
  if(s[i]==' '){
      pos=i;
      break;
    }
string ho=s.substr(0,pos);
string ten=s.substr(pos+1);

#7
#8
def tu_dai_nhat(s):
    tudainhat = ""
    dscactu = s.split()
    for tu in dscactu:
        if (len(tu) > len(tudainhat)
            tudainhat = tu
    return tudainhat
s = input()
print(tu_dai_nhat(s))

#9+#10+#11+#12+#13+#14
ds = input('nhap chuoi:').split()
#cắt phần tử
x = ds[0:-1]
for c in x:
    print(c)
#thêm phần tử vào list
ds.append('abc')
for ch in ds:
    print(ch)
#bỏ phần tử khỏi list
ds.remove('123')
for ch in ds:
    print(ch)
#tìm kiếm phần tử trong list
print('vi trí của chuỗi abs là ",ds.index('abc'))
#sắp xếp các phần tử trong list
ds.sort()
for ch in ds:
      print(ch)
    

#17
print("Nhập vào số N cần tính tổng các ước số: ")
 
n = int(input())
sum = 0
 
for i in range(1, n+1):
    if (n % i == 0):
        sum += i
 
 
print("Tổng tất cả các ước số ", n, " là: ", sum)
     
#18
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        f0 = 0
        f1 = 1
        fn = 0
        while n >= 2:
            fn = f0 + f1
            f0 = f1
            f1 = fn
            n -= 1
        return fn
n = -1
while n < 0:
    n = int(input("Nhap vao so tu nhien n: "))
    if(n>=0):
        break
result = fibonacci(n)
print(result)

#19
t=tuple()
for i in range(1,1000000):
    dem = 0
    for j in range (1,i+1):
        if(i%j == 0):
            dem = dem + 1
    if(dem == 2):
        t=t+(i,)
print(t)

#20
def factorial(n):
    f=1
    while (n>1):
        f=f*n
        n=n-1
    return f
def ncr(n,r):
    return int(factorial(n) / (factorial(n-r)*factorial(r)))
n=10
print("ve tam giác pascal:");
for i in range(0,n+1):
    for j in range(0,n-i+1):
        print("",end=" ")
    for j in range(0,i+1):
        print(" {:<3}".format(ncr(i,j)),end="")
    print("")

#21
value=[]
items=[x for x in input("nhap các số nhị phân: ").split(',')]
for p in items:
    intp=int(p,2)
    if not intp%5:
        value.append(p)
print(','.join(value))

#22
values=[]
for i in range(1000,3001):
    s=str(i)
    if(int(s[0])%2==0)and(int(s[1]%2==0)and(int(s[2])%2==0)and(int(s[3]%2==0);
values.append(s)
print(",".join(values))

#23
s = input("Nhập câu của bạn: ")
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print ("Số chữ cái là:", d["LETTERS"])
print ("Số chữ số là:", d["DIGITS"])
                                                               
#24
s = input("Nhập câu của bạn: ")
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print ("Chữ hoa:", d["UPPER CASE"])
print ("Chữ thường:", d["LOWER CASE"])

#25
values = input("Nhập dãy số của bạn, cách nhau bởi dấu phẩy: ")
numbers = [x for x in values.split(",") if int(x)%2!=0]
print (",".join(numbers))

#26
import sys
netAmount = 0
while True:
    s = input("Nhập nhật ký giao dịch: ")
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print (netAmount)

