import google.generativeai as genai



def analyze_transcript_with_gemini(transcript_path, api_key):
    genai.configure(api_key=api_key)

    with open(transcript_path, "r", encoding="utf-8") as f:
        transcript_text = f.read()

    model = genai.GenerativeModel("gemini-2.0-flash")  # ✅ Works with v1
    chat = model.start_chat()

    prompt = """
You are a sales call evaluator. Analyze the conversation and return the following:
Summary: <summary>
Feedback: <feedback>
Score: <number between 0-10>
"""

    response = chat.send_message(prompt + "\n\n" + transcript_text)
    return response.text  # or response.candidates[0].content.parts[0].text depending on version
