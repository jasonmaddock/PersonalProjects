import pytest

from merge_two_sorted_lists import Solution

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_list_destructor(list):
    decon_list = []
    while list is not None:
        decon_list.append(list.val)
        list = list.next
    return decon_list


def linked_list_constructor(list):
    if len(list) > 1:
        return ListNode(list[0], linked_list_constructor(list[1:]))
    elif len(list) == 1:
        return ListNode(list[0])
    else:
        return []


@pytest.mark.parametrize(
    "lists, expected_result",
    [
        (
            [[1,2,4],[1,3,4]],
            [1,1,2,3,4,4],
        ),
        (
            [[],[]],
            [],
        ),
        (
            [[0],[]],
            [0],
        )
    ]
)
def test(lists, expected_result):
    linked_lists = []
    for i in lists:
        linked_lists.append(linked_list_constructor(i))
    ln = Solution.mergeTwoLists(Solution, linked_lists[0], linked_lists[1])
    result = linked_list_destructor(ln)
    assert result == expected_result
