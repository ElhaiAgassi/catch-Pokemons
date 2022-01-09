import os
import unittest
from Pokemon_Game.Departments.DiGraph import DiGraph
from Pokemon_Game.Departments.GraphAlgo import GraphAlgo
from Pokemon_Game.Departments.myGame import myGame
from pygame import math


class TestDiGraph(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.graph = DiGraph()
        self.graphA = GraphAlgo()

        for n in range(4):
            self.graph.add_node(n)
        print(self.graph)

    def test_v_size(self):
        graph = self.graph
        self.assertEqual(4, graph.v_size())
        graph.add_node(5)
        self.assertEqual(5, graph.v_size())
        graph.add_node(5)
        self.assertEqual(5, graph.v_size())
        graph.add_node(6)
        self.assertEqual(6, graph.v_size())
        graph.add_node(7)
        self.assertEqual(7, graph.v_size())
        graph.add_node(8)
        self.assertEqual(8, graph.v_size())
        graph.add_node(9)
        self.assertEqual(9, graph.v_size())

    def test_add_edge(self):
        graph = self.graph
        graph.add_edge(0, 1, 5)
        self.assertTrue(self.graph.e_size(), 5)
        graph.add_edge(0, 2, 4)
        self.assertEqual(self.graph.get_w(), 4)

    def test_remove_edge(self):
        graph = self.graph
        graph.add_edge(1, 2, 4)
        graph.add_edge(2, 2, 4)
        graph.add_edge(3, 2, 4)
        self.assertEqual(True, graph.remove_edge(3, 2))
        # self.assertEqual(False, graph.remove_edge(3, 2)) -->False
        self.assertEqual(True, graph.remove_edge(1, 2))
        self.assertEqual(True, graph.remove_edge(2, 2))

    def test_add_node(self):
        graph = self.graph
        graph.add_node(0, ["35.19805902663438,32.10525428067227,0.0"])
        graph.add_node(0, ["35.19805902663438,32.10525428067227,0.0"])

        self.assertTrue(graph.get_node, "35.19805902663438,32.10525428067227,0.0")

    def test_load_from_json(self):
        graphAlgo = GraphAlgo()
        self.assertTrue(graphAlgo.load_from_json(
            r"C:\Users\97254\Desktop\catch-Pokemons-master\Pokemon_Game\data\test.json"))  # graph without pos

    def test_save_from_json(self):
        graphAlgo = GraphAlgo()
        graphAlgo.load_from_json(
            r"C:\Users\97254\Desktop\catch-Pokemons-master\Pokemon_Game\data\test.json")
        self.assertTrue(graphAlgo.save_to_json("temp.json"))
        os.remove("./temp.json")


class TestGraphAlgo(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.graphA = GraphAlgo()

    def test_shortest_path(self):
        graphAlgo = GraphAlgo()
        graphAlgo.graph.add_node(0)
        graphAlgo.graph.add_node(1)
        graphAlgo.graph.add_node(2)
        graphAlgo.graph.add_node(3)
        graphAlgo.graph.add_node(4)
        graphAlgo.graph.add_edge(0, 1, 1)
        graphAlgo.graph.add_edge(1, 2, 6)
        graphAlgo.graph.add_edge(2, 3, 4)
        graphAlgo.graph.add_edge(4, 5, 2)
        self.assertEqual(graphAlgo.shortest_path(0, 1), (1, [0, 1]))
        self.assertEqual(graphAlgo.shortest_path(0, 2), (7, [0, 1, 2]))
        self.assertEqual(graphAlgo.shortest_path(0, 3), (11, [0, 1, 2, 3]))
        graphAlgo.graph.remove_node(1)
        self.assertEqual(graphAlgo.shortest_path(0, 2), (float('inf'), []))
        self.assertEqual(graphAlgo.shortest_path(0, 3), (float('inf'), []))
        self.assertEqual(graphAlgo.shortest_path(0, 4), (float('inf'), []))

    def test_centerPoint(self):
        graphAlgo = GraphAlgo()
        graphAlgo.load_from_json(r"C:\Users\97254\Desktop\catch-Pokemons-master\Pokemon_Game\data\test.json")
        print(graphAlgo.centerPoint())
        self.assertEqual((6, 8.071366078651435), graphAlgo.centerPoint())

#
# class Test_myGame(unittest.TestCase):
#
#     def __init__(self, methodName: str = ...) -> None:
#         super().__init__(methodName=methodName)
#         self.p = myGame()

    # def test_distancePokNode(self):
    #     graphAlgo = GraphAlgo()
    #     graphAlgo.load_from_json(r"C:\Users\97254\Desktop\catch-Pokemons-master\Pokemon_Game\data\test.json")
    #     node1 = graphAlgo.graph.nodes[1]
    #     dpok = {"value": 5.0,
    #             "type": -1,
    #             "pos": "35.197656770719604,32.10191878639921,0.0"}
    #     pok = self.myGame.pokemon(dpok)
    #     dis = math.sqrt(
    #         pow(node1.location[0] - pok.pos[0], 2) + pow(node1.location[1] - pok.pos[1], 2))
    #     self.assertEqual(0.0056814757193696, dis)


if __name__ == '__main__':
    unittest.main()
