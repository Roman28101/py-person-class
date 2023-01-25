class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))
    for person in people:
        if "wife" in person and person.get("wife") is not None:
            Person.people[person["name"]].wife = (
                Person.people[person["wife"]]
            )
        if "husband" in person and person.get("husband") is not None:
            Person.people[person["name"]].husband = (
                Person.people[person["husband"]]
            )
    return person_list
