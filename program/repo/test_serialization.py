import pytest
import os
from program.repo import NewRepository
from program.repo import Serialization

@pytest.fixture()
def test_setup():
    NewRepository.connect(":memory:")
    yield

def test_serialization(test_setup):
    # Export
    data = []
    count = len(NewRepository.get_event_list())
    data.append({"title": "Title", "description": "Description", "deadline": "9999-09-09"})
    Serialization.export_data("./Test.json", data)
    Serialization.import_data("./Test.json")

    assert(len(NewRepository.get_event_list()) == count + 1)
