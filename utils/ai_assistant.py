import requests


def generate_summary(age, symptoms, medical_history):

    prompt = f"""
You are an educational patient case summarization assistant.

Patient age: {age}

Symptoms:
{symptoms}

Medical history:
{medical_history}

Give:
1. Patient information
2. Main symptoms
3. Relevant medical history
4. Important observations
5. Suggested questions for a healthcare professional

Do not diagnose the patient.
Do not prescribe medicines.
Keep the response concise and easy to understand.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        return response.json()["response"]

    return "Error connecting to Ollama."