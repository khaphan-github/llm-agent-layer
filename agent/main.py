from datetime import datetime
# Removed unused import
from env import *
from rich.console import Console
from rich.prompt import Prompt
from rich.markdown import Markdown
from langchain_core.messages import HumanMessage
from langchain_deepseek.chat_models import ChatDeepSeek

console = Console()

def get_current_time() -> str:
  """Returns the current time in HH:MM:SS format."""
  return datetime.now().strftime("%H:%M:%S")

# Bind the get_current_time tool to the model.
# Note: bind_tools returns a new instance that includes the tool(s)
model = ChatDeepSeek(model="deepseek-chat").bind_tools([get_current_time], tool_choice='auto')

def chatbox():
  """Handles a chatbox in the console with streaming responses."""
  console.print(Markdown("# Chatbox"))
  console.print("Type 'exit' to quit the chat.\n")

  while True:
    user_input = Prompt.ask("[bold green]You[/bold green]")
    if user_input.lower() == "exit":
      console.print("[bold red]Exiting chat...[/bold red]")
      break

    # Send user input to the model and stream the response
    console.print("[bold blue]Bot is typing...[/bold blue]")
    response_stream = model.stream([HumanMessage(content=user_input)])
    console.print("[bold blue]Bot:[/bold blue] ", end="")

    for chunk in response_stream:
      console.print(chunk.content, end="", style="bold blue")
    console.print()  # Newline after the response

if __name__ == "__main__":
  chatbox()