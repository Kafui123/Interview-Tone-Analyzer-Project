import whisper

# use the .load_model function in whisper to convert your file to english 
model = whisper.load_model("base")
result = model.transcribe("WhatsApp Ptt 2025-05-24 at 21.08.19.ogg")

# save to text file 

with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])