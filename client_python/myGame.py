import json
import math
from Objects import *
from DiGraph import DiGraph


class myGame:
    def __init__(self) -> None:
        self.Graph = DiGraph()
        self.pokemons = []
        self.agents = []

    def init_from_server(self, graph=None, agents=None, pokemons=None) -> None:
        if graph is not None:
            mygraph = json.loads(graph)
            for node in mygraph["Nodes"]:
                if "pos" in node:
                    data = node["pos"].split(',')
                    self.Graph.add_node(node["id"], (float(data[0]), float(data[1]), float(data[2])))
            for e in mygraph["Edges"]:
                self.Graph.add_edge(int(e["src"]), int(e["dest"]), float(e["w"]))

        if agents is not None:
            self.agents = []
            self.goToList = ()
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
            index = 0
            my_pokemons = json.loads(pokemons)
            for i in my_pokemons['Pokemons']:
                p = pokemon(i['Pokemon'])
                p.myIndex = index
                index += 1
                self.pok_pos(p)
                self.pokemons.append(p)

            # "Pokemon": {
            #     "value": 5.0,
            #     "type": -1,
            #     "pos": "35.197656770719604,32.10191878639921,0.0"
            # }

    def pok_pos(self, pok: pokemon) -> None:
        Epsilon = 0.0000000001
        for N1 in self.Graph.nodes:
            for N2 in self.Graph.nodes:
                dis1 = self.distanceNodes(self.Graph.nodes[N1], self.Graph.nodes[N2])
                dis2 = (self.distancePokNode(self.Graph.nodes[N1], pok) + self.distancePokNode(
                    self.Graph.nodes[N2], pok))
                if abs(dis1 - dis2) <= Epsilon:
                    src = None
                    dest = None
                    if pok.type == -1:
                        pok.dest = min(N1, N2)
                        pok.src = max(N1, N2)
                    else:
                        pok.dest = max(N1, N2)
                        pok.src = min(N1, N2)
                    return

    def distanceNodes(self, node1: Node, node2: Node):
        return math.sqrt(
            pow(float(node1.pos[0]) - float(node2.pos[0]), 2) + pow(float(node1.pos[1]) - float(node2.pos[1]), 2))

    def distancePokNode(self, node1: Node, pok: pokemon):
        return math.sqrt(
            pow(node1.pos[0] - pok.pos[0], 2) + pow(node1.pos[1] - pok.pos[1], 2))

    def getAgent(self, id: int) -> agent:
        for a in self.agents:
            if a.id == id:
                return a

    def clearPoke(self, Agent_id: int):
        for p in self.pokemons:
            if p.my_catcher == Agent_id:
                p.my_catcher = None
                print("found and changed", p.src, pokemon.my_catcher)

    def getPoke (self, pok_id : int):
        for p in self.pokemons:
            if p.myIndex == pok_id:
                return p
        return None



