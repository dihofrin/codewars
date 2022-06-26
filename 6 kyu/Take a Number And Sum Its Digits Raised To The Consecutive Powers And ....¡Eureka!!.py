"""The next number in having this property is 135.

See this property again: 135 = 1^1 + 3^2 + 5^3

We need a function to collect these numbers, that may receive two integers a, b that defines the range [a, b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

Let's see some cases:

sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
If there are no numbers of this kind in the range [a, b] the function should output an empty list.

sum_dig_pow(90, 100) == []
Enjoy it!!"""

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    def test(x):
        sum = 0
        count = 1
        for i in str(x):
            sum += int(i) ** count
            count += 1
        return sum == x
    return [i for i in range(a, b+1) if test(i)]