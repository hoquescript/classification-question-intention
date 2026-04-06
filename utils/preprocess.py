import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK data files
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize the lemmatizer and define the English stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Check if the text is a valid string (handles missing values)
    if not isinstance(text, str):
        return ""

    # Lowercasing
    text = text.lower()
    
    # Removing Punctuation (Keeps only alphanumeric characters and spaces)
    text = re.sub(r'[^\w\s]', '', text)
    
    # Split the text into individual words
    words = text.split()
    
    # Remove Stopwords AND Lemmatize
    cleaned_words = []
    for word in words:
        if word not in stop_words:
            # Reduce word to its root form
            root_word = lemmatizer.lemmatize(word)
            cleaned_words.append(root_word)
            
    # Re-join the cleaned words back into a single string
    return " ".join(cleaned_words)