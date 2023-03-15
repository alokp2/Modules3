'''1.What is List? How will you reverse a list? 

List is a collection of data type which contains similar and dis-similar data elements at single location.List is mutable,orderable,and indexable.

'''
'''
2.How will you remove last object from a list? 
We can use the del operator to delete the last element using index. Further, we can use the pop() method to remove the last element.

Here are the example.

'''
l=[1,2,3,4]
del l[-1]
print(l)

li=[12,3,4,5,6,7]
li.pop()
print(li)

'''Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]? 
 list1[-1] = 25. we can check it further

'''
li3=[2, 33, 222, 14, 25]
print(li3)
print(li3[-1])

'''3.Differentiate between append () and extend () methods? 

Append only add one element to the list and Extend can multiple elements at a time to the list.

 '''

'''Write a Python function to get the largest number, smallest num and sum
of all from a list. '''
total=0
list5=[12,23,21,22,11,2,34,34,56,43]
def largest_num():
   print(max(list5))

def smallest_num():
   print(min(list5))
 

def total_sum():
    print("Total sum: ",sum(list5))

largest_num()
smallest_num()
total_sum()



'''How will you compare two lists? 
we can compare the two list using condition statement
'''

l1=[1,2,677,8,9,0]
l2=[2,3,4,5,6,7,8]
if li==l2:
    print("l1 and l1 are equal")
else:
    print("l1 and l2 are not equal")


'''Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings

'''
count=0
words=["Apple","Banana","pears","GrapeG","hellh"]

for i in words:
  if len(i)>0 and i[0]==i[-1]:
      count=count+1
  

print(count)

#Write a Python program to remove duplicates from a list.


'''
Write a Python function that takes two lists and returns true if they have
at least one common member.'''

