
from rich import print
import asyncio
from ...application.database.models.llm_agent import LargeLanguageModelAgent

async def run_agent(agent: LargeLanguageModelAgent, agent_id: str, agent_queue: asyncio.Queue, agent_results: asyncio.Queue):
    while True:
        try:
            message = await agent_queue.get()
            if message is None:
                break
            result = await agent.run(message)
            await agent_results.put(result)
        except Exception as e:
            print(f"Agent {agent_id} failed with error: {e}")
            break
    print(f"Agent {agent_id} finished")