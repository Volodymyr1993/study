import pytest
import time


def test_simple(calendar):
    calendar.reload()
    calendar.franka_1_row.click()
    calendar.franka_2_row.click()
    time.sleep(10)
