class ToolConfig:
    def __init__(self, name: str, description: str, fn: any):
        self.tool_name = name
        self.tool_description = description
        self.tool_fn = fn

    def __repr__(self):
        return f"ToolConfig(tool_name={self.tool_name}"
