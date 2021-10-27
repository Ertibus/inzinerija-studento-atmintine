from program.repo.database import Repository

class NewRepository(Repository):

    @classmethod
    def add_event(cls, title: str, description: str, deadline: str):
        if not title or title.isspace() or not deadline or deadline.isspace():
            raise ValueError("Invalid input")

        cls.commit_query("INSERT INTO Event (title, description, deadline) VALUES (:title, :description, :deadline)", {
            "title": title,
            "description": description,
            "deadline": deadline,
        })

    @classmethod
    def update_event(cls, id: int, new_title: str, new_description: str, new_deadline: str):
        if not new_title or new_title.isspace() or not new_deadline or new_deadline.isspace():
            raise ValueError("Invalid input")
            
        cls.commit_query("UPDATE Event SET title = :title, description = :description, deadline = :deadline WHERE id = :id", {
            "title": new_title,
            "description": new_description,
            "deadline": new_deadline,
            "id": id
        })

    @classmethod
    def get_event_list(cls):
        ret = cls.get_list("SELECT * FROM Event")

        if not ret:
            raise ValueError("Not found")
        return ret
        
    @classmethod
    def delete_event(cls, id: int):
        cls.commit_query("DELETE FROM Event WHERE id = :id", {
            "id": id
        })

    @classmethod
    def add_user(cls, username: str, password: str):
        if not username or username.isspace() or not password or password.isspace():
            raise ValueError("Invalid input")
        
        cls.commit_query("INSERT INTO User (username, password) VALUES (:username, :password)", {
            "username": username,
            "password": password,
        })
    
    @classmethod
    def login(cls, username: str, password: str):
        if not username or username.isspace() or not password or password.isspace():
            raise ValueError("Invalid input")
        
        ret = cls.get_list("SELECT * FROM User WHERE username = :username AND password = :password", {
            "username": username,
            "password": password,
        })
        if not ret:
            raise ValueError("Invalid input")

    @classmethod
    def user_exists(cls):
        ret = cls.get_value("SELECT * FROM User")
        if not ret:
            return False
        else:
            return True

