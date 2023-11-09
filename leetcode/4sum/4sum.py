import itertools


def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    combinations = list(itertools.combinations(nums, 4))
    solutions = [tuple(sorted(i)) for i in combinations if sum(i) == target]
    solutions = list(dict.fromkeys(solutions))
    solutions = [list(i) for i in solutions]
    return solutions


tests = [
    [0, [1, 0, -1, 0, -2, 2]],
    [8, [2, 2, 2, 2, 2]],
    [4, [-5, 5, 4, -3, 0, 0, 4, -2]],
]

for i in tests:
    print(fourSum(i[1], i[0]))
