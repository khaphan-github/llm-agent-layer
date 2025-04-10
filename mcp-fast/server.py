from mcp.server.fastmcp import FastMCP
from tools.tools_list import TOOLS_LIST
from multiprocessing import Process
from packages.scheduler.app import start_celery_worker

_mcp = FastMCP(instructions='''''')

for tool in TOOLS_LIST:
    _mcp.add_tool(
        fn=tool.tool_fn,
        name=tool.tool_name,
        description=tool.tool_description
    )
    print(tool.__repr__())


if __name__ == "__main__":
    # Let run celery at other process.
    celery_process = Process(target=start_celery_worker)
    celery_process.start()
    _mcp.run(transport='sse')
    celery_process.join()
