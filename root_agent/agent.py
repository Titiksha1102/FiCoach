# root_agent.py

import asyncio
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool


from .sub_agents.budget_agent.agent import budget_agent 
from .sub_agents.debt_agent.agent import debt_agent
from .sub_agents.investment_agent.agent import investment_agent

root_agent = Agent(
    model='gemini-2.0-flash-001', # Using an updated model name
    name='root_agent',
    description='A personal finance assistant for users finance related questions.',
    instruction="""
    You are a personal finance manager agent that is responsible for overseeing the work of the other agents.

    Always delegate the task to the appropriate agent. Use your best judgement 
    to determine which agent to delegate to.Never try to answer the question yourself.

    You are responsible for delegating tasks to the following agent:
    
    - debt_agent
    - budget_agent
    - investment_agent
    """,
    # Pass the initialized agent objects here
    sub_agents=[debt_agent, budget_agent, investment_agent],
)
    
