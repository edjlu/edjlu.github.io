import os

template = '''<!DOCTYPE html>
<html>
    <head>
        <title> Reviews - {} </title>
        <link rel="stylesheet" href="review.css">
    </head>
<body>

    <nav>
        <div>
            <a href="index.html"> Homepage </div></a>
        <div class="active">
            <a href="game reviews.html" id="current"> Video Game Reviews </a>
        </div>
        <div>TV, Movie, Music Reviews</div>
        <div>
            Recipes
        </div>
        <div>
            Travels
        </div>
        
      </nav>
    <div id="wrapper">
        
    <img src="images/horizon.jpg" class="hero" alt="cover">

{}
<h2>Click the sidebar to check out more content or return home.</h2>
</body>
</html>'''

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



