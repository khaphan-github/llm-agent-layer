import asyncio
from openai import AsyncOpenAI
from mcp import ClientSession
from mcp.client.sse import sse_client
from packages.mcp_client.open_ai_function_mapper import map_tools_to_openai
from packages.mcp_client.concurrent_tool_call import process_tool_calls_loop
from env import *

# Initialize OpenAI client
client = AsyncOpenAI(api_key=OPEN_API_KEY, base_url=OPENAI_API_BASE_URL)
sse = sse_client(MCP_SERVER_HOST)


def get_history(chat_id):
    return []


def set_history(chat_id, message):
    return []


async def agent_loop(chat_id: str, prompt: str, client: AsyncOpenAI, session: ClientSession, model: str = DEFAULT_MODEL):
    await session.initialize()
    mcp_tools = await session.list_tools()
    tools = map_tools_to_openai(mcp_tools.tools)
    messages = get_history(chat_id=chat_id)
    messages.append({"role": "user", "content": prompt})

    response = await client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    tool_calls = response.choices[0].message.tool_calls or []
    assistant_message_content = response.choices[0].message.content
    if len(tool_calls) == 0:
        assystant_mgs = {"role": "assistant",
                         "content": assistant_message_content}
        messages.append(assystant_mgs)
        set_history(chat_id, assystant_mgs)
        yield response.choices[0].message
        return

    tool_executed_message = await process_tool_calls_loop(session, tool_calls)
    messages.extend(tool_executed_message)
    for tool_message in tool_executed_message:
        set_history(chat_id, tool_message)

    response = await client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=1.0,
        stream=True,
    )

    assistant_message_content = ""
    async for chunk in response:
        mgs = chunk.choices[0].delta
        if "content" in mgs:
            assistant_message_content += mgs["content"]
        yield mgs

    assystant_mgs = {"role": "assistant", "content": assistant_message_content}
    set_history(chat_id, assystant_mgs)


async def run():
    async with sse as (read, write):
        async with ClientSession(
            read, write,
        ) as session:
            # Test prompt
            # prompt = "Who are u?"
            prompt = "How many table in my database, name of database is postgres and wht each of them do?"
            print(f"User: {prompt}")
            async for res in agent_loop(1, prompt, client, session):
                if res.content is not None:
                    print(res.content, end="", flush=True)

if __name__ == "__main__":
    asyncio.run(run())
