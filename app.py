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
def homepage():
    return(render_template('index.html'))
    
@app.route("/bookreviews")
def firstpage():
    return(render_template('bookreviews.html'))
    
@app.route("/quarantineactivities")
def seccondpage():
    return(render_template('quarantineactivities.html'))


#start the server
if __name__ == "__main__":
    app.run()
