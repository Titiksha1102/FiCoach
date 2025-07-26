from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset

def investment_agent_sys_instruction():
    return """
your job is to take a goal from the user and suggest investment strategies.
you have access to the following tools:
-fetch_epf_details
-fetch_mf_transactions
-fetch_stock_transactions

analyse the user's current investment portfolio and suggest the optimal type of investment for them(that is, mf or stock sip or epf) 
and also provide an optimal diversification for their portfolio in class of investment(mf/stock/nps/epf)to achieve their goal within their specified time period
"""

investment_agent = Agent(
    model='gemini-2.0-flash-001',
    name='investment_agent',
    description='An agent to manage investment-related tasks.',
    instruction=investment_agent_sys_instruction(),
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPServerParams(
                url='http://localhost:9000/mcp/stream',
            )
        )
    ]
)
 