import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import os

# Download only required NLTK data (stopwords)
=======
import nltk
import streamlit as st
import pickle
import string
from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer
nltk.download('punkt')
>>>>>>> a0e55e7716d99c4f1efc18e44abe58cf4a09de81
nltk.download('stopwords')

ps = PorterStemmer()

<<<<<<< HEAD
def transform_text(text):
    text = text.lower()
    text = text.split()   # ✅ replaced nltk.word_tokenize()
=======

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
>>>>>>> a0e55e7716d99c4f1efc18e44abe58cf4a09de81

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

<<<<<<< HEAD

# Load model and vectorizer safely
BASE_DIR = os.path.dirname(_file_)

tfidf = pickle.load(open(os.path.join(BASE_DIR, 'vectorizer.pkl'), 'rb'))
model = pickle.load(open(os.path.join(BASE_DIR, 'model.pkl'), 'rb'))

# UI
st.title("📩 SMS Spam Classifier")
=======
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("SMS Spam Classifier")
>>>>>>> a0e55e7716d99c4f1efc18e44abe58cf4a09de81

input_sms = st.text_area("Enter the message")

if st.button('Predict'):

<<<<<<< HEAD
    # preprocess
    transformed_sms = transform_text(input_sms)

    # vectorize
    vector_input = tfidf.transform([transformed_sms])

    # predict
    result = model.predict(vector_input)[0]

    # display
    if result == 1:
        st.error("🚨 Spam Message")
    else:
        st.success("✅ Not Spam")
=======
    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")

