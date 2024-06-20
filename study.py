import sys

n = 1
ch = "a"
print(sys.getrefcount(ch), sys.getrefcount(n))
ls = []
ls.append(ch)
ls.append(n)
print(sys.getrefcount(ch), sys.getrefcount(ls), sys.getrefcount(n))







