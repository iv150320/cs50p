from seasons import date_diff_minutes
from datetime import date
import pytest


def test_one_year():
    d1 = date(2025, 5, 26)
    d2 = date(2026, 5, 26)
    assert date_diff_minutes(d1, d2) == 525600


def test_leap_year():
    d1 = date(2023, 3, 1)
    d2 = date(2024, 3, 1)
    assert date_diff_minutes(d1, d2) == 527040


def test_zero():
    today = date.today()
    assert date_diff_minutes(today, today) == 0
