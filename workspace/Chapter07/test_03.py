from re import findall, sub

tests = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,A124&***$?']

def crean_text(text) :
    texts_re = text.lower()
    texts_re2 = sub('2-8', '', texts_re)
    texts_re3 = sub('[,.?;:]', '', texts_re2)
    texts_re4 = sub('[$&*]', '', texts_re3)
    texts_re5 = ' '.join(texts_re4.split())
    return texts_re5

texts_result = [crean_text(text) for text in texts]
print(texts_result)
