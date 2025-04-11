import json
import asyncio


async def process_tool_calls_loop(session, tool_calls):
    async def handle_tool_call(tool_call):
        print(f"Processing tool call: {tool_call}")
        tool_name = tool_call.function.name
        args_str = tool_call.function.arguments
        try:
            args = json.loads(args_str)
        except json.JSONDecodeError:
            args = {}
        try:
            tool_result = await session.call_tool(tool_name, args)
            print(f"MCP tool '{tool_name}' executed successfully.")
            if tool_result.isError:
                return {
                    "role": "assistant",
                    "tool_call_id": tool_call.id,
                    "content": str(tool_result.content),
                }
            else:
                return {
                    "role": "assistant",
                    "tool_call_id": tool_call.id,
                    "content": str(tool_result.content),
                }
        except Exception as e:
            return {
                "role": "assistant",
                "tool_call_id": tool_call.id,
                "content": str({"error": f"Tool execution failed: {type(e).__name__}: {e}"}),
            }

    tool_messages = await asyncio.gather(
        *[handle_tool_call(tool_call) for tool_call in tool_calls]
    )
    return tool_messages
