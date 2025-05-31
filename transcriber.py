from textblob import TextBlob
import whisper, re

# use the .load_model function in whisper to convert your file to english 
model = whisper.load_model("base")
result = model.transcribe("um, uh like.ogg")

# save to text file 


with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])


# loading and cleaning the transcription 

with open("transcription.txt", "r") as file:
    transcript1 = file.read().strip()



# creating a filler words list 
filler_words = ["um", "uh", "like", "you know", "i mean"]

pattern = r'\b(?:' + '|'.join(filler_words) + r')\b'

# this searches the text for anything matching pattern. and it replaces it with "" (deletees them).... returns a string 
transcript1 = re.sub(pattern, '', transcript1, flags=re.IGNORECASE)
print(type(transcript1))

with open("transcription1.txt", "w", encoding="utf-8") as f:
    f.write(transcript1)



# using the textblob nlp to break the words into sentences as well as the sentiment 
blob = TextBlob(transcript1)


word_count = len(blob.words)

sentence_count = len(blob.sentences)

sentiment = blob.sentiment


print("Word Count:", word_count)
print("Sentence Count:", sentence_count)
print("Sentiment (polarity, subjectivity):", sentiment)


