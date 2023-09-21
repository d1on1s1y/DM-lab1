arr =  [1, 5, 23, 12, -6, 9, 14]
av_value = sum(arr)/len(arr)
#print (av_value)
i = 0
while i < len(arr):
    if(arr[i] > av_value):
        arr[i]-=18
    i+=1    
print("Новий массив ",arr) 