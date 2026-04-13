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