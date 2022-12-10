sentence=eval(input("sentence:"))
num=eval(input("number:"))
a=sentence.split()
b=0
g=[]
for i in a:
    c=len(i)
    if c==num:
        b=1+b
        g.append(i)


print(b,"words have length",num)
print(g)