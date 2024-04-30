import pytest
from rozenka.components.pages import PythonPage

def test_simple_go_to_python_page(python_page: PythonPage):

    assert python_page.get_started_button.is_visible(), "Button is not visible"