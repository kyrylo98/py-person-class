class Person:
    people = {}
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    my_list = []
    for married in people:
        name =married["name"]
        age = married["age"]
        person_instance = Person(name, age)
        my_list.append(person_instance)
    for married in people:
        person_current = Person.people[married["name"]]
        if "wife" in married and married["wife"] is not None:
            wife_name = married["wife"]
            if wife_name in Person.people:
                person_current.wife = Person.people[wife_name]
        if "husband" in married and married["husband"] is not None:
            husband_name = married["husband"]
            if husband_name in Person.people:
                person_current.husband = Person.people[husband_name]
    return my_list




