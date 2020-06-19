from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
 from flask import Blueprint, render_template
 
 rss_reader = Blueprint('rss_reader',__name__,template_folder='templates')
 
 
 @rss_reader.route('/')
 def index():
     return render_template('index.html')
  

app.register_blueprint(blueprint_name)