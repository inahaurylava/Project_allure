import pytest
from task_manager_project.app.task_manager import TaskManager
import allure

@pytest.fixture
def task_manager():
    return TaskManager()

@allure.feature("Add task in list")
def test_add_task(task_manager):
    task = task_manager.add_task("Do hometask", priority="high")
    assert task["name"] == "Do hometask"
    assert task["priority"] == "high"
    assert task["completed"] == False

@allure.story("Incorrect priority")
def test_add_task_invalid_priority(task_manager):
    with pytest.raises(ValueError, match="Приоритет должен быть 'low', 'normal' или 'high'"):
        task_manager.add_task("Write a list", priority="urgent")

@allure.feature("Return list of tasks")
def test_list_tasks(task_manager):
    task_manager.add_task("Do hometask", priority="high")
    tasks = task_manager.list_tasks()
    assert tasks

@allure.feature("Completed tasks")
def test_mark_task_completed(task_manager):
    task_manager.add_task("Read the book")
    updated_task = task_manager.mark_task_completed("Read the book")
    assert updated_task["name"] == "Read the book"
    assert updated_task["completed"] == True
    assert task_manager.tasks[0]["completed"] == True

@allure.story("Task doesn`t find")
def test_mark_task_completed_error(task_manager):
  with pytest.raises(ValueError, match="Задача с таким названием не найдена"):
        task_manager.mark_task_completed("Несуществующая задача")


@allure.step("Remove task")
def test_remove_task(task_manager):
    with allure.step("Add task"):
        pass
    task = task_manager.add_task("Task for Delete")
    with allure.step("Assert task"):
        pass
    assert task["name"] == "Task for Delete"
    with allure.step("Len task"):
        pass
    assert len(task_manager.tasks) == 1
    with allure.step("Remove task"):
        pass
    task = task_manager.remove_task("Task for Delete")
    with allure.step("Assert task"):
        pass
    assert task["name"] == "Task for Delete"
    with allure.step("Len task"):
        pass
    assert len(task_manager.tasks) == 0

@allure.step("Task doesn`t find" )
def test_remove_task_not_found(task_manager):
    with allure.step("ERROR: The task with name doesn`t find"):
        pass
    with pytest.raises(ValueError, match="Задача с таким названием не найдена"):
        task_manager.remove_task("Несуществующая задача")
    with allure.step("Len of tasks"):
        pass
    assert len(task_manager.tasks) == 0