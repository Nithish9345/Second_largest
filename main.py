"""Finding Second max
   finding both max and second max
   by swaping each other"""


class Second_largest():
    @staticmethod
    def find_2ndlargest(array):

        max = float("-inf")
        sec_max = float("-inf")

        for i in array:
            if i > max:
                sec_max = max
                max = i
            if i > sec_max and max > i:
                sec_max = i

        if(sec_max != float("-inf") ):
            return sec_max
        else:
            return -1


result = Second_largest()
array = list(map(int, input().split()))
print(result.find_2ndlargest(array))

