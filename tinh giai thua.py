def giai_thua(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
# moi ban nhap n
c=giai_thua(n)
print("ket qua la=",c)