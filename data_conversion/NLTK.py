import nltk
from nltk.stem import  SnowballStemmer
def NLTK(text):
    stemmer = SnowballStemmer('russian') #У нас поставлена Русская раскладка!
    #тоесть эта штука у нас сейчас работает только для русского текста, но мы можем это поменять
    stem=[stemmer.stem(w) for w in text.split()]
    stem= ' '.join(stem)
    return(stem)

