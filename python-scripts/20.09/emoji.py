import re


old_smile = {':-)': '\U0001f642', '}:-)': '\U0001f608', ':-(': '\U00002639', ':-|': '\U0001f610', '=_=': '\U0001f611',
             'O_o': '\U0001f914', ':-O': '\U0001f632', ':-\\': '\U0001f615', '*\\O/*': '\U0001f483'}
with open("emoji_text.txt", "r", encoding='utf-8-sig') as infile,\
        open("emoji_text_final.txt", "w", encoding='utf-8-sig') as outfile:
    '''for line in infile:
        words = line.split()
        for item in words:
            if item in old_smile:
                words[words.index(item)] = old_smile[item]
        print(words)
        lol = " ".join(words)
        print(lol)
        outfile.write(lol)'''
    for line in infile:
        outfile.write(re.sub(r'[-}:)(|O_o\\*/=]{3,5}', lambda x: old_smile[x.group()], line))
