import subprocess
from client import *
from GUI import GUI
from myGame import *

subprocess.Popen(['powershell.exe', f'java -jar Ex4_Server_v0.0.jar {0}'])


PORT = 6666
HOST = '127.0.0.1'

client = Client()
client.start_connection(HOST, PORT)
client.add_agent("{\"id\":0}")

myGame = myGame()
animation = GUI(myGame)
client.start()


""" run and init my game """
if __name__ == '__main__':
    while(client.is_running()):
        myGame.init_from_server(client.get_graph(),client.get_agents(),client.get_pokemons())
        info = client.get_info().split(",")
        move = info[2].split(":")[1]
        animation.run()
        for agent in myGame.agents:
            if agent.dest == -1:
                next_node = (agent.src - 1) % len(myGame.graph.nodes)
                client.choose_next_edge(
                    '{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_node) + '}')
                ttl = client.time_to_end()
                print(ttl, client.get_info())
        client.move()


