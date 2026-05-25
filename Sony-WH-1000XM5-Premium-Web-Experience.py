
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sony WH-1000XM5</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&display=swap" rel="stylesheet">

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    scroll-behavior:smooth;
}

body{
    font-family:'Poppins',sans-serif;
    background:#050505;
    color:white;
    overflow-x:hidden;
}

body::before{
    content:"";
    position:fixed;
    width:600px;
    height:600px;
    background:radial-gradient(circle,#3d1cff55,transparent 70%);
    top:-200px;
    left:-100px;
    z-index:-1;
    animation:float1 8s ease-in-out infinite;
}

body::after{
    content:"";
    position:fixed;
    width:500px;
    height:500px;
    background:radial-gradient(circle,#00c3ff33,transparent 70%);
    bottom:-200px;
    right:-100px;
    z-index:-1;
    animation:float2 10s ease-in-out infinite;
}

@keyframes float1{
    0%,100%{transform:translateY(0px);}
    50%{transform:translateY(40px);}
}

@keyframes float2{
    0%,100%{transform:translateY(0px);}
    50%{transform:translateY(-40px);}
}

nav{
    width:100%;
    position:fixed;
    top:0;
    z-index:999;
    backdrop-filter:blur(20px);
    background:rgba(0,0,0,0.35);
    padding:20px 8%;
    display:flex;
    justify-content:space-between;
    align-items:center;
}

nav h1{
    font-size:1.5rem;
    letter-spacing:2px;
}

nav a{
    color:white;
    text-decoration:none;
    margin-left:20px;
    transition:0.3s;
}

nav a:hover{
    color:#8a7dff;
}

.hero{
    min-height:100vh;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:120px 10%;
    gap:40px;
}

.hero-text{
    max-width:600px;
}

.hero-text h2{
    font-size:5rem;
    line-height:1;
    margin-bottom:20px;
    opacity:0;
    transform:translateY(60px);
    animation:fadeUp 1s forwards;
}

.hero-text p{
    font-size:1.1rem;
    color:#d6d6d6;
    line-height:1.8;
    opacity:0;
    transform:translateY(60px);
    animation:fadeUp 1s 0.3s forwards;
}

.hero-text button{
    margin-top:30px;
    padding:15px 35px;
    border:none;
    border-radius:50px;
    background:linear-gradient(90deg,#8b5cf6,#00d4ff);
    color:white;
    font-size:1rem;
    cursor:pointer;
    transition:0.4s;
    opacity:0;
    transform:translateY(60px);
    animation:fadeUp 1s 0.6s forwards;
}

.hero-text button:hover{
    transform:scale(1.08);
    box-shadow:0 0 30px #6d5cff;
}

.hero-img{
    position:relative;
}

.hero-img img{
    width:520px;
    animation:floatHeadphones 5s ease-in-out infinite;
    transition:0.4s;
    filter:drop-shadow(0 0 30px rgba(140,120,255,0.4));
}

.hero-img img:hover{
    transform:scale(1.05) rotate(-4deg);
}

@keyframes floatHeadphones{
    0%,100%{transform:translateY(0px);}
    50%{transform:translateY(-25px);}
}

@keyframes fadeUp{
    to{
        opacity:1;
        transform:translateY(0);
    }
}

.section{
    padding:120px 10%;
}

.section-title{
    text-align:center;
    margin-bottom:70px;
    opacity:0;
    transform:translateY(40px);
    transition:1s;
}

.section-title.show{
    opacity:1;
    transform:translateY(0);
}

.section-title h3{
    font-size:3rem;
}

.cards{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
    gap:30px;
}

.card{
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:30px;
    padding:30px;
    backdrop-filter:blur(20px);
    transition:0.5s;
    opacity:0;
    transform:translateY(60px);
}

.card.show{
    opacity:1;
    transform:translateY(0);
}

.card:hover{
    transform:translateY(-10px) scale(1.03);
    box-shadow:0 0 40px rgba(138,125,255,0.2);
}

.card img{
    width:100%;
    margin-bottom:20px;
    transition:0.4s;
}

.card img:hover{
    transform:scale(1.08) rotate(3deg);
}

.card h4{
    font-size:1.5rem;
    margin-bottom:15px;
}

.card p{
    color:#c8c8c8;
    line-height:1.7;
}

.gallery{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
    gap:25px;
}





.specs{
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:25px;
}

.spec{
    width:220px;
    padding:30px;
    border-radius:25px;
    background:rgba(255,255,255,0.05);
    text-align:center;
    transition:0.4s;
}

.spec:hover{
    transform:translateY(-10px);
    background:rgba(138,125,255,0.15);
}

.spec h2{
    font-size:2.5rem;
    margin-bottom:10px;
    color:#8a7dff;
}

.order-form{
    max-width:700px;
    margin:auto;
    background:rgba(255,255,255,0.05);
    padding:50px;
    border-radius:35px;
    backdrop-filter:blur(25px);
}

form{
    display:flex;
    flex-direction:column;
    gap:20px;
}

input, textarea{
    padding:18px;
    border:none;
    border-radius:18px;
    background:rgba(255,255,255,0.08);
    color:white;
    font-size:1rem;
    outline:none;
}

textarea{
    min-height:120px;
    resize:none;
}

form button{
    padding:18px;
    border:none;
    border-radius:20px;
    background:linear-gradient(90deg,#8b5cf6,#00d4ff);
    color:white;
    font-size:1rem;
    cursor:pointer;
    transition:0.4s;
}

form button:hover{
    transform:scale(1.03);
    box-shadow:0 0 25px #6d5cff;
}

footer{
    text-align:center;
    padding:40px;
    color:#888;
}

.reveal{
    opacity:0;
    transform:translateY(60px);
    transition:1s;
}

.reveal.active{
    opacity:1;
    transform:translateY(0);
}

@media(max-width:900px){
    .hero{
        flex-direction:column;
        text-align:center;
    }

    .hero-text h2{
        font-size:3.5rem;
    }

    .hero-img img{
        width:100%;
        max-width:420px;
    }
}
</style>
</head>
<body>

<nav>
    <h1>SONY WH-1000XM5</h1>

    <div>
        <a href="#features">Features</a>
        <a href="#specs">Specs</a>
        <a href="#order">Order</a>
    </div>
</nav>

<section class="hero">
    <div class="hero-text">
        <h2>Experience Pure Silence</h2>

        <p>
            The Sony WH‑1000XM5 delivers legendary noise cancellation,
            cinematic sound quality, premium comfort, and futuristic design.
            Built for music lovers, night workers, creators, and dreamers.
        </p>

        <button onclick="document.getElementById('order').scrollIntoView()">
            Order Now
        </button>
    </div>

    <div class="hero-img">
        <img src="https://d2q01ftr6ua4w.cloudfront.net/assets/images/153cf6a7709f026bcb9ffafa7178c5ade9ce0fc7.png?t=1704870249">
    </div>
</section>

<section class="section" id="features">
    <div class="section-title reveal">
        <h3>Premium Features</h3>
    </div>

    <div class="cards">
        <div class="card reveal">
            <img src="https://gearsforears.com/cdn/shop/products/61prknFwvJL._AC_SL1500_1600x.jpg?v=1660258151">
            <h4>Industry Leading ANC</h4>
            <p>
                Immerse yourself in complete silence with intelligent adaptive
                noise cancellation powered by Sony's advanced processors.
            </p>
        </div>

        <div class="card reveal">
            <img src="https://gagadget.com/media/post_big/Sony_WH-1000XM5.png">
            <h4>Studio Quality Audio</h4>
            <p>
                Feel every detail with rich bass, crystal highs, and ultra-clean
                wireless sound tuned for perfection.
            </p>
        </div>

        <div class="card reveal">
            <img src="https://images.squarespace-cdn.com/content/v1/55787f0ae4b02f0501debbeb/1653409665430-PF5HN4WGKJIU30WFBU64/a.png?format=1000w">
            <h4>30 Hours Battery</h4>
            <p>
                Enjoy all-day listening with ultra-fast charging and incredible
                battery endurance built for modern life.
            </p>
        </div>
    </div>
</section>



<section class="section" id="specs">
    <div class="section-title reveal">
        <h3>Specifications</h3>
    </div>

    <div class="specs">
        <div class="spec reveal">
            <h2>30h</h2>
            <p>Battery Life</p>
        </div>

        <div class="spec reveal">
            <h2>LDAC</h2>
            <p>Hi‑Res Audio</p>
        </div>

        <div class="spec reveal">
            <h2>ANC</h2>
            <p>Noise Cancellation</p>
        </div>

        <div class="spec reveal">
            <h2>BT 5.2</h2>
            <p>Wireless Connection</p>
        </div>
    </div>
</section>

<section class="section" id="order">
    <div class="section-title reveal">
        <h3>Order Your Sony WH‑1000XM5</h3>
    </div>

    <div class="order-form reveal">
        <form method="POST">
            <input type="text" name="name" placeholder="Your Name" required>

            <input type="email" name="email" placeholder="Your Email" required>

            <input type="text" name="address" placeholder="Shipping Address" required>

            <textarea name="message" placeholder="Additional Notes"></textarea>

            <button type="submit">Place Order</button>
        </form>
    </div>
</section>

<footer>
    Sony WH‑1000XM5 — Designed for Night Listening ✨
</footer>

<script>
const reveals = document.querySelectorAll('.reveal');

window.addEventListener('scroll', () => {
    reveals.forEach(reveal => {
        const windowHeight = window.innerHeight;
        const revealTop = reveal.getBoundingClientRect().top;

        if(revealTop < windowHeight - 100){
            reveal.classList.add('active');
            reveal.classList.add('show');
        }
    });
});

document.querySelectorAll('.gallery img').forEach(img => {
    img.addEventListener('mousemove', (e) => {
        const x = e.offsetX / img.clientWidth;
        const y = e.offsetY / img.clientHeight;

        img.style.transform =
            `perspective(1000px) rotateY(${(x - 0.5) * 10}deg)
             rotateX(${(0.5 - y) * 10}deg) scale(1.05)`;
    });

    img.addEventListener('mouseleave', () => {
        img.style.transform = 'perspective(1000px) rotateY(0deg) rotateX(0deg)';
    });
});
</script>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        return f"""
        <body style='background:#050505;color:white;font-family:Poppins;padding:100px;text-align:center;'>
            <h1>Thank You, {name}!</h1>
            <p>Your Sony WH‑1000XM5 order request has been received.</p>
            <a href="/" style='color:#8a7dff;'>Go Back</a>
        </body>
        """
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
