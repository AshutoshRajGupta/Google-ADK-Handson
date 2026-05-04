# from google.adk.agents.llm_agent import Agent
# from google.adk.tools import google_search
# import os
#
# # def list_all_files() -> str:
# #     """
# #     Lists all files and folders in the current directory
# #
# #     Returns:
# #         A formated string containing all entries or an error message.
# #     """
# #     try:
# #         items= os.listdir(".")
# #         if not items:
# #             return "the current directory is empty "
# #
# #         result= "Contents of current directory:\n"
# #         for name in items:
# #             path = os.path.abspath(name)
# #             if os.path.isdir(path):
# #                 result+= f"[DIR] {path}\n"
# #             else:
# #                 result+= f"[FILE] {path}\n"
# #
# #         return result.strip()
# #
# #     except Exception as e:
# #         return f"Error listing directory contents: {e}"
#
# root_agent = Agent(
#     model='gemini-2.5-flash',
#     name='root_agent',
#     description='A helpful assistant for user questions.',
#     instruction='Answer user questions to the best of your knowledge',
#     tools=[google_search]
# )


from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

root_agent = Agent(
    model="gemini-flash-latest",
    name="github_agent",
    instruction="Help users get information from GitHub",
    tools=[
        McpToolset(
            connection_params=StreamableHTTPConnectionParams(
                url="https://api.githubcopilot.com/mcp/",
                headers={
                    "Authorization": f"Bearer {GITHUB_TOKEN}",
                    "X-MCP-Toolsets": "all",
                    "X-MCP-Readonly": "true"
                },
            ),
        )
    ],
)