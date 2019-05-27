#A0=dict(zip((’a’,’b’,’c’,’d’,’e’),(’1’,’2’,’3’,’4’,’5’)))
# A1=range(10)
# A2=[iforiinA1ifiinA0]
# A3=sorted(A0[i]foriinA0)
# A4=[[i,i*i]foriinA1] 

a1 =range(10)
a0 =dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
a2 =[i for i in a1 if i in a0]
a3 =sorted(a0[i] for i in a0)
a4 =[[i ,i*i]for i in a1]

b =[a0 ,a1 ,a2 ,a3,a4]

for y in b:
    for x in y:
        print(x)   
    print(111111111111)
        
    
for i in range(5):
    print(globals()[f'a{i}'])