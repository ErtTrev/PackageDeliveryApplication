# Creates the PackageObject class to represent package objects. Stores attributes that correspond to a specific package that is identified with its package ID.
# Time Complexity: O(1)
# Space Complexity: O(1)
class PackageObject:
    def __init__(self, packageID, address, city, state, zipCode, deliveryDeadline, mass, specialNotes, status, timestamp):
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deliveryDeadline = deliveryDeadline
        self.mass = mass
        self.specialNotes = specialNotes
        self.status = status
        self.timestamp = timestamp

    def __str__(self):
        return ' | '.join(('{}: {}'.format(item, self.__dict__[item]) for item in self.__dict__))


    def __repr__(self):
        return str(self)