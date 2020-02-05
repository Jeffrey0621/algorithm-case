#冒泡排序
#所有从第一个数开始往后比较，如果前一个数比后一个数大，则交换
#然后去掉最后一个数，从第一个继续开始重复以上比较，最大的数在最后
def bubbleSort(array):
    length = len(array)
    for i in range(length):
        for j in range(length-1-i):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1] , array[j]
    return array

#选择排序
#从第一个数开始，设定当前数的下标为最小值下标，往后比较，若遇到更小的，
#则更新最小值下标，遍历一遍后第一个数和最小数互换，再从第二个数开始比较
def selectSort(array):
    length = len(array)
    for i in range(length):
        minindex = i
        for j in range(i+1,length):
            if array[minindex] > array[j]:
                minindex = j
        array[i],array[minindex] = array[minindex],array[i]
    return array

#插入排序
#从第二个数开始，当前数和已经排过序的数组进行比较，从后往前遍历，
#若当前数更小，则互换位置
def insertSort(array):
    length = len(array)
    for i in range(length-1):
        for j in range(i+1,0,-1):
            if array[j-1]>array[j]:
                array[j-1],array[j] = array[j],array[j-1]
    return array

#希尔排序
#定义初始步长，按照步长进行插入排序，python3中除法会生成float，需要转int
def shellSort(array):
    length = len(array)
    gap = int(length/2)
    while gap > 0:
        for i in range(gap,length):
            preindex = i
            current = array[preindex]
            while preindex >= gap and array[preindex-gap] > current:
                array[preindex-gap],array[preindex] = array[preindex],array[preindex-gap]
                preindex -= gap
        gap = int(gap/2)
    return array

#归并排序
def mergeSort(array):
    length = len(array)
    if length <= 1:
        return array
    middle = int(length/2)
    left = mergeSort(array[:middle])
    right = mergeSort(array[middle:])
    return merge(left,right)

def merge(left,right):
    result = []
    leftindex = 0
    rightindex = 0
    while leftindex <len(left) and rightindex < len(right):
        if left[leftindex] < right[rightindex]:
            result.append(left[leftindex])
            leftindex += 1
        else:
            result.append(right[rightindex])
            rightindex += 1
    if leftindex == len(left):
        for h in right[rightindex:]:
            result.append(h)
    else:
        for h in left[leftindex:]:
            result.append(h)
    return result


#快速排序
#取一个key值，比key值大的放右边，小的放左边，对左右两边再进行快速排序
def quickSort(array):
    length = len(array)
    if length < 2:
        return array
    mid = array[int(length/2)]
    array.remove(mid)
    left = []
    right = []
    for item in array:
        if item < mid:
            left.append(item)
        else:
            right.append(item)
    return quickSort(left)+[mid]+quickSort(right)
        

if __name__ == "__main__":
    array = [3,1,4,2]
    print(bubbleSort(array))
    array = [3,1,4,2]
    print(selectSort(array))
    array = [3,1,4,2]
    print(insertSort(array))
    array = [3,1,4,2]
    print(shellSort(array))
    array = [3,1,4,2]
    print(mergeSort(array))
    array = [6,9,7,3,1,4,2]
    print(quickSort(array))
