from re import sub

st3 = 'test^홍길동 abc 대한*민국 123$tbc'

text1 = sub('[\^*$]+', '', st3)
print(text1)

text2 = sub('[0-9]', '', text1)
print(text2)
