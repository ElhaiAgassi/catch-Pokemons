import random
from .Objects import Node

class DiGraph():
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.mc = 0

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.edges)

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].In

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].out

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.nodes and id2 in self.nodes:
            self.edges[(id1, id2)] = weight
            self.nodes[id1].out[id2] = weight
            self.nodes[id2].In[id1] = weight
            self.mc += 1
        else:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        if pos!=None:

            self.nodes[node_id] = Node(node_id, pos)
            self.mc += 1
        else:
            self.nodes[node_id] = Node(node_id,(random.uniform(35.19,35.21),random.uniform(32.1031462,32.10314621),0.0))
            self.mc += 1

        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes:

            for d in self.nodes[node_id].out:
                self.edges.pop(node_id, d)
                self.nodes[d].In.pop(node_id)

            for s in self.nodes[node_id].In:
                self.edges.pop(s, node_id)
                self.nodes[s].out.pop(node_id)

            self.nodes.pop(node_id)
            self.mc += 1
            return True

        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.nodes and node_id2 in self.nodes:
            self.edges.pop(node_id1,node_id2)
            self.nodes[node_id1].out.pop(node_id2)
            self.nodes[node_id2].In.pop(node_id1)
            self.mc += 1
            return True
        return False

    def __repr__(self) -> str:
        return f'{self.nodes} ' f'{self.edges}'