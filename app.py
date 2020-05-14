################
# Elizabeth Lee
# efl2121
# final
################

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return(render_template('index.html'))
    
@app.route("/1006")
def classpage():
    return "<p> 1006 Homepage</p>"


#start the server
if __name__ == "__main__":
    app.run()


#<a href="https.website.com> Text for website here </a>