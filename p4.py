list1=[1, 2, 3, 4, 5,6]
print(list(map(lambda x:x+x,filter(lambda x: x%2==0, list1))))