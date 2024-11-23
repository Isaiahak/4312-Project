from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

csv_path_processed = r"Task2.csv"
csv_path_comparison = r"Task3vader.csv"

reviews = pd.read_csv(csv_path_processed)

results = []
analyzer = SentimentIntensityAnalyzer()

for review in reviews.itertuples():
    if not isinstance(review.Review, str) or review.Review.strip() == '':
        continue
    
    vaderSentiment = analyzer.polarity_scores(review.Review)
    review_dict = {
            'Apps package name': review.Package_name,
            'Review': review.Review,
            'Polarity': vaderSentiment['compound']
        }
    results.append(review_dict)

df = pd.DataFrame(results)
df.to_csv(csv_path_comparison, index='false')
print("added the comparison to the csv")



