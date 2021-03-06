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
    def get_recovery_info(cls):
        ret = cls.get_list("SELECT question_id, answer, password FROM User")
        return ret[0]

    @classmethod
    def get_event_list(cls):
        ret: list = cls.get_list("SELECT * FROM Event ORDER BY deadline ASC")

        return ret
        
    @classmethod
    def delete_event(cls, id: int):
        cls.commit_query("DELETE FROM Event WHERE id = :id", {
            "id": id
        })

    @classmethod
    def add_user(cls, username: str, password: str, question: int, answer: str):
        if not username or username.isspace() or not password or password.isspace() or not answer or answer.isspace():
            raise ValueError("Invalid input")
        
        cls.commit_query("INSERT INTO User (username, password, question_id, answer) VALUES (:username, :password, :question_id, :answer)", {
            "username": username,
            "password": password,
            "question_id": question,
            "answer": answer,
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

