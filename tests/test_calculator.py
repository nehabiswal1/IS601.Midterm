import os
import pandas as pd
import pytest
from Midterm. main import add_to_history, load_history, save_history, clear_history

# Test add_to_history
def test_add_to_history():
    history = pd.DataFrame(columns=["Operation", "Operands", "Result"])
    new_history = add_to_history("add", [2, 3], 5, history)
    assert len(new_history) == 1
    assert new_history.iloc[0]["Operation"] == "add"
    assert new_history.iloc[0]["Result"] == 5

# Test saving history
def test_save_history(tmpdir):
    history = pd.DataFrame({"Operation": ["add"], "Operands": [[2, 3]], "Result": [5]})
    filepath = os.path.join(tmpdir, 'test_history.csv')
    save_history(history, filename=filepath)
    assert os.path.exists(filepath)

# Test loading history
def test_load_history(tmpdir):
    filepath = os.path.join(tmpdir, 'test_history.csv')
    history = pd.DataFrame({"Operation": ["add"], "Operands": [[2, 3]], "Result": [5]})
    history.to_csv(filepath, index=False)
    loaded_history = load_history(filename=filepath)
    assert len(loaded_history) == 1
    assert loaded_history.iloc[0]["Operation"] == "add"

# Test clearing history
def test_clear_history():
    history = pd.DataFrame({"Operation": ["add"], "Operands": [[2, 3]], "Result": [5]})
    cleared_history = clear_history(history)
    assert len(cleared_history) == 0

