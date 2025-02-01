import time
from pytrends.request import TrendReq
import pandas as pd

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Track **general relocation interest**
broad_search_terms = ["Moving abroad", "Leaving the US", "Relocating overseas"]

# Track **specific country interest** (limit to 5 to avoid Google errors)
top_countries = ["Moving to Canada", "Moving to Mexico", "Moving to Portugal", 
                 "Moving to Spain", "Moving to Australia"]

# Function to fetch Google Trends data safely
def fetch_trends(keywords):
    try:
        pytrends.build_payload(keywords, timeframe='now 7-d', geo='US')
        data = pytrends.interest_over_time()

        if 'isPartial' in data.columns:
            data = data.drop(columns=['isPartial'])

        return data.mean().sort_values(ascending=False)

    except Exception as e:
        print(f"Error fetching data for {keywords}: {e}")
        return pd.Series()

# Query broad search terms
print("Fetching general relocation trends...")
broad_trends = fetch_trends(broad_search_terms)
time.sleep(2)  # Small pause to avoid Google blocking

# Query country-specific interest
print("Fetching country-specific relocation trends...")
country_trends = fetch_trends(top_countries)
time.sleep(2)

# Save results
broad_trends.to_csv('broad_moving_trends.csv')
country_trends.to_csv('country_moving_trends.csv')

print("\n✅ Data saved: broad_moving_trends.csv & country_moving_trends.csv")

# Print results for review
print("\n📊 General Relocation Interest:")
print(broad_trends)

print("\n🌍 Top Trending Countries:")
print(country_trends)