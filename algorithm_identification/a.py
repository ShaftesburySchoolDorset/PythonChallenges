#
# 'S' recursive funtion that does a binary search
#
def S(A, value, low, high):
    if (high < low):
        return "Error"

    mid = int((low + high) / 2)

    if A[mid] > value:
        return S(A, value, low, mid-1)
    elif A[mid] < value:
        return S(A, value, mid+1, high)
    else:
        return mid

#
# Executing the search
#

# List of values to search
values = [1, 3, 5, 7, 9]
# Value to find
to_find = 9
# Do the find and save the result
result = S(values, to_find, 0, len(values) - 1)
# Output the index
print(result)
