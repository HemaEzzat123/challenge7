from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(self.path.split('?')[1]) if '?' in self.path else {}

        if 'cookie' in query:
            cookie_value = query['cookie'][0]
            with open("/tmp/cookies.txt", 'a') as f:  # Use /tmp for writable file storage in Vercel
                f.write(cookie_value + '\n')
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Cookie received.')
            return

        feedback = query.get('msg', [None])[0]

        html = f'''
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
            {'<h2>Your Feedback:</h2><p>' + feedback + '</p>' if feedback else ''}
            <p>Hint: When you start attacking a website, which file do you search for first? :)</p>
            <p>AzCTF{{cookie_crumble}}</p>
        </body>
        </html>
        '''

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())
