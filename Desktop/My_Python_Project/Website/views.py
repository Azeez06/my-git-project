from flask import Blueprint, render_template
views = Blueprint ("views", __name__)
@views.route('/')
def home():
    return render_template  ("home.html")
    #return "<h1>Hello</h1>" 
#@views.route('/')
#def home():
    #print("Home page loaded!")  # This should show in your terminal
    #return "<h1>Hello! Welcome Azeez </h1>"