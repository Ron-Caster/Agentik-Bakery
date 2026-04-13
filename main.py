# Input Prompt

    # Get Input from the cli
    # Get Input from the scheduler

    # Pass the prompt to the Intent Module

# Intent Module

    # Process the prompt and determine the intent - output as a JSON object
       
        # Send the prompt to LLMHub 
        # Get JSON output from LLMHub to to select the appropriate agent

    # Send the "Input Prompt" to "General" or "Planner" based on JSON output

# Receive Output/Log/Printables from General and Planner

    # Show the Output/Log/Printables to the user

from input.cli import display_result, get_cli_input
from orchestration.intent import route_input


def main() -> tuple[str, int, str]:
    prompt = get_cli_input()
    agent_name, flag, output = route_input(prompt)
    display_result(agent_name, flag, output)
    return agent_name, flag, output


if __name__ == "__main__":
    main()
