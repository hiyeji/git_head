email = ["""hong@12.com
you2@naver.com
12kang@hanmail.net
kimjs@gmail.com"""]

email_rel = [t.lower() for t in email]
print('email_rel :', email_rel)


from re import findall, match

for e in email.split(sep='\n') :
