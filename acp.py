
class FriendNetwork:
    def __init__(self):
        self.people = set()
        self.friends = {}

    def add_person(self, name):
        self.people.add(name)

    def add_friendship(self, person1, person2):

        self.people.add(person1)
        self.people.add(person2)


        if person1 not in self.friends:
            self.friends[person1] = set()
        self.friends[person1].add(person2)


        if person2 not in self.friends:
            self.friends[person2] = set()
        self.friends[person2].add(person1)

    def get_friends(self, name):
        return sorted(self.friends.get(name, []))

    def count_friends(self, name):
        return len(self.get_friends(name))


network = FriendNetwork()

for name in ["Asha", "Ben", "Chen", "Dia"]:
    network.add_person(name)

network.add_friendship("Asha", "Ben")
network.add_friendship("Asha", "Chen")
network.add_friendship("Ben", "Chen")
network.add_friendship("Chen", "Dia")

print("===== FRIEND NETWORK =====")

for name in sorted(network.people):
    print(
        name,
        "->",
        network.get_friends(name),
        "| friend count:",
        network.count_friends(name)
    )