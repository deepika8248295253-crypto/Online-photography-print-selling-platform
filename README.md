# Online-photography-print-selling-platformfrom flask import Flask, request, redirect, session, render_template_string
import sqlite3
app = Flask(__name__)
app.secret_key = "photo123"
P = [
    (1, "Nature Sunset", 199),
    (2, "Mountain View", 249),
    (3, "Ocean Waves", 299),
    (4, "City Lights", 349)
]
def db():
    return sqlite3.connect("photo.db")
def setup():
    c = db()
    c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name, email UNIQUE, password)")
    c.execute("CREATE TABLE IF NOT EXISTS orders(id INTEGER PRIMARY KEY, user, total, payment)")
    c.commit()
    c.close()
T = """
<style>
body{font-family:Arial;background:#f5f5f5;margin:0}
nav{background:#111;color:white;padding:20px}
nav a{color:white;margin:12px}
.box{background:white;padding:20px;margin:20px auto;max-width:700px}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:15px}
.card{background:white;padding:15px;border-radius:10px}
.btn,button{background:#111;color:white;padding:10px;border:0;text-decoration:none}
input,select{padding:10px;width:95%;margin:8px}
</style>
<nav>
<b>PhotoPrint</b>
<a href="/">Home</a>
<a href="/cart">Cart</a>
<a href="/login">Login</a>
<a href="/register">Register</a>
<a href="/orders">Orders</a>
</nav>
{{x|safe}}
"""
def page(x):
    return render_template_string(T, x=x)
@app.route("/")
def home():
    items = ""
    for p in P:
        items += f"""
        <div class="card">
            <h3>{p[1]}</h3>
            <h3>₹{p[2]}</h3>
            <a class="btn" href="/add/{p[0]}">Add to Cart</a>
        </div>
        """
    return page(f"""
    <div class="box">
        <h1>Online Photography Print Store</h1>
        <div class="grid">{items}</div>
    </div>
    """)
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        try:
            c = db()
            c.execute(
                "INSERT INTO users(name,email,password) VALUES(?,?,?)",
                (request.form["name"],
                 request.form["email"],
                 request.form["password"])
            )
            c.commit()
            c.close()
            return redirect("/login")
        except:
            return page("<div class='box'>Email already registered</div>")
    return page("""
    <div class="box">
    <h2>Register</h2>
    <form method="post">
    <input name="name" placeholder="Name" required>
    <input name="email" placeholder="Email" required>
    <input name="password" type="password" placeholder="Password" required>
    <button>Register</button>
    </form>
    </div>
    """)
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        c = db()
        u = c.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (request.form["email"],
             request.form["password"])
        ).fetchone()
        c.close()
        if u:
            session["user"] = u[0]
            return redirect("/")
        return page("<div class='box'>Invalid login</div>")
    return page("""
    <div class="box">
    <h2>Login</h2>
    <form method="post">
    <input name="email"
           placeholder="Email"
           required>
    <input name="password"
           type="password"
           placeholder="Password"
           required>
    <button>Login</button>
    </form>
    </div>
    """)
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
@app.route("/add/<int:i>")
def add(i):
    q = session.get("cart", {})
    q[str(i)] = q.get(str(i), 0) + 1
    session["cart"] = q
    return redirect("/cart")
@app.route("/remove/<int:i>")
def remove(i):
    q = session.get("cart", {})
    q.pop(str(i), None)
    session["cart"] = q
    return redirect("/cart")
@app.route("/cart")
def cart():
    q = session.get("cart", {})
    total = sum(
        p[2] * q.get(str(p[0]), 0)
        for p in P
    )
    items = ""
    for p in P:
        if q.get(str(p[0]), 0):
            items += f"""
            <div class="card">
            <h3>{p[1]}</h3>
            ₹{p[2]} × {q.get(str(p[0]),0)}
            <a href="/remove/{p[0]}">
            Remove
            </a>
            </div>
            """
    return page(f"""
    <div class="box">
    <h2>Cart</h2>
    {items}
    <h2>Total ₹{total}</h2>
    <a class="btn" href="/checkout">
    Payment
    </a>
    </div>
    """)
