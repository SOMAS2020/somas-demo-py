import asyncio
from server import Server

async def main():
    server = Server()
    await server.call_func1()
    await server.call_func2()

if __name__ == "__main__":
    asyncio.run(main())