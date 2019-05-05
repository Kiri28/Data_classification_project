import nltk.stem as Stemmer
def STEM(text):
    stemm = Stemmer('russian')
    text = ' '.join( stemm.stemWords( text.split() ) )
    return(text)
print(STEM("Привет ребятки!!!"))

