def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        # Just use the + operator to join lists
        return sort(less) + equal + sort(greater)
    # Note that you want equal ^^^^^ not pivot
    # You need to hande the part at the end of the recursion - when you only
    # have one element in your array, just return the array.
    else:
        return array

array = [12, 4, 5, 6, 7, 3, 1, 15]

print(array)

print(sort(array))
