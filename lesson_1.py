#count_max = 1
#count_pre_max = 0
#n = int(input())
#for i in range (1, n + 1):
#    m = int(input())
#    if m > count_max:
#        count_pre_max = count_max
#        count_max = m
#    elif m > count_pre_max and m < count_max:
#        count_pre_max = m
#print(count_max)
#print(count_pre_max)   



#на ввод 1, 2, 3, 4 
#gold = 99 #1
#silv = 100 #5
#n = int(input())
#for i in range (1, n + 1):
#    num = int(input())
#    if num < gold:
#        silv = gold 
#        gold = num
#    elif num > gold and num < silv:
#        silv = num
#print(gold, silv)


#n = int(input()) #количество элементов
#even = 0
#odd = 0
#for i in range(1, n + 1):
#    num = int(input())
#    if num % 2 == 0:
#        even += 1
#    elif num % 2 != 0:
#        odd += 1          
#print(even, odd, sep = "\n")    
   

#n = int(input())
#count = 0
#for i in range (1, n + 1):
#    num = int(input())
#    if num % 3 == 0 or num % 5 == 0:
#        count += num    
#print(count)


#n = int(input())
#prev_dig = int(input())
#count = 0
#for i in range(1, n):
#    num = int(input())
#    if num > prev_dig:
#        count += 1
#    prev_dig = num
#print(count)


#n = int(input())
#gold = (- 1000)
#for i in range(1, n + 1):
#    num = int(input())
#    if num % 2 == 0 and num > gold:
#        gold = num
#print(gold)
        

#n = int(input())
#count = 1
#found = 0
#for i in range(1, n + 1):
#    num = int(input())
#    if num > 0:
#        count = count * num
#        found += 1
#if found > 0:
#    print(count)
#else:
#    print('0')    
                

#n = int(input())
#gold = float('-inf')
#count = 0
#for i in range(1, n + 1):
#    num = int(input())
#    if num > gold:
#        gold = num 
#        count = 1
#    elif num == gold:
#            count += 1
#print(count)        


#n = int(input())
#n_max = 1
#n_min = 0
#for i in range(1, n + 1):
#    num = int(input())
#    if num > n_max:
#        n_min = n_max   
#        n_max = num 
#    elif n_min < num < n_max:
#        n_min = num 
#print(n_min)           


n = int(input())
n_min = float('inf')
count = 0
for i in range(1, n + 1):
    num = int(input())
    if num % 2 == 0 and num < n_min:
        n_min = num
        count += 1
print(n_min)        
if n_min != float('inf'):
        print('0')

                