#n = 1
#while n <= 10:
#    print(n)
#    n += 1


#total = 0
#n = int(input())
#while n != 0:
#    total += n  
#    n = int(input())
#print(total)


#total = float('-inf')
#n = int(input())
#while n < 0:
#    if n > total: 
#        total = n  
#    n = int(input())
#print(total) 


#total = 0
#n = int(input())
#while n != 0:
#    total += 1  
#    n = int(input())
#print(total) 


total = 0  #кол-во введенных знач
amount = 0 #сумма введ знач
n = int(input())
while n != 0:
    total += 1  
    amount = amount + n
    n = int(input())
print(amount / total) 