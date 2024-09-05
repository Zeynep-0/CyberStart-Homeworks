import math

points=[(1,2),(3,5),(8,7),(4,6),(3,7),(5,4)]
def euclideanDistance(tuple1,tuple2):
    x_sum=(tuple1[0]-tuple2[0])**2
    y_sum=(tuple1[1]-tuple2[1])**2
    result=math.sqrt(x_sum+y_sum)
    return result
distances=[]
for i in range(len(points)):
    for j in range(i+1,len(points)):
        distances.append(euclideanDistance(points[i],points[j]))
            
print(min(distances))
