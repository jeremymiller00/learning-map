import pytest
from src.learningmap.crud import *

def test_add():
    assert add(3,4) == 7 
