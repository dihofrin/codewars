"""Build Tower
Build a pyramid-shaped tower given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ",
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ",
  "    ***    ",
  "   *****   ",
  "  *******  ",
  " ********* ",
  "***********"
]"""

def tower_builder(n_floors):
    tower = []
    block = '*' * (n_floors * 2 - 1)
    for i in range(1, n_floors+1):
        tower.append(block)
        spaces = ' ' * i
        block = spaces + '*' * (n_floors * 2 - (i * 2)-1) + spaces
    return tower[::-1]
