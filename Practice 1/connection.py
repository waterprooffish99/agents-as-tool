import os
from dotenv import load_dotenv
from openai_agents import OpenAIChatCompletionsModel, RunConfig, AsyncOpenAI


# Load environment variables from .env file
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is set, if not, raise an error

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set. Please set it in your .env file.")

#Reference: http://ai.googgle.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.5-flash",
    openai_client = external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)
