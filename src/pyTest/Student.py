
class Student:

    def __init__(self ,id ,name):
        self._id = id
        self._name = name
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_id(self ,value):
        self._id = value

    def set_name(self ,value):
        self._name = value

    def __eq__(self, other):
        if self.__class__== other.__class__:
            if self._id == other._id and self._name == other._name:
                return True

        return False


