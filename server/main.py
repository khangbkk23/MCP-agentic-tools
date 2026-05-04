import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Nhập (Import) logic từ module tools
from tools.calculator import execute_basic_math

app = Server(name="agentic-mcp-server", version="1.0.0")

@app.tool()
async def calculate_basic_math(operation: str, a: float, b: float) -> float:
    return execute_basic_math(operation, a, b)

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stop server.")