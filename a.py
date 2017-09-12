from Node import Node

class A():
    closed = {}
    opened = []
    all_states = {}
    iw = None


    def run(self,main_wrapper,instance_wrapper, initial_state):
        # todo load code
        self.opened.insert(Node(initial_state))

        #check if open is empty and fail it it is.
        if not self.opened:
            print("open list is empty, failed to find a solution")
        else:

            #pop node from open and check if it is a solution
            current_node = self.opened.pop(0)
            self.closed.add(current_node)
            if current_node.is_solution():
                self.success(current_node)

            #generate and insert successors
            successors = current_node.generate_successors
            for successor in successors:

                #if successor does not exist, insert it in open and attach to parent
                if successor not in self.opened and successor not in self.closed:
                    successor.attach_and_eval(current_node)
                    self.opened.insert(successor)

                #if successor does exist, update distance and parent
                else:
                    identical_node = self.find_identical(successor)
                    if identical_node.f < successor.f:
                        continue
                    else:
                        identical_node.attach_and_eval(current_node)
                        identical_node.f = successor.f
                        identical_node.parent = successor.parent
                        if identical_node in self.closed:
                            identical_node.propagate_improvement()



    def find_identical(self,node):
        #todo find identical node in opened or closed and return it
        return sibling



    def success(self):
        #todo signal that A* has found a solution and is ending
        # Make sure to break loop somehow


