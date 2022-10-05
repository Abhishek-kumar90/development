class source1:
    def source(self):
        print("source of power")

class source2:
    def source(self):
        print("source of power2")


class father(source1):
    def superpower(self):
        print("i have")

    def suit(self):
        print("i have a")

class mother(self):
    def superpower(self):
        print("i have mind")

    def suit(self):
        print("i have no")


class child1(father,mother):
    pass
class child2(father,mother):
    pass


