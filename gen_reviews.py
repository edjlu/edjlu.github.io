import os

t = open('template.html', 'r')
template = t.read()
t.close()


def gen1(name):    
    g = open('game_reviews/{}'.format(name), encoding='utf-8')
    title = g.readline()
    body = g.read()
    g.close()

    html = template.format(title, body)
    f = open('review {}'.format(name), 'w', encoding='utf-8')
    f.write(html)
    f.close()

files = os.listdir('game_reviews')
for filename in files:
    gen1(filename)
    print(filename)



