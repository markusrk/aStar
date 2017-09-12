from Node import Node
import board as wrapper



class A():
    closed = {}
    opened = []
    all_nodes = {}
    iw = None

    def run(self):
        # todo load code
        root_node = Node(wrapper.load_file('easy-3.txt'), True)
        self.opened.append(root_node)
        self.all_nodes.update( {root_node.id:root_node})

        while True:
            # check if open is empty and fail it it is.
            if not self.opened:
                print("open list is empty, failed to find a solution")
            else:

                # pop node from open and check if it is a solution
                current_node = self.opened.pop(0)
                self.closed.update({current_node.id:current_node})
                if current_node.is_solution():
                    self.success(current_node)

                # generate and insert successors
                successors = current_node.generate_successors()
                for successor in successors:

                    # if successor does not exist, insert it in open and attach to parent
                    if successor not in self.opened and successor.id not in self.closed:
                        successor.attach_and_eval(current_node)
                        self.opened.append(successor)

                    # if successor does exist, update distance and parent
                    else:
                        identical_node = self.find_identical(successor)
                        if identical_node.f < successor.f:
                            continue
                        else:
                            identical_node.attach_and_eval(current_node)
                            identical_node.f = successor.f
                            identical_node.parent = successor.parent
                            if identical_node.id in self.closed:
                                identical_node.propagate_improvement()

    def find_identical(self,node):
        return self.all_nodes[node.id]

    def success(self, node):
        print("we succeeded")
        # todo signal that A* has found a solution and is ending
        # Make sure to break loop somehow


