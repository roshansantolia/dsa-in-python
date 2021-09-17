# TC= O(log(n)) SC =O(n) need a sorted list(ascd or desc)
def binary_search(list,query):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low+high)//2
        result= list[mid]
        if (result < query):
            low = mid + 1
        elif (result > query):
            high = mid - 1
        else:
            return mid
    return -1

answer = binary_search([12,24,32,39,45,50,54,60],45)
if (answer == -1):
    print("Query Not Found")
else:
    print("Query Found at position: {}".format(answer + 1))