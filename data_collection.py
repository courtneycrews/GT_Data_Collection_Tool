from pytrends.request import TrendReq
import pandas as pd

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Define the search keywords and timeframe
keywords = ['moving to Canada', 'relocation after election']
pytrends.build_payload(keywords, timeframe='now 7-d', geo='US')

# Fetch interest over time
data = pytrends.interest_over_time()

# Save the data to a CSV file
if not data.empty:
    data.to_csv('google_trends_data.csv')
    print("Data collected and saved to google_trends_data.csv")
else:
    print("No data found for the given keywords.")