import re
import string
import nltk
from num2words import num2words
from emoji import demojize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pandas as pd

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

csv_path_raw = r"Task1.csv"
csv_path_processed = r"Task2.csv"

def clean_review(review):

    review = review.translate(str.maketrans('', '', string.punctuation))
    review = demojize(review)
    review = re.sub(r'[^\w\s]', '', review)  
    review = ' '.join([num2words(word) if word.isdigit() else word for word in review.split()])   
    review = re.sub(r'\s+', ' ', review).strip()   
    review = review.lower()     
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(review)
    words = [word for word in words if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]  
    return ' '.join(words)

df = pd.read_csv(csv_path_raw)

df['Review'] = df['Review'].apply(clean_review)

df.to_csv(csv_path_processed, index=False)
print(f"Data saved to {csv_path_processed}")