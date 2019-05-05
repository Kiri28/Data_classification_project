def words():
    import nltk
    from nltk.corpus import brown
    stop_words= nltk.corpus.stopwords.words('russian')
    stop_word=" "
    for i in stop_words:
        stop_word=  stop_word+" "+i
    return(stop_word)
