def vay():
    numbers=[30,50,16,2,5,8,9]
    sum=0
    length=0
    product=1
    subtraction=0
    for n in numbers:
     sum += n
     length +=1
     product *=n
     subtraction -=n
     print('the sum of the numbers is ', sum)
     
     print('the numbers of the numbers is ', length)
     
     print('the subtraction of the numbers is ', subtraction)
     
     print('the product of the numbers is ', product)
    
vay()