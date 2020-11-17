from typing import List, Any
import sys

# lol python :)
sys.path.append("../..")
from common import BaseClient, sc_types, cs_types
from clients import ClientA, ClientB

# REGISTER YOUR CLIENT HERE
ALL_CLIENTS: List[Any] = [ClientA, ClientB]


class Server:
    def __init__(self):
        self.clients: List[BaseClient] = self._get_clients()

    async def call_func1(self):
        for c in self.clients:
            msg: sc_types.JustAServerMessageType = {
                "memes_int": 420,
                "memes_str": "memes"
            }
            rcv = await c.func1(msg)
            print(f"Server received {rcv} from {c.id}")

    
    async def call_func2(self):
        for c in self.clients:
            msg: sc_types.JustAnotherServerMessageType = {
                "more_memes_int": 420,
                "more_memes_float": 4.3
            }
            rcv = await c.func2(msg)
            print(f"Server received {rcv} from {c.id}")


    def _get_clients(self) -> List[BaseClient]:
        return [c() for c in ALL_CLIENTS]
    
