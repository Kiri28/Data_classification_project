import pymystem3
def lemmatize(text):
    mystem = pymystem3 . Mystem ( )
    z=text.split()
    lem=""
    for i in range(0,len(z)):
        lem =lem + " "+ mystem. lemmatize (z[i])[0]
    return(lem)


