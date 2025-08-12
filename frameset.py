# frameset_app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Frameset Example</title>
    </head>
    <frameset rows="80,*,50">
        <frame src="/top" name="topFrame" scrolling="no" noresize>
        <frameset cols="200,*">
            <frame src="/left" name="leftFrame">
            <frame src="/main" name="mainFrame">
        </frameset>
        <frame src="/bottom" name="bottomFrame" scrolling="no" noresize>
    </frameset>
    </html>
    """

@app.route("/top")
def top():
    return """
    <html><body style="background:#f0f0f0; text-align:center;">
    <h2>Top Header — Home | Site Map | Search</h2>
    </body></html>
    """

@app.route("/left")
def left():
    return """
    <html><body style="background:#fafafa;">
    <h3>Navigation</h3>
    <ul>
        <li><a href="/main?content=home" target="mainFrame">Home</a></li>
        <li><a href="/main?content=about" target="mainFrame">About Us</a></li>
        <li><a href="/main?content=contact" target="mainFrame">Contact Us</a></li>
        <li><a href="/main?content=sponsors" target="mainFrame">Sponsors</a></li>
    </ul>
    </body></html>
    """

@app.route("/main")
def main():
    from flask import request
    content = request.args.get("content", "home")
    pages = {
        "home": "<h2>Welcome to the Home Page</h2><p>This is the main content area.</p>",
        "about": "<h2>About Us</h2><p>We are a fictional company.</p>",
        "contact": "<h2>Contact Us</h2><p>Email: example@domain.com</p>",
        "sponsors": "<h2>Our Sponsors</h2><p>List of sponsors goes here.</p>"
    }
    return f"<html><body>{pages.get(content, 'Page not found.')}</body></html>"

@app.route("/bottom")
def bottom():
    return """
    <html><body style="background:#f0f0f0; text-align:center;">
    <small>© 2025 — About Us | Contact Us | Sponsors</small>
    </body></html>
    """

if __name__ == "__main__":
    app.run(debug=True)