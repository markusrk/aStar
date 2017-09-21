from Node import Node


class IdenticalSuccessorException(Exception):
    pass


class A():

    import sys

    sys.setrecursionlimit(1000000)

    closed = {}
    opened = []
    search_order = []
    all_nodes = {} #except root
    iw = None
    final_node = "not filled yet"
    no_of_moves = 0
    max_size_search_tree = 0

    def run(self,wrapper):
        # todo load code
        root_node = Node(wrapper.make_root_node(), True, wrapper)
        self.opened.append(root_node)
        self.all_nodes.update({root_node.id:root_node})

        while True:
            # check if open is empty and fail it it is.
            if not self.opened:
                print("open list is empty, failed to find a solution")
            else:

                # Sort opened list
                self.opened.sort(key=lambda x: x.f, reverse=False)

                # pop node from open and check if it is a solution
                current_node = self.opened.pop(0)
                self.closed.update({current_node.id:current_node})
                self.search_order.append(current_node.id)
                if current_node.is_solution():
                    self.final_node = current_node
                    break

                # generate and insert successors
                successors = current_node.generate_successors()
                for successor in successors:

                    # if successor does not exist, insert it in open and attach to parent
                    if successor.id not in self.all_nodes:
                        if successor == current_node:
                            print("we have trouble")
                            raise IdenticalSuccessorException
                        successor.attach_and_eval(current_node)
                        self.opened.append(successor)
                        self.all_nodes.update({successor.id:successor})

                    # if successor does exist, update distance and parent
                    else:
                        identical_node = self.find_identical(self,successor)
                        if identical_node == current_node: raise ChildProcessError
                        if identical_node.g < current_node.g + current_node.arc_cost(identical_node):
                            continue
                        else:
                            if identical_node.id == current_node.id:
                                print("we have trouble")
                            identical_node.attach_and_eval(current_node)
                            if identical_node.id in self.closed:
                                identical_node.propagate_improvement()

        print('we succeeded')
        list_of_nodes = []
        while self.final_node.parent and self.final_node != self.final_node.parent:
            list_of_nodes.append(self.final_node.id)
            self.final_node = self.final_node.parent
            self.no_of_moves += 1
        list_of_nodes.append(self.final_node.id)
        print('No of moves = ' + str(self.no_of_moves))
        print('No of nodes expanded = ' + str(len(self.closed)))
        print('No of nodes generated = ' + str(len(self.all_nodes)))
        return list_of_nodes, self.search_order


    def find_identical(self,node):
        return self.all_nodes[node.id]



