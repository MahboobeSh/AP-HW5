def func(a,b,c,*args,**keywords):
    print(a ,b ,c)
    for arg in args:
        print(f'arg ={arg}')
    for key in keywords:
        print(f'key ={key} , value ={keywords[key]}')
        
        
func(1 ,3,2 ,'acd','asd','asdf',234,A=26 ,B=27 ,C=28,m=9523067)
