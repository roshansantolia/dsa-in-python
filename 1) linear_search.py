# TC = O(n) SC = O(n)
def linear_search(list,query):
    for items in range(len(list)):
        if (list[items] == query):
            return items
    else:
        return -1

answer = linear_search([2,4,1,6,9,3,5],1)
if (answer == -1):
    print("Query Not Found")
else:
    print("Query Found at position: {}".format(answer + 1))