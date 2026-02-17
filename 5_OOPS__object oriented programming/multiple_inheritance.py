
class Father:
    def skill(self):
        print("Father's skills : brave, singing")
class Mother:
    def skill(self):
        print("Mother's skills : bold, cooking")
class Child(Father, Mother):
    def skill(self):
        super().skill()
        print("Child skills ")
obj=Child()
obj.skill()

#have 2 parent -> 1 child -> output will load either of 1 parent

#single inheritance : 1 parent - 1 child
#multiple level inheritance : waterfall model a->b->c
#multiple inheritance : 2 parent - 1 child
#heirachy inheritance : type of inheritance having single parent & multiple children

#hybrid inheritance : single inheritance + multiple inheritance

