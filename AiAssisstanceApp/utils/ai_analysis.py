import google.generativeai as genai

def analyze_transcript_with_gemini(transcript_path, api_key):
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-pro')

    with open(transcript_path, "r", encoding="utf-8") as f:
        transcript_text = f.read()

    prompt = (
        "This is a transcript of a sales call. Please:\n"
        "1. Summarize it\n"
        "2. Give sales feedback\n"
        "3. Rate the performance from 0 to 10\n\n"
        f"Transcript:\n{transcript_text}"
    )

    response = model.generate_content(prompt)
    return response.text  # Gemini uses `.text` not `.content`