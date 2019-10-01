import pandas as pd

df = pd.read_csv('city_weather.csv')

# Use the .to_html() to get your table in html
print(df.to_html())