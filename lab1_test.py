"""test code for TIL Python programming jupyter notebook Lab 1 - Python Environment"""
import pytest
import inspect
from testbook import testbook


@pytest.fixture(scope='module')
def tb():
    with testbook('lab1_2025.ipynb', execute=True) as tb:
        yield tb
#Q1
def test_multiply(tb):
    multi = tb.ref("multiply")
    assert callable(multi)
    assert multi(2, 3) == 6

# Q2
def test_get_first_accepts_print_or_return(tb):
    get_first = tb.ref("get_first_item")
    # case: non-empty list
    result = get_first([1, 2, 3])
    assert result == 1
    # case: empty list -> printed message or returned message or None (but must not crash)
    result_empty = get_first([])
    empty_return = result_empty == "No items to display." or result_empty is None
    assert empty_return

# Q3
def test_schedule_tasks_outputs_and_returns_done(tb, capsys):
    schedule_tasks = tb.ref("schedule_tasks")
    # multiple tasks
    tasks = ["taskA", "taskB"]
    result = schedule_tasks(tasks)
    captured = capsys.readouterr()
    expected = "Scheduling task: taskA\nScheduling task: taskB\n"
    assert result == "Done"
    if captured.out:
        assert captured.out == expected

# additional check for single task printing behavior
def test_schedule_tasks_single_task_print(tb, capsys):
    schedule_tasks = tb.ref("schedule_tasks")
    result = schedule_tasks(["only"])
    captured = capsys.readouterr()
    assert result == "Done"
    if captured.out:
        assert captured.out == "Scheduling task: only\n"

# Q4

def test_add_positive_numbers(tb):
    add_positive_numbers = tb.ref("add_positive_numbers")
    assert callable(add_positive_numbers)
    assert add_positive_numbers([1, -2, 3, 4, -5]) == 8
    assert add_positive_numbers([-1, -2, -3]) == 0
    assert add_positive_numbers([]) == 0