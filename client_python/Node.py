class Node:
    def __init__(self,key:int,pos:tuple) -> None:
        self.key = key
        self.pos = pos
        self.out = {}
        self.In = {}

    def __repr__(self) -> str:
        return f'key = {self.key}, ' f'pos = {self.pos}'
