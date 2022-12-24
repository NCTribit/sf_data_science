import pandas as pd
import json


countries_df = pd.DataFrame(
    data = [
        ['Англия', 56.29, 133396],
        ['Канада', 38.05, 9984670],
        ['США', 322.28, 9826630],
        ['Россия', 146.24, 17125191],
        ['Украина', 45.5, 603628],
        ['Беларусь', 9.5, 207600],
        ['Казахстан', 17.04, 2724902]
    ],
    columns= ['country', 'population', 'square'],
    index = ['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ']
)

countries_df.to_json('countries.json', force_ascii=False, orient="index")
with open('countries.json', 'r', encoding='utf-8') as f:
    parsed = json.load(f)
# json.detect_encoding(parsed)
print(json.dumps(parsed, indent=4, ensure_ascii=False))