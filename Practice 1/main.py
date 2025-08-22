from openai_agents import Agent, Runner
from connection import config

# Creating Individual Agents for translation tasks.

italian_agent = Agent(
    name = "Italian Translator",
    Instruction = "Translate any English text to Italian.",
)

italian_agent = Agent(
    name = "Italian Translator",
    Instruction = "Translate any English text to Italian.",
)

spanish_agent = Agent(
    name = "Spanish Translator",
    Instruction = "Translate any English text to Spanish.",
)

french_agent = Agent(
    name = "French Translator",
    Instruction = "Translate any English text to French.",
)

thai_agent = Agent(
    name = "Thai Translator",
    Instruction = "Translate any English text to Thai.",
)

# Creating main Agent that will run the translation tasks.
triage_agent = Agent(
    name = "Triage Agent",
    instructions = """You are a triage agent that will assign 
    translation tasks to the appropriate language-specific agents.""",
    tools = [
        italian_agent.as_tool(
            name = "Italian Translator",
            instructions = "Translate any English text to Italian."
        ),

        spanish_agent.as_tool(
            name = "Spanish Translator",
            instructions = "Translate any English text to Spanish."
        ),
        french_agent.as_tool(
            name = "French Translator",
            instructions = "Translate any English text to French."
        ),
        thai_agent.as_tool(
            name = "Thai Translator",
            instructions = "Translate any English text to Thai."
        ),
    ]
)

result = Runner.run_sync(
    triage_agent,
    "Translate 'I love Learning Python' into Italian.",
    run_config = config
)


print(result.final_output)
