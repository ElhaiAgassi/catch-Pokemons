@authers Elhai Agassi & Ofek Avi Saadon & Barak sharbi
***
Wiki link Click [here](https://github.com/ElhaiAgassi/catch-Pokemons/wiki/)
# Pokemon Game
![alt](https://miro.medium.com/max/2800/0*ZLujw1b18CnMFxFa.jpg)

>The Pokemon game is part of a series of assignments related to graphs of an object-oriented course.
This game is based on all the assignment that preceded it as well as on algorithms in graph theory. This game is based on a client-server and simulates by collecting Pokemon the capabilities of algorithms like TSP, dijkstra, BFS ...
Also this game takes into account a limited amount of moves and therefore it is necessary to calculate distances in order to know how to perform a minimum amount of moves and keep passing in short lanes and of course collecting the highest value Pokemon.
Also this game includes several stages, a total of 16 stages and allows up to 3 agents collecting the Pokemon.
Here are some sample photos:

## Level 1
![alt](https://github.com/ElhaiAgassi/catch-Pokemons/blob/master/Pokemon_Game/media/level_1.png)
## Level 9
![alt](https://github.com/ElhaiAgassi/catch-Pokemons/blob/master/Pokemon_Game/media/level_9.png)
## Level 11
![alt](https://github.com/ElhaiAgassi/catch-Pokemons/blob/master/Pokemon_Game/media/level_11.png)
## Level 13
![alt](https://github.com/ElhaiAgassi/catch-Pokemons/blob/master/Pokemon_Game/media/level_13.png)
## Level 15
![alt](https://github.com/ElhaiAgassi/catch-Pokemons/blob/master/Pokemon_Game/media/level_15.png)
## Video Clip
![alt](https://github.com/ElhaiAgassi/catch-Pokemons/blob/master/Pokemon_Game/media/videoClip.gif)


# GUI
>The game interface is based on the game library PyGame which can be used to build multi-process games.
We have created a game with a spectacular graphic design, which allows the user to view the score obtained by collecting Pokemon as well as the amount of moves required for this.
Please note that this interface has the ability to zoom in and out without compromising the user experience, the interface is really responsive.
# Main_Pokemon
* 

# myGame
* function
>

# Objects
* Agent
>
* Nodes
>
* Pokemon
>
# Algo
>this is the core class of Graph design. it contains multiple algorithms based on well known Graph theory algorithms like Dijkstra DFS and many more, the main method of this class is to disassemble those algorithms to smaller function in way they can use each other's information and sync with each other, what make Graph Design better quicker and simpler. the whole class outputs is based on the same results format so each function can help multiple answers for different user requests. the main algorithms are:

## Dijakstra:
>Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks. It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later. [4] [5] [6]

>The algorithm exists in many variants. Dijkstra's original algorithm found the shortest path between two given nodes, [6] but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.

>For a given source node in the graph, the algorithm finds the shortest path between that node and every other. [7]: 196–206 It can also be used for finding the shortest paths from a single node to a single destination node by stopping the algorithm once the shortest path to the destination node has been determined. For example, if the nodes of the graph represent cities and edge path costs represent driving distances between pairs of cities connected by a direct road (for simplicity, ignore red lights, stop signs, toll roads and other obstructions), Dijkstra's algorithm can be used to find the shortest route between one city and all other cities. A widely used application of shortest path algorithms is network routing protocols, most notably IS-IS (Intermediate System to Intermediate System) and Open Shortest Path First (OSPF). It is also employed as a subroutine in other algorithms such as Johnson's.

## TSP:
>The travelling salesman problem (also called the travelling salesperson problem or TSP) asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?" It is an NP-hard problem in combinatorial optimization, important in theoretical computer science and operations research.

>The travelling purchaser problem and the vehicle routing problem are both generalizations of TSP.

>In the theory of computational complexity, the decision version of the TSP (where given a length L, the task is to decide whether the graph has a tour of at most L) belongs to the class of NP-complete problems. Thus, it is possible that the worst-case running time for any algorithm for the TSP increases superpolynomially (but no more than exponentially) with the number of cities.


# UML
![alt](https://www.plantuml.com/plantuml/png/TLHDJnmz3BxFhzZZ-whYKCvL1HGLKQdLIhJdo2Hc9yma6JcPBLlWlzTnilF1qilQZ-tOZpzcBs82IgFh6zr3Z9jhUqCmjC_DsSO7Wv4bcfr8fviFcxsAzW_-zp-hEAixJ0hwNkq5PSrw9UzKU50vqUG8OphrI0AdIv0n4Z21AOZGXJsUu19SadoBmKi339KY74WfzhqsjJtnNVQxa1lSPS3IsCSk9W9MhN-GbzRRfDH4JI85zG6CUg3Wr2EN4bC49f72mj06IXYJ6Y2LLxf5tLc_KoJmvzsscD4df6smFWbUCvusKjXbnf7qWhVJXJ7_4jEAB0SOihW-QI9y3NHRgeo3WSHa1EIOs4AQnhqzSaujtZdU63Uock2lsyp4yOAVgZna2K-2MGeUUZWWiN8FkjjH6BrXi0qTtdDELYzZcmss0zsEh7rfWHnuWvGdgA4lZDn1pS0G_EOKO4QAaq7slu2mGvzcE7195_mYG8w6PsXmjbsDAHs3QFJBXhy3jxWjMPxPdPTwNhDMYXc9UeKnNKxr7IJT2e7pcPIuurKWDAMyZGcyncL9TxW1XtdCqxqUTPR7ZbW5IVPssQBAZKQaFP8O-HLJYQkQF_8NNezymLlt29GxNjqX1mkb3cM_8TSFO-BVM_-FhwqopQyC962nXtv4bkamu9IbN3LJuMHvuJhF3UbjMxFd8-FtAyf0SZrhvchh0d50D5Fj-q0LTUjwx-U_au4-lrQeUylr61RxvjFBsTdBvsfkYX3ZOf5Bw_AscYca-Ee_yLjpkOtJuFeNrjHdOfQTDUL5CSXyLfQXLbzIAHx-qfiBz6Pq_Ly0)

# UnitTesting
>A unit test is a way of testing a unit - the smallest piece of code that can be logically isolated in a system. In most programming languages, that is a function, a subroutine, a method or property. ... Modern versions of unit testing can be found in frameworks like JUnit, or testing tools like TestComplete.

* TestDiGraph
 >In testing this unit we would like to check if each of the functions in the above class is indeed working as expected
 
* Example:
 ```py
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.graph = DiGraph()
        for id in range(4):
            self.graph.add_node(id)

    def test_v_size(self):
        print("\nTest v_size")
        print("----------------------------")
        self.assertEqual(self.graph.v_size(), 4)
        self.graph.add_node(6)
        self.assertEqual(self.graph.v_size(), 5)
 ```   
>In this example we build a graph with 4 codes and perform a test on the function v_size() and expect to get truth that the function has indeed returned the expected value

>We will then get another vertex and perform the test again, which means that now the function will return true if the entered vertex increased the number of vertices in the graph



## How to run
```bash
# Clone the repository
$ git clone https://github.com/ElhaiAgassi/catch-Pokemons.git
# Go into the repository
$ cd catch-Pokemons/Pokemon_Game
# Open the terminal on Windows
$ Run "py ./Main_Pokemon.py <number graph> [0-15]"
# Open the terminal on Linux
$ Run "python3 ./Main_Pokemon.py 0"
```
* example for graph number 0
```bash
$ Run "py ./Main_Pokemon.py 0"
```

## PyCharm 
***
![alt](https://github.com/ElhaiAgassi/catch-Pokemons/blob/master/Pokemon_Game/media/HowToRun.png)
