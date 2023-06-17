class BubbleSort:
    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(self.nums) - 1):
                if self.nums[i] > self.nums[i + 1]:
                    self.nums[i], self.nums[i + 1] = self.nums[i + 1], self.nums[i]
                    swapped = True

    def display(self):
        print(self.nums)


def main():
    random_list_of_nums = [5, 2, 1, 8, 4]
    bubble = BubbleSort(random_list_of_nums)
    bubble.sort()
    bubble.display()


if __name__ == "__main__":
    main()
