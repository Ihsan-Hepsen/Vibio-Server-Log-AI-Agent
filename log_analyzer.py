from openai import OpenAI
import os


def analyze_logs(logs: str, model="gpt-4") -> str:
    if not logs:
        return "No logs to send to GPT-4"

    print("[info]: Sending logs to GPT-4")
    content = f"""
        You are an expert DevOps log reviewer. You are given log lines to inspect. 
        Your task:
        - Flag any errors or warnings that require attention
        - Group similar messages
        - Rate them: 
            🔴 ALERT (if requires immediate attention and/or exremely critical)
            🟠 Critical (with most likey cause, a short description)
            🟡 Warning (with a best suggestion, a short description)
        - Suggest likely causes and fixes
        - Ignore common noise (e.g., known startup messages, cache misses, etc.)
        - Ignore regular INFO and similar logs that are not important
        
        You MUST use the following teplate when reporting:
        Template start:
        --- R E P O R T ---
        🔴 ALERT (don't report if there is none) (count)
            show the specific log and show the possible cause and solution
        🟠 Critical (don't report if there is none) (count)
            show the specific log and show the possible cause and solution
        🟡 Warning (don't report if there is none) (count)
            show the specific log and show the possible cause and solution
        Template end

        Here are the logs you are tasked to inspect:
        {logs}
    """

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": content},
        ],
    )
    return response.choices[0].message.content
