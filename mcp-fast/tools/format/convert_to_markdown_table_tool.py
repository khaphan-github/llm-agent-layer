import pytablewriter
from core.tool_config import ToolConfig


def convert_to_markdown_table(headers: list, data: list) -> str:
    """
    Convert data into a Markdown table.
    """
    writer = pytablewriter.MarkdownTableWriter()
    writer.headers = headers
    writer.value_matrix = data
    return writer.dumps()


CONVERT_TO_MARKDOWN_TABLE_TOOL = ToolConfig(
    description="""
    usecase:
        Convert tabular data into a Markdown-formatted table.
        Useful for generating Markdown tables for documentation or reports.
    rules:
        Ensure that the number of headers matches the number of columns in the data.
        Data should be structured as a list of rows, where each row is a list of values corresponding to the headers.
    parameters:
    - headers: list: A list of column headers for the table.
    - data: list: A list of rows, where each row is a list of values corresponding to the headers.
    """,
    name="convert_to_markdown_table",
    fn=convert_to_markdown_table,
)
