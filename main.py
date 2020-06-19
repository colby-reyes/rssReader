#! ~/miniconda/envs/webapps/bin/python
from flask import Flask, render_template
from feed import *
app = Flask(__name__)


@app.route('/')
def index():
    data = get_articles()
    return render_template(‘home.html’, data=data)

@app.route('/selected-article')
def func_name(foo):
    selected = 'article clicked on >> use "set" in html file? >> how to have html buttons call py functions?'  
    article = data['articles'][selected]
    return render_template('article.html', data=article)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
 
