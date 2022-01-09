import json
import math
from Departments.Objects import *
from Departments.GraphAlgo import GraphAlgo


class myGame:
    def __init__(self,graphAlgo=GraphAlgo()) -> None:
        self.GraphAlgo =graphAlgo
        self.Graph = self.GraphAlgo.get_graph()
        self.pokemons = []
        self.agents = []
      
        
    def init_from_server(self, agents=None, pokemons=None) -> None:
        if pokemons is not None:
            self.pokemons.clear()
            my_pokemons = json.loads(pokemons)
            for i in my_pokemons['Pokemons']:
                p = pokemon(i['Pokemon'])
                self.pok_pos(p)
                self.pokemons.append(p)
        self.pokemons.sort(key=lambda x: x.value, reverse=True)
      
        if agents is not None:
            self.agents = []
            my_agents = json.loads(agents)
            for a in my_agents['Agents']:
                self.agents.append(agent(a['Agent']))
            



    def pok_pos(self, pok: pokemon) -> None:
        Epsilon = 0.0000000001
        for N1 in self.Graph.nodes:
            for N2 in self.Graph.nodes:
                dis1 = self.distanceNodes(self.Graph.nodes[N1], self.Graph.nodes[N2])
                dis2 = (self.distancePokNode(self.Graph.nodes[N1], pok) + self.distancePokNode(
                    self.Graph.nodes[N2], pok))
                if abs(dis1 - dis2) <= Epsilon:
                    if pok.type == -1:
                        pok.dest = min(N1, N2)
                        pok.src = max(N1, N2)
                    else:
                        pok.dest = max(N1, N2)
                        pok.src = min(N1, N2)
                    return

    def distanceNodes(self, node1: Node, node2: Node):
        return math.sqrt(pow(node1.pos[0] - node2.pos[0], 2) + pow(node1.pos[1] - node2.pos[1], 2))


    def distancePokNode(self, node1: Node, pok: pokemon):
        return math.sqrt(
            pow(node1.pos[0] - pok.pos[0], 2) + pow(node1.pos[1] - pok.pos[1], 2))

    def getAgent(self, id: int) -> agent:
        for a in self.agents:
            if a.id == id:
                return a

    def clearPoke(self, Agent_id : int):
        for p in self.pokemons:
            if p.my_catcher == Agent_id:
                p.my_catcher = None
                print("found and changed", p.src ,pokemon.my_catcher)
            

