import pandas as pd
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification

from transformers import TextClassificationPipeline

def cut_text(text):
    if len(text)>511:
        return text[:512]
    return text

def map_impl(df, column):
    return pd.Series(map(pipe, df[column]))

model_name = 'nlptown/bert-base-multilingual-uncased-sentiment'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer, return_all_scores=True)

# Load provided train data
data_df = pd.read_excel('TestSet/Rest_Mex_2022_Sentiment_Analysis_Track_Train.xlsx')
data_df['Title'] = data_df['Title'].fillna(' ').apply(str)
data_df['Opinion'] = data_df['Opinion'].fillna(' ').apply(str)
data_df['Opinion'] = data_df['Opinion'].apply(lambda x: cut_text(x))


data_df['Score Opinion'] = map_impl(data_df, 'Opinion')
data_df.to_csv('TestSet/test_opinion.csv', index=False)

data_df['Score Title'] = map_impl(data_df, 'Title')
data_df.to_csv('TestSet/test_title.csv', index=False)

data_df['Features'] = data_df['Score Opinion'].apply(lambda x: [x[0][i]['score'] for i in range(5)]) + data_df['Score Title'].apply(lambda x: [x[0][i]['score'] for i in range(5)])
data_df.to_csv('TestSet/test_10D.csv', index=False)