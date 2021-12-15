import pytest
import os
from program.repo import NewRepository

@pytest.fixture()
def test_setup():
    NewRepository.connect(":memory:")
    yield

def test_add_event(test_setup):
    count = len(NewRepository.get_event_list())
    NewRepository.add_event("Title", "Description", "1999-99-99")
    assert(len(NewRepository.get_event_list()) == count + 1)


def test_update_event(test_setup):
    count = len(NewRepository.get_event_list())
    NewRepository.add_event("Title", "Description", "1000-99-99")
    assert(len(NewRepository.get_event_list()) == count + 1)
    id = NewRepository.get_event_list()[0][3]
    NewRepository.update_event(id, "NewTitle", "Desc", "1000-01-01")
    assert(len(NewRepository.get_event_list()) == count + 1)
    assert(NewRepository.get_event_list()[0][0] == "NewTitle")

def test_get_event_list(test_setup):
    assert(NewRepository.get_event_list() != None)

def test_get_recovery_info(test_setup):
    NewRepository.add_user("TestUser", "password", 0, "answer")
    assert(NewRepository.get_recovery_info()[1] == "answer")

def test_update_event(test_setup):
    count = len(NewRepository.get_event_list())
    NewRepository.add_event("Title", "Description", "1000-99-99")
    assert(len(NewRepository.get_event_list()) == count + 1)
    NewRepository.delete_event(1)
    assert(len(NewRepository.get_event_list()) == count)

def test_get_user(test_setup):
    NewRepository.add_user("TestGetUser", "password", 0, "answer")
    assert(NewRepository.user_exists())

def test_user_exists(test_setup):
    NewRepository.add_user("TestExistUser", "password", 0, "answer")
    assert(NewRepository.user_exists())

def test_login(test_setup):
    NewRepository.add_user("TestLoginUser", "password", 0, "answer")
    assert(NewRepository.login("TestLoginUser", "password") == None)
