
def findPeakElements( numbers ):
    # create an empty list called peaks that will hold the elements of the peak values
    peaks = []

    # for loop that goes from 0 to last element in numbers ?
    for i in range(0, len(numbers) ):
        firstIndex  = 0
        lastIndex   = len(numbers) - 1 # len(numbers) == size and we start at 0 so thats why we sub 1
        currElement = numbers[i]

        # if not at the end indices:
        if i != firstIndex and i != lastIndex:
            # if currelement is greater than neighbors
            if currElement > numbers[i-1] and currElement > numbers[i+1]:
                peaks.append(currElement)
                # add to peaks list
            # else i do not care

        #else this means at at the ends
        # ignore the points
    return peaks


print( findPeakElements([5, 10, 20, 15]) )              # [20]
print( findPeakElements([10, 20, 15, 2, 23, 90, 67]) )  # [20, 90]
