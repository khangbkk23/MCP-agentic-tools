import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server

app =Server(name="agentic-mcp-server", version="1.0.0")

@app.tool()
async def calculate_basic_math(operation: str, a: float, b: float) -> float:
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            raise ValueError("Math error: Cannot divide for zero")
        return a/b
    else:
        raise ValueError(f"Syntax error: {operation} is not supported.")
    
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