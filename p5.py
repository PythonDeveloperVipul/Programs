import math
list1=[56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]

# res=[]
# for item in list1:
#     if math.isnan(item)==False:
#         res.append(item)
# print(res)

# it is practise code
a=10
ans=[item for item in list1 if math.isnan(item)==False]
print(ans)
