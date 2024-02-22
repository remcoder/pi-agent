
import sys
import json
from openai import OpenAI

client = OpenAI(api_key="<insert key>")

def analyze_and_alert_with_gpt3():
    system_report = sys.stdin.read()
    # Adding an improved role instruction to the prompt
    role_instruction = """
    You are an advanced AI system specialized in monitoring and analyzing computer system health. You have been designed to read and understand system reports, identify potential issues, and advise on whether these issues are critical enough to warrant immediate attention. Your responses should be concise, lighthearted, and directly address the concerns highlighted in the reports. Cheerful. Sound like the weatherman. You aim to assist system administrators in maintaining optimal system performance and security.
    """
    instruction = "Please respond in JSON format with two fields: 'descriptive_report' which contains your analysis of the system report, and 'alert_status' which should be either 'True' or 'False' indicating whether an alert should be triggered based on the report."
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": role_instruction},
            {"role": "user", "content": f"{system_report}\n{instruction}"}
        ]
    )
    
    try:
        message_content = response.choices[0].message.content
        print(message_content)
    except AttributeError:
        print("There was an error processing the GPT-3 response.")

if __name__ == "__main__":
  sys.stderr.write('Consulting GPT\n')
  sys.stderr.flush()
  analyze_and_alert_with_gpt3()