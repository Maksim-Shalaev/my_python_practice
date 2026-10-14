#n = 0
#while n < 10:
#    n += 1
#    if n % 2 == 0:
#        continue
#    print(n)


#att = 3
#while att > 0 :
#    print(f"Remaining of attempts: {att}")
#    att -= 1
#    num = int(input())
#    if num == 1234:
#            print("PIN accepted")
#            break
#else:
#    print("Attempts are finished")



count = 0
while count < 1000:
    n = int(input())
    count = count + n
    if n == 0:
        print(count)
        break
print(count)    
