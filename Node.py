import board as wrapper


class Node:


    def __init__(self, id, parent):
        if parent == True:
            self.id = id
            self.g = 0
            self.h = self.calculate_h()
            self.f = self.h + self.g
            self.parent = self
            self.children = []
        else:
            self.id = id
            self.parent = parent
            self.children = []

    def attach_and_eval(self, parent):
        self.h = self.calculate_h()
        self.g = parent.g + self.arc_cost(parent)
        self.f = self.h + self.g
        self.parent = parent
        parent.children.append(self)

    def generate_successors(self):
        successor_ids = wrapper.generate_successors(self.id)
        successors = []
        for id in successor_ids:
            successors.append(Node(id, self))
        return successors

    def calculate_h(self):
        return wrapper.calculate_h(self.id)

    def propagate_improvement(self):
        self.g = self.parent.g + self.arc_cost(self.parent)
        self.f = self.g + self.h
        if not self.children:
            return
        else:
            for child in self.children:
                arc_cost = self.arc_cost(child)
                child.propagate_improvement()

    def arc_cost(self, node):
        return wrapper.arc_cost(self, node)

    def is_solution(self):
        return wrapper.is_solution(self.id)
