A=[
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]

# list1=[]
# t_matrix = zip(*A)
# for row in t_matrix:
#     list1.append(list(row))
# print(list1)

# res = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


list2=[]
for j in range(len(A[0])):
    list1=[]
    for i in range(len(A)):
        list1.append(A[i][j])    
    list2.append(list1)
print(list2)




