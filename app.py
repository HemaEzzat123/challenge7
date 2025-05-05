from flask import Flask, request, render_template_string, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    # If a cookie is passed in the query parameters, save it to a file
    cookie = request.args.get('cookie')
    if cookie:
        with open("cookies.txt", "a") as f:
            f.write(cookie + "\n")
        return "Cookie received."
    
    return render_template_string(open('index.html').read())

@app.route('/feedback', methods=['GET'])
def feedback():
    # Get the feedback message from the query parameters
    msg = request.args.get('msg')
    if msg:
        return f"<h2>Your Feedback:</h2><p>{msg}</p>"
    
    return '''
        <p>Hint: When you start attacking a website, which file do you search for first? :)</p>
    '''

@app.route('/chocolate_chip')
def chocolate_chip():
    return "AzCTF{cookie_crumble}"

if __name__ == '__main__':
    app.run(debug=True)
