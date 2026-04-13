import random

from agents.general import process_input as process_general
from agents.planner import process_input as process_planner


def route_input(user_input: str):
    choice = random.choice(["general", "planner"])
    if choice == "general":
        flag, response = process_general(user_input)
        return "general", flag, response

    flag, response = process_planner(user_input)
    return "planner", flag, response
