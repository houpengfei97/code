
def MidSearch(list1,target):
    listsort = sorted(list1)
    low = 0
    high = len(listsort)
    while (low < high):
        mid = int((low + high) / 2)
        if (listsort[mid] == target):
            return mid
        if (listsort[mid] > target):
            high = mid - 1
        else:
            low = mid + 1

    print('The data not exists')

if __name__ == '__main__':
    listtest = [1,4,5,2,55,43,65,22,12,3,7,0]
    print (MidSearch(listtest,0))