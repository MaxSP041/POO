import random
class numer:
    
    def __init__(self):
        pass
    
    def numerosRandom(self):
        nu=[]
        for i in range(10):
            nu.append(random.randint(101, 999))
        return(nu)
    
    def primoFuc(self,num):
        if num <= 1:
            return 0  
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return 0  
        return 1  
    
    def impr(self,nums,primos):
        print(nums)
        print(primos)
        
        
    
obj=numer()
nums=obj.numerosRandom()
primos=[]
for num in nums:
    primos.append(obj.primoFuc(num))
obj.impr(nums,primos)