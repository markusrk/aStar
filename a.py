from Node import Node
import board as wrapper



class A():
    closed = {}
    opened = []
    all_nodes = {} #except root
    iw = None
    final_node = "not filled yet"
    no_of_moves = 0
    max_size_search_tree = 0

    def run(self):
        # todo load code
        root_node = Node(wrapper.load_file('expert-2'
                                           '.txt'), True)
        self.opened.append(root_node)
        self.all_nodes.update({root_node.id:root_node})

        while True:
            # check if open is empty and fail it it is.
            if not self.opened:
                print("open list is empty, failed to find a solution")
            else:

                # pop node from open and check if it is a solution
                current_node = self.opened.pop(0)
                self.closed.update({current_node.id:current_node})
                if len(self.closed) > self.max_size_search_tree: self.max_size_search_tree = len(self.closed)
                if current_node.is_solution():
                    self.final_node = current_node
                    break

                # generate and insert successors
                successors = current_node.generate_successors()
                for successor in successors:

                    # if successor does not exist, insert it in open and attach to parent
                    if successor.id not in self.all_nodes:
                        if successor.id == current_node.id:
                            print("we have trouble")
                        successor.attach_and_eval(current_node)
                        self.opened.append(successor)
                        self.all_nodes.update({successor.id:successor})

                    # if successor does exist, update distance and parent
                    else:
                        identical_node = self.find_identical(self,successor)
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
        print('No of moves = ' + str(self.no_of_moves))
        print('max number of nodes = ' + str(self.max_size_search_tree))
        return list_of_nodes


    def find_identical(self,node):
        return self.all_nodes[node.id]



