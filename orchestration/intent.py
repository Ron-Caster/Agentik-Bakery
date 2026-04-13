from agents.general import process_input as process_general
from agents.planner import process_input as process_planner
from models.llmhub import intent_json


def route_input(user_input: str):
    selection = intent_json(user_input)
    print("AI intent response:", selection)
    agent = selection.get("agent")
    if agent == "planner":
        return "planner", *process_planner(user_input)
    return "general", *process_general(user_input)
