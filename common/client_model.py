from . import cs_types
from . import sc_types

class BaseClient():
    def __init__(self):
        self.id: str = "PLEASE REGISTER YOUR ID!"

    async def func1(self, x: sc_types.JustAServerMessageType) -> cs_types.JustAClientMessageType:
        raise NotImplementedError("Override this method!")

    async def func2(self, x: sc_types.JustAnotherServerMessageType) -> cs_types.JustAnotherClientMessageType:
        raise NotImplementedError("Override this method!")

    async def log(self, s: str):
        """
        Logger function to know who's naughty.
        Do not directly use `print`, and _please_ do not override this!
        """
        print(f"{self.id}: {s}")