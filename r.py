class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    def introduce(self):
        print("My name is: " + self.name)

class Person:
    def __init__(self, name, personality, isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
    
    def sit_down(self):
        self.isSitting = True
    def stand_up(self):
        self.isSitting = False    
    
r1 = Robot("Tom1", "White", 30)
r2 = Robot("Tom2", "Black", 40)

p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)

p1.robotOwned = r2
p2.robotOwned = r1

p1.robotOwned.introduce()

#List Comprehesions
x = [x**2 for x in range(6, 0, -1)]
print(x)

def end_other(a, b):
  s1 = a[-3:]
  s2 = b[-3:]
  print(s1)
  print(s2)
  return s1.lower() == s2.lower()

print(end_other('Hiabc', 'abc'))
