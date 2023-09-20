class Array:
    def removeDuplicates(self, array: list, crop: bool = False) -> None:
        '''Remove duplicates from a given array Without extra space'''
        if array is None:
            return None
        l = 0 
        for r in range(1, len(array)):
            if array[l] == array[r]:
                array[r] = 0
                continue
            else: # Removing duplicates
                l += 1 
                array[l] = array[r]
                # Set to Zeor in place of duplicates
                array[r] = 0
        # Return the croped array else original array
        return array[: l + 1] if crop else array

myArray = [0, 0, 1, 1, 1, 2, 9, 9, 10, 10, 11, 11, 11]
obj = Array()
obj.removeDuplicates(myArray)
print(myArray)