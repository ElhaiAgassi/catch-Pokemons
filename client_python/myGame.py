import json
import math

from diGraph import Node

import DiGraph
from DiGraph import DiGraph


class agent:
    def __init__(self, data: dict) -> None:
        self.id = int(data['id'])
        self.value = float(data['value'])
        self.src = int(data['src'])
        self.dest = int(data['dest'])
        self.speed = float(data['speed'])
        xyz = str(data['pos']).split(',')
        self.pos = []
        for n in xyz:
            self.pos.append(float(n))

        self.stations = []

    def __repr__(self) -> str:
        return f'{self.id} ' f'{self.value},' f'{self.src}' f'{self.dest}' f'{self.speed}' f'{self.pos}'


class pokemon:
    def __init__(self, data: dict) -> None:
        self.value = data['value']
        self.type = int(data['type'])
        p = str(data['pos']).split(',')
        self.pos = []
        for i in p:
            self.pos.append(float(i))
        self.src = None
        self.dest = None


class myGame:
    def __init__(self) -> None:
        self.graph = DiGraph()
        self.pokemons = []
        self.agents = []

    def init_from_server(self, graph=None, agents=None, pokemons=None) -> None:
        if graph is not None:
            mygraph = json.loads(graph)
            for n in mygraph["Nodes"]:
                if "pos" in n:
                    data = n["pos"].split(',')
                    self.graph.add_node(n["id"], (float(data[0]), float(data[1]), float(data[2])))

            for e in mygraph["Edges"]:
                self.graph.add_edge(int(e["src"]), int(e["dest"]), float(e["w"]))


        if agents is not None:
            self.agents = []
            my_agents = json.loads(agents)
            for a in my_agents['Agents']:
                self.agents.append(agent(a['Agent']))


            # "Agent":
            # {
            #     "id": 0,
            #     "value": 0.0,
            #     "src": 0,
            #     "dest": 1,
            #     "speed": 1.0,
            #     "pos": "35.18753053591606,32.10378225882353,0.0"
            # }

        if pokemons is not None:
            self.pokemons.clear()
            my_pokemons = json.loads(pokemons)
            for i in my_pokemons['Pokemons']:
                p = pokemon(i['Pokemon'])
                self.pok_pos(p)
                self.pokemons.append(p)

            print(self.pokemons)

            # "Pokemon": {
            #     "value": 5.0,
            #     "type": -1,
            #     "pos": "35.197656770719604,32.10191878639921,0.0"
            # }

    def pok_pos(self, poke: pokemon) -> None:
        Epsilon = 0.00000001
        for N1 in self.graph.nodes:
            for N2 in self.graph.nodes:
                nodes_dist = self.distanceNodes(self.graph.nodes[N1], self.graph.nodes[N2])
                pokemons_dist = (self.distancePokNode(self.graph.nodes[N1], poke) + self.distancePokNode(
                    self.graph.nodes[N2], poke))

                if (nodes_dist - pokemons_dist) <= Epsilon:
                    if poke.type == -1:
                        poke.src = min(N1, N2)
                        poke.dest = max(N1, N2)
                    else:
                        poke.src = max(N1, N2)
                        poke.dest = min(N1, N2)
                    return

    def distanceNodes(self, node1: Node, node2: Node):
        return math.sqrt(pow(float(node1.pos[0]) - float(node2.pos[0]), 2) + pow(float(node1.pos[1]) - float(node2.pos[1]), 2))


    def distancePokNode(self, node1: Node, pok: pokemon):
        return math.sqrt(
            pow(node1.pos[0]- pok.pos[0], 2) + pow(node1.pos[1] - pok.pos[1], 2))
