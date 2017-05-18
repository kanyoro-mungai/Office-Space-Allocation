class Person(object):
    """docstring for Person"""

    def __init__(self, name, p_type):
        self.name = name
        self.p_type = p_type


class Fellow(Person):
    """docstring for Fellow"""

    def __init__(self, name, p_type="fellow", accomodation="n"):
        super(Fellow, self).__init__(name, p_type="fellow")


class Staff(Person):
    """docstring for Staff"""

    def __init__(self, name, p_type="staff"):
        super(Staff, self).__init__(name, p_type="staff")
