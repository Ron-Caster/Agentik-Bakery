def get_cli_input(prompt: str = "Enter input: ") -> str:
    try:
        return input(prompt).strip()
    except EOFError:
        return ""


def display_result(agent_name: str, flag: int, output: str) -> None:
    print(output)
    print(f"agent={agent_name} flag={flag}")
