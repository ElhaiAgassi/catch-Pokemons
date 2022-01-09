import subprocess
import sys
from GUI import *
import time
from Departments.GraphAlgo import GraphAlgo
from Departments.myGame import *
from Departments.Objects import *
"""sys.argv[1]"""
subprocess.Popen(['powershell.exe', f'java -jar Ex4_Server_v0.0.jar {sys.argv[1]}'])

flag = True
PORT = 6666
HOST = '127.0.0.1'

client = Client()
client.start_connection(HOST, PORT)

algoGraph = GraphAlgo()

infoClient = json.loads(client.get_info())
graphFile = infoClient["GameServer"]["graph"]

algoGraph.load_from_json(graphFile)
myGame = myGame(algoGraph)
pokemons = client.get_pokemons()
pokemons_obj = json.loads(pokemons)

pokemons = []
for i in pokemons_obj['Pokemons']:
    p = pokemon(i['Pokemon'])
    myGame.pok_pos(p)
    pokemons.append(p)

# To sort the list in place...
pokemons.sort(key=lambda x: x.value, reverse=True)

numberAgent = int(infoClient["GameServer"]["agents"])

for i in range(numberAgent):
    client.add_agent("{\"id\":"+str(pokemons[i].src)+"}")

animation = GUI(myGame)
client.start()

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
    bestValue = float('-inf')
    best_agentID = None
    for agent in myGame.agents:
        if agent.bored == True:
            shortPath = algoGraph.shortest_path(agent.src, pokemon.src)
            # if pokemon.value > bestValue:
            #     bestValue = pokemon.value
            # else:
            #     continue
            if shortPath[0] < best or pokemon.value > bestValue:
                best = shortPath[0]
                bestValue = pokemon.value
                best_agentID = agent.id
    if best_agentID is not None:
        myGame.getAgent(best_agentID).bored = False
        pokemon.my_catcher = best_agentID


# def match_poke2agent():
#     pokemonValue=float("-inf")
#     for pokemon in myGame.pokemons:
#         for agent in myGame.agents:
#             if (pokemon.my_catcher != None):
#                 if agent.id == pokemon.my_catcher:
#                     continue
#                 shorter = algoGraph.shortest_path(agent.src, pokemon.src)
#                 # if agent.pok == None:
#                 if (shorter[0] < algoGraph.shortest_path(myGame.getAgent(pokemon.my_catcher).src, pokemon.src)[0] and pokemon.value>pokemonValue):
#                     pokemonValue=pokemon.value
#                     myGame.getAgent(pokemon.my_catcher).bored = True
#                     myGame.clearPoke(pokemon.my_catcher)
#                     agent.bored = False
#                     pokemon.my_catcher = agent.id
#                     agent.pok = pokemon
#                 # else:
#                 #     if (shorter[0] < algoGraph.shortest_path(myGame.getAgent(pokemon.my_catcher).src, pokemon.src)[0] and agent.pok.value <= pokemon.value):
#                 #         myGame.getAgent(pokemon.my_catcher).bored = True
#                 #         myGame.clearPoke(pokemon.my_catcher)
#                 #         agent.bored = False
#                 #         pokemon.my_catcher = agent.id
#                 #         agent.pok = pokemon

#             else:
#                 BestAgent(pokemon)
#                 break

def match_poke2agent():
    pokemonValue = float("-inf")
    for agent in myGame.agents:
        for pokemon in myGame.pokemons:
            if (pokemon.my_catcher != None):
                if agent.id == pokemon.my_catcher:
                    continue
                shorter = algoGraph.shortest_path(agent.src, pokemon.src)
                # if agent.pok == None:
                if (shorter[0] < algoGraph.shortest_path(myGame.getAgent(pokemon.my_catcher).src, pokemon.src)[0] and pokemon.value > pokemonValue):
                    pokemonValue = pokemon.value
                    myGame.getAgent(pokemon.my_catcher).bored = True
                    myGame.clearPoke(pokemon.my_catcher)
                    agent.bored = False
                    pokemon.my_catcher = agent.id
                    agent.pok = pokemon
                else:
                    if (shorter[0] < algoGraph.shortest_path(myGame.getAgent(pokemon.my_catcher).src, pokemon.src)[0] and agent.pok.value <= pokemon.value):
                        myGame.getAgent(pokemon.my_catcher).bored = True
                        myGame.clearPoke(pokemon.my_catcher)
                        agent.bored = False
                        pokemon.my_catcher = agent.id
                        agent.pok = pokemon

            else:
                BestAgent(pokemon)
                break

def AgentsBored():
    for agent in myGame.agents:
        if agent.bored == True:
            return True
    return False


def distance(posSerc, posDest):
    return math.sqrt(
        pow(abs(posSerc[0] - posDest[0]), 2) + pow(abs(posSerc[1] - posDest[1]), 2))


if __name__ == '__main__':

    while client.is_running() == 'true':
        myGame.init_from_server(agents=client.get_agents(), pokemons=client.get_pokemons())
        animation.run(client)
        # while AgentsBored() == True:
        #     match_poke2agent()
        for agent in myGame.agents:
            if agent.dest == -1:
                continue
            for p in myGame.pokemons:
                if abs(agent.src - p.src) == 0:
                    destPos = myGame.Graph.nodes[agent.dest]
                    w = myGame.Graph.edges[(agent.src, agent.dest)]
                    a = distance(agent.pos, destPos.pos)
                    b = distance(p.pos, destPos.pos)
                    timeSleep = abs(a-b)*(w/a)
                    time.sleep((timeSleep/agent.speed))
                    client.move()
                    flag = not flag
                    
            if flag:
                timeSleep = myGame.Graph.edges[(agent.src, agent.dest)]
                time.sleep((timeSleep/agent.speed)/5)
                client.move()
            flag = True
        myGame.init_from_server(
            agents=client.get_agents(), pokemons=client.get_pokemons())
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




