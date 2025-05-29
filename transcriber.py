import whisper 


model = whisper.load_model("base")
result = model.transcribe("WhatsApp Ptt 2025-05-24 at 21.08.19.ogg")

print(result["text"])