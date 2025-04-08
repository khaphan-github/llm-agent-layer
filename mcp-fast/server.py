"""
A FastMCP server that provides tools for calculating dimensions based on aspect ratios.
This server specifically handles 16:9 aspect ratio calculations.
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-mcp-ratio-server")


@mcp.tool()
def get_height_for_16_9(width: float) -> float:
    """
    Get the height value for a given width using 16:9 aspect ratio.

    Args:
        width (float): The width value

    Returns:
        float: The calculated height value
    """
    return (width * 9) / 16


if __name__ == "__main__":
    mcp.run(transport='stdio')
