file=open("abc.txt",'x')
file.write("hi my name is Nishant Ranjan")
file.close()
file=open("abc.txt","r")
content=file.read()
print(content)
file.close()
 fil
 file = open("xyz.txt" , 'r');
 file.write("hello again")
 content=file.read()
 print(content)
 file.close()
 file=open("abc.txt",'a')
 file.write("my name is nishant")
 file.close()
 file=open("abc.txt","r")
 content=file.read()
 print(content)
 print("my name is %s and weight is %d kg"%("ds",70))
name="ds"
wt=70
 print("my name is { ds} and my wt is{70}kg".format(name,70))
 def fun(name):
     print("my name is"+name)
     print(f'my name is {name}'