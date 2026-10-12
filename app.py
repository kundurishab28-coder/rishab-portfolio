from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Rishab | Cybersecurity</title>
<style>
* { box-sizing: border-box; }
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #07111f;
    color: #e5f3ff;
}
header {
    padding: 22px 8%;
    background: #0d1b2a;
    border-bottom: 1px solid #183b56;
    color: #38bdf8;
    font-weight: bold;
    letter-spacing: 2px;
}
main {
    max-width: 950px;
    margin: auto;
    padding: 55px 22px;
}
.hero {
    padding: 35px 0;
}
.tagline { color: #38bdf8; letter-spacing: 3px; }
h1 { font-size: 48px; margin: 12px 0; }
h1 span { color: #38bdf8; }
p { color: #b6c7d8; line-height: 1.8; }
section {
    background: #0d1b2a;
    border: 1px solid #183b56;
    border-radius: 14px;
    padding: 25px;
    margin: 25px 0;
}
h2 { color: #38bdf8; }
.skill {
    display: inline-block;
    background: #132b40;
    color: #7dd3fc;
    padding: 9px 13px;
    margin: 5px;
    border-radius: 7px;
}
a { color: #38bdf8; }
footer {
    text-align: center;
    padding: 25px;
    border-top: 1px solid #183b56;
}
@media(max-width:600px) {
    h1 { font-size: 34px; }
}
</style>
</head>
<body>
<header>RISHAB.DEV | PORTFOLIO</header>
<main>
    <div class="hero">
        <p class="tagline">CYBERSECURITY • LEARNING • BUILDING</p>
        <h1>Hello, I'm <span>Rishab Kundu</span></h1>
        <h2>Cybersecurity Enthusiast</h2>
        <p>B.Tech Computer Science student exploring network
        security, Linux and ethical hacking.</p>
    </div>

    <section>
        <h2>About Me</h2>
        <p>I'm developing my technical skills step by step and
        learning how to identify and prevent security risks.</p>
    </section>

    <section>
        <h2>Technical Skills</h2>
        <span class="skill">Networking Basics</span>
        <span class="skill">Kali Linux Basics</span>
        <span class="skill">Ethical Hacking Fundamentals</span>
        <span class="skill">Python</span>
    </section>

    <section>
        <h2>Featured Project</h2>
        <h3>CyberShield</h3>
        <p>A beginner project exploring basic network scanning
        and security report generation.</p>
    </section>

    <section>
        <h2>Connect With Me</h2>
        <p>LinkedIn:
        <a href="https://www.linkedin.com/in/rishab-kundu-279207383/"
        target="_blank">My LinkedIn Profile</a></p>
        <p>Email: Add your email address here.</p>
    </section>
</main>
<footer>© 2026 Rishab Kundu | Built with Python & Flask</footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)

