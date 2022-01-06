import copy
import json
from typing import List

import matplotlib.pyplot as plt
from DiGraph import DiGraph


class GraphAlgo():
    def __init__(self,graph=DiGraph()) -> None:
        self.graph = graph
        self.dijkstra = dijkstra(graph)
        self.inf = float('inf')

    def get_graph(self) :
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            dict={}
            graph_res = self.graph
            with open(file_name,"r") as f:
                dict=json.load(f)

            for n in dict["Nodes"]:
                if "pos" in n:
                    data = n["pos"].split(',')
                    graph_res.add_node(n["id"],(data[0],data[1],data[2]))
                else:
                    graph_res.add_node(n["id"])

            for e in dict["Edges"]:
                graph_res.add_edge(e["src"],e["dest"],e["w"])

        except IOError as e:
            print(e)
            return False
        self.graph = graph_res
        return True



    def save_to_json(self, file_name: str) -> bool:
        graph_dict = {"Edges": [], "Nodes": []}
        for e in self.graph.edges:
            graph_dict["Edges"].append(
                {"src": e[0],"w": self.graph.edges[e],"dest": e[1]})
        for n in self.graph.nodes.values():
            id = n.key
            if(n.pos!=None):
                pos = f'{n.pos[0]},{n.pos[1]},{n.pos[2]}'
                graph_dict["Nodes"].append({"pos": pos, "id": id})
            else:
                graph_dict["Nodes"].append({"pos": None, "id": id})
        try:
            with open(file_name,"w") as f:
                json.dump(graph_dict, fp=f, indent=2, default=lambda o:o.__dict__)
        except IOError as e:
            print(e)
            return False
        return True


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        self.getdijk(id1)
        self.dijkstra.addPath(id2)
        start = self.dijkstra.D[id2]
        end = self.dijkstra.roads[id2]
        return (start,end)


    def TSP(self, node_lst: List[int]) -> (List[int], float):
        try:
            chosen,road = self.inf,[]
            for i in node_lst:
                self.getdijk(i)
                path = []
                new = self.checking_r(i,copy.deepcopy(node_lst), path)
                if new < chosen:
                    chosen,road = new,path
                else:
                    continue
            return (road,chosen)
        except:
            return ([],self.inf)


    def checking_r(self, a: int, b: list, c: list):
        c.append(a)
        b.remove(a)
        count = 0
        while len(b):
            low = self.inf
            for j in b:
                if self.dijkstra.D[j]< low:
                    low,ind = self.dijkstra.D[j],j
            count += low
            path,f = self.shortest_path(a, ind)[1],True
            for j in path:
                if not f:
                    c.append(j)
                else:
                    f = False
            a = ind
            self.getdijk(a)
            b.remove(ind)
        return count



    def centerPoint(self) -> (int, float):
        try:
            res = (0, self.inf)
            for i in self.graph.nodes:
                self.getdijk(i)
                rD = (i, max(self.dijkstra.D.values()))
                if res[1] > rD[1]:
                    res = rD
            return res
        except:
            return (0,self.inf)


    def __repr__(self) -> str:
        return f'{self.graph}'


    def getdijk(self, src: int) -> bool:
        if src == self.dijkstra.src and self.graph.mc == self.dijkstra.mc:
            return False
        else:
            self.dijkstra.src = src
            self.dijkstra.MC = self.graph.mc
            self.dijkstra.goForIt()
            return True

    def plot_graph(self) -> None:
        for node in self.graph.nodes.values():
            x = float(node.pos[0])
            y = float(node.pos[1])
            id = int(node.key)
            plt.plot(x, y, markersize=10, marker="o", color="pink")
            for edge in self.graph.all_out_edges_of_node(id):
                his_x = float(self.graph.nodes[edge].pos[0])
                his_y = float(self.graph.nodes[edge].pos[1])
                plt.annotate("", xy=(x, y), xytext=(his_x, his_y), arrowprops=dict(arrowstyle="<-"))
        plt.show()



class dijkstra:

    def __init__(self,graph):
        self.src = 0
        self.graph = graph
        self.mc = 0
        self.inf = float('inf')

    #hashmaps
        self.roads = {}
        self.paps = {}
        self.D = {}

    def goForIt(self):
        var = []
        self.initshate(self.paps, var)
        while len(var) != 0:
            small = self.theSmallest(var)
            if small == -self.inf:
                return
            for i in self.graph.all_out_edges_of_node(small):
                self.updating(small,i)


    def updating(self, s: int, d: int):
        updatedDistance = self.D[s] + self.graph.edges[(s, d)]
        if updatedDistance >= self.D[d]:
            return
        else:
            self.D[d] = updatedDistance
            self.paps[d] = s


    def initshate(self,fathers: dict, listPerNode: list):
        for i in self.graph.nodes.keys():
            if i != self.src:
                self.D[i] = self.inf
                fathers[i] = self.inf
                listPerNode.append(i)
                self.roads[i] = []
        fathers[self.src] = self.src
        self.D[self.src] = 0.0
        self.roads[self.src] = []
        listPerNode.append(self.src)


    def addPath(self, next: int):
        if len(self.roads[next]) != 0:
            return
        self.roads[next] = []
        if next == self.src:
            self.roads[next].append(next)
            return
        dad = self.paps[next]
        if dad == self.inf:
            return
        if dad in self.roads:
            self.addPath(dad)
        self.roads[next].extend(self.roads[dad])
        self.roads[next].append(next)


    def theSmallest(self, p: list) -> int:
        M = self.inf
        ans = -self.inf
        for i in p:
            if M > self.D[i]:
                ans = i
                M = self.D[i]
        if ans != -self.inf:
            p.remove(ans)
        return ans
