import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.task_manager import add_task, list_tasks, complete_task

TEST_FILE = "data/tasks.json"


def setup_function():
    # limpa o arquivo antes de cada teste
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_add_task():
    add_task("Estudar Python")
    tasks = list_tasks()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Estudar Python"


def test_empty_task():
    with pytest.raises(ValueError):
        add_task("")


def test_complete_task():
    add_task("Testar app")
    complete_task(0)
    tasks = list_tasks()
    assert tasks[0]["done"] is True
