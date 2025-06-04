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

matches = re.findall(pattern, transcript1.lower())
filler_count = len(matches)

# this searches the text for anything matching pattern. and it replaces it with "" (deletees them).... returns a string 
transcript1 = re.sub(pattern, '', transcript1, flags=re.IGNORECASE)


with open("transcription1.txt", "w", encoding="utf-8") as f:
    f.write(transcript1)



# using the textblob nlp to break the words into sentences as well as the sentiment 
blob = TextBlob(transcript1)


word_count = len(blob.words)

sentence_count = len(blob.sentences)

sentiment = blob.sentiment.polarity
sentiment1 = blob.sentiment.subjectivity

# get the total time for the project 
word_count = len(transcript1.split())
wpm = 130 
minutes = word_count / wpm



print("Word Count:", word_count)
print("Sentence Count:", sentence_count)
print("Sentiment Scores: Positive" if sentiment > 0 else "Sentiment Scores: Negative" if sentiment < 0 else "Neutral")


# examples 
# fewer filler words the better 
# Longer sentences  = the better 
# positive sentiment = better 
confidence = 10 

if filler_count > 20:
    confidence -= 2
if sentiment < -0.1:
    confidence -= 1.5
if word_count / transcript1.count('.') < 10:
    confidence -= 1.5


confidence = max(0, min(confidence, 10))


print(f"Confidence Score:", confidence)


# give the suggestions 
suggestions = []


if filler_count > 20:
    suggestions.append("Try to reduce filler words like 'um' and 'like'.")

if sentiment < 0:
    suggestions.append("Try to sound more enthusiastic and positive.")

if "I think I" in transcript1:
    suggestions.append("Avoid uncertain phrases like 'I think I...' and be assertive.")

if not suggestions:
    suggestions.append("Great job! Keep your tone confident and conscise")

print("Suggestion:", "".join(suggestions))





