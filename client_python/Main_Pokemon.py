import subprocess
from GUI import *
import time
from GraphAlgo import GraphAlgo
from myGame import *
from Objects import *

subprocess.Popen(['powershell.exe', f'java -jar Ex4_Server_v0.0.jar {3}'])

PORT = 6666
HOST = '127.0.0.1'

client = Client()
client.start_connection(HOST, PORT)

client.add_agent("{\"id\":0}")
client.add_agent("{\"id\":5}")
client.add_agent("{\"id\":10}")
client.add_agent("{\"id\":12}")

myGame = myGame()
client.start()
myGame.init_from_server(client.get_graph(), client.get_agents(), client.get_pokemons())
animation = GUI(myGame)
algoGraph = GraphAlgo(myGame.Graph)

""" run and init my game """


def path2pokemon(id: int, pok: pokemon):
    shorter = algoGraph.shortest_path(myGame.getAgent(id).src, pok.src)
    path = shorter[1]
    path.append(pok.dest)
    return path


def mypoke(agent):
    for pok in myGame.pokemons:
        if pok.my_catcher == agent.id:
            return path2pokemon(agent.id, pok)

def BestAgent(pokemon: pokemon):
    best = float('inf')
    best_agentID = None
    for agent in myGame.agents:
        if agent.bored == True:
            shortPath = algoGraph.shortest_path(agent.src, pokemon.src)
            if shortPath[0] < best:
                best = shortPath[0]
                best_agentID = agent.id
    if best_agentID is not None:
        myGame.getAgent(best_agentID).bored = False
        pokemon.my_catcher = best_agentID
    else: print(pokemon)

def match_poke2agent():
    for pokemon in myGame.pokemons:
        for agent in myGame.agents:
            if (pokemon.my_catcher != None):
                if agent.id == pokemon.my_catcher: continue
                shorter = algoGraph.shortest_path(agent.src, pokemon.src)
                if (shorter[0] < algoGraph.shortest_path(myGame.getAgent(pokemon.my_catcher).src, pokemon.src)[0]):
                    myGame.getAgent(pokemon.my_catcher).bored = True
                    myGame.clearPoke(pokemon.my_catcher)
                    agent.bored = False
                    pokemon.my_catcher = agent.id

            else:
                BestAgent(pokemon)
                break


def AgentsBored():
    for agent in myGame.agents:
        if agent.bored == True:
            return True
    return False


if __name__ == '__main__':
    while (client.is_running()):
        myGame.init_from_server(graph=client.get_graph(), agents=client.get_agents(), pokemons=client.get_pokemons())
        animation.run(client)

        while AgentsBored() == True:
            match_poke2agent()
        for agent in myGame.agents:
            next_node = None
            path = mypoke(agent)
            if path == None:
                continue
            elif path == -1:
                next_node = path
            else:
                if (len(path) == 1):
                    next_node = path[0]
                else:
                    next_node = path[1]
                client.choose_next_edge(
                    '{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_node) + '}')
        # print(client.get_info())

        time.sleep(0.05)
        client.move()

