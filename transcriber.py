import streamlit as st
from textblob import TextBlob
import whisper, re

# Streamlit UI
st.title("🎤 Speech Confidence Analyzer")
st.write("Upload an audio file, and we'll analyze filler words, sentiment, and give you a confidence score.")

# File uploader
uploaded_file = st.file_uploader("Upload your audio file (.ogg, .mp3, .wav)", type=["ogg", "mp3", "wav"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    with open("temp_audio.ogg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.info("🔄 Transcribing audio... please wait.")
    
    # Transcribe with Whisper
    model = whisper.load_model("base")
    result = model.transcribe("temp_audio.ogg")
    transcript = result["text"]

    # --- Filler word analysis ---
    filler_words = ["um", "uh", "like", "you know", "i mean"]
    pattern = r'\b(?:' + '|'.join(filler_words) + r')\b'
    matches = re.findall(pattern, transcript.lower())
    filler_count = len(matches)

    # Clean transcript
    transcript_clean = re.sub(pattern, '', transcript, flags=re.IGNORECASE)

    # --- Sentiment analysis ---
    blob = TextBlob(transcript_clean)
    word_count = len(blob.words)
    sentence_count = len(blob.sentences)
    sentiment = blob.sentiment.polarity
    sentiment1 = blob.sentiment.subjectivity

    # --- Confidence scoring ---
    confidence = 10
    if filler_count > 20:
        confidence -= 2
    if sentiment < -0.1:
        confidence -= 1.5
    if word_count / (transcript_clean.count('.') + 1) < 10:
        confidence -= 1.5
    confidence = max(0, min(confidence, 10))

    # --- Suggestions ---
    suggestions = []
    if filler_count > 20:
        suggestions.append("Try to reduce filler words like 'um' and 'like'.")
    if sentiment < 0:
        suggestions.append("Try to sound more enthusiastic and positive.")
    if "I think I" in transcript_clean:
        suggestions.append("Avoid uncertain phrases like 'I think I...' and be assertive.")
    if not suggestions:
        suggestions.append("Great job! Keep your tone confident and concise.")

    # --- Display results ---
    st.subheader("📄 Transcription")
    st.write(transcript)

    st.subheader("📊 Analysis Results")
    st.write(f"**Word Count:** {word_count}")
    st.write(f"**Sentence Count:** {sentence_count}")
    st.write(f"**Filler Words Count:** {filler_count}")
    st.write(f"**Sentiment Polarity:** {sentiment:.2f}")
    st.write(f"**Sentiment Subjectivity:** {sentiment1:.2f}")
    st.write(f"**Confidence Score:** {confidence}/10")

    st.subheader("💡 Suggestions")
    for s in suggestions:
        st.write(f"- {s}")