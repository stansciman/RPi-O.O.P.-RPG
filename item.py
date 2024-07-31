#items class generator
class Item:
    def __init__(self, item_name):
        self.name = item_name
        self.description = None
        self.value = 0

    #get description property
    @property
    def description(self):
        return self._description

    #set description property
    @description.setter
    def description(self, item_description):
        self._description = item_description

    #getters and setters for name variable; when I attempted to change to property, this caused recursion errors
    def set_name(self, item_name):
        self.name = item_name

    def get_name(self):
        return self.name

    #get value property
    @property
    def value(self):
        return self._value

    #set item value for sale back on earth
    @value.setter
    def value(self, item_value):
        self._value = item_value
