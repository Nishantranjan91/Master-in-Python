#string formatting
template="Dear{},you are awesome.Take this {}$ bag" 
a="john"
a1=10000
b="jack"
b1=1000
c="marie"
c2=300
s1=template.format(a,a1)
print(s1)
print(f"{a}you are awesome and take this {a}$ bag")