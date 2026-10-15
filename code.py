import pandas as pd
import numpy as np
import re
from hazm import Normalizer, word_tokenize, Stemmer, stopwords_list
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# بارگذاری مجموعه داده‌ها
df = pd.read_excel('C:/Users/A.Refua/IMDB_Dataset_Farsi.xlsx')

# نمایش چند نمونه از داده‌ها
print(df.head())

# پیش‌پردازش داده‌ها
normalizer = Normalizer()
stop_words = set(stopwords_list())
stemmer = Stemmer()

def preprocess_text_farsi(text):
    text = normalizer.normalize(text)
    words = word_tokenize(text)
    words = [stemmer.stem(word) for word in words if word not in stop_words]
    return ' '.join(words)

df['review'] = df['review'].apply(preprocess_text_farsi)
print(df.head())

# استخراج ویژگی‌ها
vectorizer = CountVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['review']).toarray()
y = df['sentiment'].apply(lambda x: 1 if x == 'positive' else 0)  # تبدیل برچسب‌ها به اعداد

# تقسیم داده‌ها به مجموعه‌های آموزش و تست
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# آموزش مدل
model = MultinomialNB()
model.fit(X_train, y_train)

# پیش‌بینی بر روی داده‌های تست
y_pred = model.predict(X_test)

# ارزیابی مدل
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print('Confusion Matrix:')
print(conf_matrix)
print('Classification Report:')
print(class_report)

# تابع پیش‌بینی احساسات برای متن‌های جدید
def predict_sentiment(review):
    review = preprocess_text_farsi(review)
    review_vector = vectorizer.transform([review]).toarray()
    sentiment = model.predict(review_vector)
    return 'مثبت' if sentiment[0] == 1 else 'منفی'

# متن‌های ورودی برای تست
test_reviews_farsi = [
    "من واقعا این فیلم را دوست داشتم! بازیگری فوق‌العاده بود و داستان بسیار جذاب بود.",
    "این بدترین فیلمی بود که تا به حال دیده‌ام. کاملاً وقت تلف کردن بود.",
    "فیلم بدی نبود، نه خیلی عالی و نه خیلی بد.",
    "داستان فوق‌العاده و اجرای عالی بازیگران. شدیداً توصیه می‌کنم!",
    "من اصلاً از این فیلم لذت نبردم. داستان خیلی خسته‌کننده و قابل پیش‌بینی بود.",
    "فیلم لحظات خوبی داشت، اما در کل ناامید کننده بود.",
    "تصاویر شگفت‌انگیز و داستان جذاب. باید دید!",
    "فیلم خیلی کسل‌کننده و بی‌مزه بود.",
    "فیلم بسیار عالی با پیام قوی. بازیگران کار فوق‌العاده‌ای انجام دادند.",
    "من این فیلم را توصیه نمی‌کنم. عمق نداشت و ضعیف اجرا شده بود."
]

# پیش‌بینی احساسات برای هر یک از متن‌های تست
for review in test_reviews_farsi:
    sentiment = predict_sentiment(review)
    print(f'نظر: {review}\nاحساس: {sentiment}\n')
