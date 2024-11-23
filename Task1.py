from google_play_scraper import Sort,reviews_all 
import pandas as pd 
import numpy as np  


apps = {
    'Norton Genie': 'com.norton.genieapp',
    'Bitdefender Mobile Security': 'com.bitdefender.security',
    'Verify Scams - Scam Detector': 'com.verifyscams.app',
    'Spam Shield block－Spam Blocker': 'com.spam.shield.spamblocker.notificationhistory',
    'Lookout Life - Mobile Security': 'com.lookout'
}

columns_to_save = ['App', 'userName', 'content', 'score']
csv_path = r"Task1.csv"

def fetch_reviews(app_id, count=1000):
    reviews = []
    page = 1
    while len(reviews) < count:
        current_reviews = reviews_all(
            app_id,
            sleep_milliseconds=0,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=1000  
        )
        reviews.extend(current_reviews)
        if len(reviews) >= count:
            break
        page += 1  
    return reviews[:count] 

all_reviews = pd.DataFrame()

for app_name, app_id in apps.items():
    reviews = fetch_reviews(app_id, count=1000)
    df_reviews = pd.DataFrame(reviews)
    df_reviews['App'] = app_name
    all_reviews = pd.concat([all_reviews, df_reviews], ignore_index=True)



all_reviews[columns_to_save].to_csv(csv_path, index=False)
print(f"Data saved to {csv_path}")






