import pytest


def test_simple_go3_to_python_page(python_page):

    assert python_page.get_started_button.is_visible(), "Button is not visible"


def test_second3_test(python_page):
    python_page.get_started_button.click()
    assert python_page.installation.is_visible(), "Installation is not sisible"


def test_thir3d_test(python_page):
    python_page.get_started_button.click()
    assert python_page.writing_tests.is_visible(), "Installation is not sisible"
