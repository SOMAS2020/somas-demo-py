# server to client types
from typing import TypedDict

class JustAServerMessageType(TypedDict):
    memes_int: int
    memes_str: str

class JustAnotherServerMessageType(TypedDict):
    more_memes_int: int
    more_memes_float: float

