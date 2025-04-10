from mcp.server.fastmcp import FastMCP
from tools.tools_list import TOOLS_LIST

_mcp = FastMCP(name="my-mcp-ratio-server",
               instructions='''''')

for tool in TOOLS_LIST:
    _mcp.add_tool(
        fn=tool.tool_fn,
        name=tool.tool_name,
        description=tool.tool_description
    )
    print(tool.__repr__())
if __name__ == "__main__":
    _mcp.run(transport='sse')
