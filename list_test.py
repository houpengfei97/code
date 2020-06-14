from collections import deque

#vect = [1,2,3,4,6]
##嵌套列表##
def Nest_list(listin,listin2,matrix):
    listtmp1 = [x*2 for x in listin]
    listtmp2 = [[x,x*3] for x in listin]
    listtmp3 = [2**x for x in listin if x>2]
    listtmp4 = [x+y for x in listin for y in listin2]
    matrix_list = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return  listtmp1,listtmp2,listtmp3,listtmp4,matrix_list
def main():
    vect = [1,2,3,4,6]
    vect2 = [3,1,20,-3,5]
    martixin = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
    ]
    listres = Nest_list(vect,vect2,martixin)
    for vec in listres:
        print (vec)
    queue = deque(["Eric","tom","Alin"])
    queue.append("Terry")
    queue.append("Gramd")
    queue.popleft()
    queue.popleft()
    print(queue)

if __name__ == '__main__':
    main()


