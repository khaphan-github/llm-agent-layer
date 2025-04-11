def map_tools_to_openai(tools):
    functions = []
    for tool in tools:
        properties = {
            key: {
                "type": value["type"],
                "description": value.get("title", "")
            } for key, value in tool.inputSchema.get("properties", {}).items()
        }
        function_schema = {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description.strip(),
                "parameters": {
                    "type": "object",
                    "properties": properties,
                    "required": tool.inputSchema.get("required", []),
                    "additionalProperties": False
                },
                "strict": True
            }
        }
        functions.append(function_schema)
    return functions
