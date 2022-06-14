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
        self.bored = True
        self.pok=None

    def __repr__(self):
        return f"id -> {self.id} value -> {self.value} src -> {self.src} dest ->{self.dest} speed -> {self.speed} pos -> {self.pos}"


class pokemon:

    def __init__(self, data: dict):
        self.data=data
        self.value = data['value']
        self.type = int(data['type'])
        p = str(data['pos']).split(',')
        self.pos = []
        for i in p:
            self.pos.append(float(i))
        self.src = None
        self.dest = None
        self.my_catcher = None

    def __gt__(self,pok):
        return self.value>pok.value


    def my_catcher(self):
        if self.my_catcher:
            return self.my_catcher
        else:
            return - 1

    def __repr__(self) -> str:
        return f'value = {self.value}, 'f' type = {self.type}, 'f' pos = {self.pos}, 'f' src = {self.src},'f' dest = {self.dest}, 'f' my_catcher = {self.my_catcher}'


class Node:
    def __init__(self, key: int, pos: tuple) -> None:
        self.key = key
        self.pos = float(pos[0]),float(pos[1]),float(pos[2])
        self.out = {}
        self.In = {}

    def __repr__(self) -> str:
        return f'key = {self.key}, ' f'pos = {self.pos}'
