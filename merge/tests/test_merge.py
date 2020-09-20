from merge import __version__
from merge.merge_sort import printList,merge_sort

def test_version():
    assert __version__ == '0.1.0'

def test_merge_sort_1():
    arr = [8,4,23,42,16,15] 
    expected = arr
    merge_sort(arr)
    actual = printList(arr)
    assert expected == actual

def test_merge_sort_11():
    arr = [8,4,23,42,16,15] 
    expected = [4,8,15,16,23,42]
    merge_sort(arr)
    actual = printList(arr)
    assert expected == actual

def test_merge_sort_2():
    arr = [20,18,12,8,5,-2] 
    expected = arr
    merge_sort(arr)
    actual = printList(arr)
    assert expected == actual

def test_merge_sort_22():
    arr = [20,18,12,8,5,-2] 
    expected = [-2,5,8,12,18,20]
    merge_sort(arr)
    actual = printList(arr)
    assert expected == actual

def test_merge_sort_3():
    arr = [5,12,7,5,5,7]
    expected = arr
    merge_sort(arr)
    actual = printList(arr)
    assert expected == actual

def test_merge_sort_33():
    arr = [5,12,7,5,5,7]
    expected = [5,5,5,7,7,12]
    merge_sort(arr)
    actual = printList(arr)
    assert expected == actual

def test_merge_sort_4():
    arr = [2,3,5,7,13,11]
    expected = arr
    merge_sort(arr)
    actual = printList(arr)
    assert expected == actual

def test_merge_sort_4():
    arr = [2,3,5,7,13,11]
    expected = [2,3,5,7,11,13]
    merge_sort(arr)
    actual = printList(arr)
    assert expected == actual