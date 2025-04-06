import os
import json
import pytest
from main import persist_and_sum, DATA_FILE

def setup_function():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

def test_persist_and_sum():
    assert persist_and_sum(3) == 3
    assert persist_and_sum(5) == 8
    assert persist_and_sum(-2) == 6

def teardown_function():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
