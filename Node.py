from board import Board

class Node():
    h = 0
    g = 0
    f = 0
    wrapper = Board()
    id = "todo"

    parent = "some node"
    children = []

    def attach_and_eval(self, parent):
        h = self.calculate_h()
        g = parent.g + self.arc_cost(parent)
        f = h + g
        self.parent = parent
        parent.children.insert(self)

    def generate_successors(self):
        # todo
        return successors

    def calculate_h(self, node):
        # TODO
        return distance_estimate

    def propagate_improvement(self):
        self.g = self.parent.g + self.arc_cost()
        self.f = self.g + self.h
        if not node.children:
            return
        else:
            for child in self.children:
                arc_cost = self.arc_cost(child)
                self.propagate_improvement(child, arc_cost)

    def arc_cost(self, node):
        return 1

    def is_solution(self):
        return wrapper_class.is_solution