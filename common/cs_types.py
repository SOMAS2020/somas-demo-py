# client to server types
from typing import TypedDict, Tuple

class JustAClientMessageType(TypedDict):
    client_memes: Tuple[int, str]

class JustAnotherClientMessageType(TypedDict):
    client_memes: Tuple[int, float]
