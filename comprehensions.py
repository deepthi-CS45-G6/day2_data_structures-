#List Comprehensions
num=[i for i in range(10)]
print(num)
#squares
squares=[x*x for x in range(1,5)]
print(squares)
#even
even=[x for x in range(1,11) if x%2==0]
print(even)

#Set Comprehensions
square={x*x for x in range(1,5)}
print(square)
even={x for x in range(1,11) if x%2==0}
print(even)

#Dictionary Comprehension
even={x:x*x for x in range(1,11) if x%2==0}
print(even)


