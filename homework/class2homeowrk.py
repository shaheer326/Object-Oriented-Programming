class DailyDataHelper:

    def __init__(self):
        print("session created")

    def __del__(self):
        print("session deleted")

    def twoSums(self, nums, target):

        lookup = {}

        for i, num in enumerate(nums):
            if target - num in lookup:
                return(lookup[target - num], i)

            lookup[num] = 1

value = int(input("Enter sum for which you want to make this search: "))
result = DailyDataHelper().twoSums((10, 20, 30, 40, 50, 60, 70), value)

if result is not None:
    print("index1=%d, index2=%d" % result)
else:
    print("No matching pair found for that sum.")