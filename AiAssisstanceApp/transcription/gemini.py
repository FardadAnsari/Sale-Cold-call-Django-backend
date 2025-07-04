import google.generativeai as genai

def analyze_transcript_with_gemini(transcript_text: str, api_key: str) -> str:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = (
        "This is a transcript of a sales call. Please:\n"
        "1. Summarize it\n"
        "2. Give sales feedback\n"
        "3. Rate the performance from 0 to 10"
    )

    response = model.generate_content([prompt, transcript_text])
    return response.text