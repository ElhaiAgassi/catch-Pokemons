import subprocess
import sys

from GUI import *
import time
from GraphAlgo import GraphAlgo
from myGame import *
from Objects import *

"""sys.argv[1]"""
subprocess.Popen(['powershell.exe', f'java -jar Ex4_Server_v0.0.jar {13}'])

PORT = 6666
HOST = '127.0.0.1'

client = Client()
client.start_connection(HOST, PORT)
for NA in range(int(json.loads(client.get_info())["GameServer"]["agents"])):
    client.add_agent("{\"id\":" + str(NA) + "}")

myGame = myGame()
client.start()
myGame.init_from_server(client.get_graph(), client.get_agents(), client.get_pokemons())
animation = GUI(myGame)
algoGraph = GraphAlgo(myGame.Graph)

""" run and init my game """


def path2pokemon(agent: agent, pok: pokemon):
    shorter = algoGraph.shortest_path(agent.src, pok.src)
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


def match_poke2agent():
    for agent in myGame.agents:
        minimal_value = float('inf')
        best_pok = None
        for pokemon in myGame.pokemons:
            if pokemon.my_catcher is not None: continue
            pokVal = pokemon.value
            pokWeight = algoGraph.shortest_path(agent.src, pokemon.src)[0]
            if ((pokWeight/pokVal) < minimal_value):
                best_pok = pokemon.myIndex
                minimal_value = pokWeight/pokVal

        agent.bored = False
        myGame.clearPoke(agent.id)
        myGame.getPoke(best_pok).my_catcher = agent.id
        agent.assign = best_pok
    for a in myGame.agents:
        print(a.id, a.assign)


def AgentsBored():
    for agent in myGame.agents:
        if agent.bored == True:
            return True
    return False


if __name__ == '__main__':
    while (client.is_running()):
        myGame.init_from_server(graph=client.get_graph(), agents=client.get_agents(), pokemons=client.get_pokemons())
        animation.run(client)

        # while AgentsBored() == True:
        match_poke2agent()
        for agent in myGame.agents:
            next_node = None
            path = path2pokemon(agent, myGame.getPoke(agent.assign))
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
        print(client.get_info())

        time.sleep(0.048)
        client.move()
