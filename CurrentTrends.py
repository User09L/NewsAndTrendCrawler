from pytrends.request import TrendReq
from datetime import date

# Create a pytrends client
pytrends = TrendReq(hl='en-PH', tz=360)

# Set the keyword and timeframe
keyword = "Philippines"  
timeframe = 'now 1-H'   # Adjust the timeframe as needed (1 hour in this example)

# Get trending topics
pytrends.build_payload(kw_list=[keyword], cat=0, timeframe=timeframe)
trending_topics_df = pytrends.trending_searches(pn='philippines')

# Write the trending topics to a text file
output_file_path = "TrendingTopics" + str(date.today()) + ".txt",

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for topic in trending_topics_df:
        output_file.write(topic + '\n')

print(f"Trending topics of the Philippines written to '{output_file_path}'.")


