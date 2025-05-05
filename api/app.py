from flask import Flask, request, render_template_string, make_response
import os

app = Flask(__name__)

# Ensure the cookies.txt file exists
if not os.path.exists('cookies.txt'):
    with open('cookies.txt', 'w') as f:
        pass

# HTML template
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Halib Al-Khair</title>
</head>
<body>
    <h1>Welcome to Halib Al-Khair</h1>
    <p>Your feedback is important to us!</p>
    <form action="/" method="get">
        <label for="msg">Your Feedback:</label>
        <input type="text" id="msg" name="msg" required>
        <button type="submit">Submit</button>
    </form>
    {% if feedback %}
    <h2>Your Feedback:</h2>
    <p>{{ feedback }}</p>
    {% endif %}
    <p>Hint: When you start attacking a website, which file do you search for first? :)</p>
    <p>AzCTF{cookie_crumble}</p>
</body>
</html>
'''

@app.route('/', methods=['GET'])
def index():
    # Handle the cookie parameter (equivalent to the PHP cookie handler)
    if 'cookie' in request.args:
        cookie_value = request.args.get('cookie')
        with open('cookies.txt', 'a') as f:
            f.write(cookie_value + '\n')
        return "Cookie received."
    
    # Handle feedback message (equivalent to the PHP feedback handler)
    feedback = request.args.get('msg', None)
    
    # Render the template with the feedback if available
    return render_template_string(HTML_TEMPLATE, feedback=feedback)

# For Vercel deployment
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))