class Student:

    def __init__(self, student_id, name, age, department):
        self.id = student_id
        self.name = name
        self.age = age
        self.department = department
 
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "department": self.department
        }
    
    def __str__(self):
        return (
            "----------------------------\n"
            f"ID         : {self.id}\n"
            f"Name       : {self.name}\n"
            f"Age        : {self.age}\n"
            f"Department : {self.department}\n"
            "----------------------------"
    )

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["name"],
            data["age"],
            data["department"]
        )