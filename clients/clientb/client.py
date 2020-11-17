import sys

# python mem
sys.path.append("../../..")
from common import BaseClient, sc_types, cs_types


class Client(BaseClient):
    def __init__(self):
        self.id = "B"

    async def func1(
        self,
        x: sc_types.JustAServerMessageType,
    ) -> cs_types.JustAClientMessageType:
        await self.log("func1 called")
        memes_int = x["memes_int"]
        memes_str = x["memes_str"]

        ret: cs_types.JustAClientMessageType = {"client_memes": (memes_int, memes_str)}
        return ret

    async def func2(
        self,
        x: sc_types.JustAnotherServerMessageType,
    ) -> cs_types.JustAnotherClientMessageType:
        await self.log("func2 called")

        more_memes_int = x["more_memes_int"]
        more_memes_float = x["more_memes_float"]

        ret: cs_types.JustAnotherClientMessageType = {
            "client_memes": (more_memes_int, more_memes_float)
        }
        return ret
