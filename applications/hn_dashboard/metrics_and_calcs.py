from applications.hn_dashboard.sql import get_latest_data_distribution, get_latest_text
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from applications.hackernews_nlp.ai_handling.predictors import clean_text


def get_distribution_of_labels(start, end):
    df = get_latest_data_distribution(start, end)
    dist = df['standard_ml_label'].value_counts()
    return dist


def get_wordcloud(topic):
    df = get_latest_text(topic)
    stopwords = set(STOPWORDS)
    stopwords.update(["x27", "quot", 'x2F'])
    raw_txt = (" ").join([df['raw_txt'][i] for i in range(df.shape[0])])
    wordcloud_img = WordCloud(stopwords=stopwords).generate(raw_txt)
    return wordcloud_img
