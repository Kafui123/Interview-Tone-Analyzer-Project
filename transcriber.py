import whisper, re

# use the .load_model function in whisper to convert your file to english 
model = whisper.load_model("base")
result = model.transcribe("WhatsApp Ptt 2025-05-24 at 21.08.19.ogg")

# save to text file 


with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])


# loading and cleaning the transcription 

with open("transcription.txt", "r") as file:
    transcript = file.read().strip()



# creating a filler words list 
filler_words = ["um", "uh", "like", "you know", "i mean"]

pattern = r'\b(?:' + '|'.join(filler_words) + r')\b'

# this searches the text for anything matching pattern. and it replaces it with "" (deletees them)....
transcript = re.sub(pattern, '', transcript, flags=re.IGNORECASE)
