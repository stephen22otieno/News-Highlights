#Files imports
from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_source,get_article
from ..models import Source


#Views
@main.route("/")
def index():
    title ='Global News'
    sources = get_source()
    return render_template("index.html",title=title,sources=sources)
    

@main.route('/articles') 
def articles(): 
    '''
    View article page function that returns the articles details page and its data
    '''

    articles = get_article()
    return render_template('article.html', articles = articles) 

    

@main.route('/sources')
def source():
    
    sources = get_source()
    print(sources)
   
    return render_template('source.html', sources = sources)