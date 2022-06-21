"""Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8"""

def row_sum_odd_numbers(n):
    def start_pos(n):
        if n == 1:
            return 1
        return start_pos(n-1)+2*(n-1)
    x = start_pos(n)
    nums = []
    for i in range(n):
        nums.append(x)
        x += 2
    return sum(nums)

print(row_sum_odd_numbers(3))
