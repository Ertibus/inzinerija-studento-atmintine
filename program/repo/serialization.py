import json
from program.repo.repository import NewRepository

class Serialization():
    @classmethod
    def import_data(cls, source: str):
        with open(source, 'r') as file:
            json_data = file.read()
            data = json.loads(json_data)

            for entry in data:
                NewRepository.add_event(entry['title'], entry['description'], entry['deadline'])

    @classmethod
    def export_data(cls, source: str, data: dict):
        with open(source, 'w') as file:
            json_data = json.dumps(data)
            file.write(json_data)
            print(json_data)
