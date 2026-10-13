import os
T="pops-Ewq2haA3o4-ianZeFaJIA7dxcEqm1wP_"; D="https://g3cyberspace.com"
NAV=[("index.html","Home"),("shop.html","Shop"),("about.html","About"),("contact.html","Contact"),("cookie-test.html","Cookie Lab")]
def pg(f,title,key,body,foot="",data=True):
    nav="".join('<a href="%s"%s>%s</a>'%(a,' class="on"' if a==f else "",l) for a,l in NAV)
    h='''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s | G3 Shop</title>
<meta name="description" content="G3 Shop - demo ecommerce store for testing cookie consent management.">
<!-- OWNERSHIP VERIFICATION (method 1: HTML meta tag) -->
<meta name="privacyops-site-verification" content="%s">
<link rel="canonical" href="%s/%s">
<link rel="icon" type="image/svg+xml" href="img/favicon.svg">
<link rel="stylesheet" href="css/style.css">
<!-- ===== PASTE YOUR CONSENT MANAGEMENT (CMP) SCRIPT HERE, as the FIRST script ===== -->
<!-- <script src="https://YOUR-CMP-URL/banner.js" data-site-id="..."></script> -->
<!-- ===== END CMP SCRIPT ===== -->
</head>
<body data-page="%s">
<div class="topbar">Free shipping on orders over $75 &bull; Demo store, no real purchases</div>
<header class="site"><div class="wrap bar">
<a class="brand" href="index.html"><i>G3</i> Shop</a>
<button class="burger" aria-label="Menu" onclick="document.body.classList.toggle('open')">&#9776;</button>
<nav class="nav">%s</nav>
<form class="search" id="hs"><input id="hq" placeholder="Search products..." aria-label="Search"></form>
<a class="cartlink" href="cart.html">Cart<span class="badge">0</span></a>
</div></header>
<main>
%s
</main>
<footer class="site"><div class="wrap">
<div class="fg">
<div><h4>G3 Shop</h4><p>A fictional store built for testing cookie consent banners, preference centres and tracker blocking.</p></div>
<div><h4>Shop</h4><a href="shop.html?cat=Electronics">Electronics</a><a href="shop.html?cat=Fashion">Fashion</a><a href="shop.html?cat=Home">Home</a><a href="shop.html?cat=Sports">Sports</a></div>
<div><h4>Help</h4><a href="about.html">About</a><a href="contact.html">Contact</a><a href="cart.html">Cart</a><a href="cookie-test.html">Cookie Lab</a></div>
<div><h4>Legal</h4><a href="privacy.html">Privacy Policy</a><a href="cookie-policy.html">Cookie Policy</a><a href="#" class="opencs">Cookie Settings</a></div>
</div><div class="cp">&copy; 2026 G3 Shop (test site). All products are fictional.</div></div></footer>
<div id="toast"></div>
%s<script src="js/app.js"></script>
%s</body>
</html>
'''%(title,T,D,"" if f=="index.html" else f,key,nav,body,'<script src="js/data.js"></script>\n' if data else "",foot)
    open(f,"w").write(h)

pg("index.html","Home","home",'''<section class="hero"><div class="wrap"><div><h1>Everything you love. One simple store.</h1><p>Headphones, sneakers, home and fitness gear. A realistic shop to test your cookie consent flow end to end.</p><p><a class="btn alt" href="shop.html">Shop now</a> <a class="btn out" href="cookie-test.html">Cookie Lab</a></p></div><div class="art">🛍️</div></div></section>
<section class="blk"><div class="wrap"><h2>Shop by category</h2><div class="cats" id="cats"></div></div></section>
<section class="blk"><div class="wrap"><h2>Featured products</h2><div class="grid" id="feat"></div></div></section>
<section class="blk"><div class="wrap"><div class="perks"><div><b>🚚</b>Free delivery over $75</div><div><b>↩️</b>30-day returns</div><div><b>🔒</b>Secure checkout</div><div><b>💬</b>24/7 support</div></div></div></section>
<section class="blk"><div class="wrap"><div class="news"><h2>Join our newsletter</h2><p class="mu">Collects an email (personal data) for consent testing.</p><form id="newsf"><input id="newse" type="email" required placeholder="you@example.com"><button class="btn">Subscribe</button></form></div></div></section>''')

pg("shop.html","Shop","shop",'''<div class="wrap shop"><aside class="side"><h4>Categories</h4><div id="fcats"></div></aside>
<div><div class="tools"><b id="count"></b><select id="sort"><option value="">Featured</option><option value="lo">Price: low to high</option><option value="hi">Price: high to low</option><option value="rt">Top rated</option></select></div><div class="grid" id="list" style="grid-template-columns:repeat(3,1fr)"></div></div></div>''')

pg("product.html","Product","product",'''<div class="wrap"><div class="pd" id="pd"></div>
<h2>Related products</h2><div class="grid" id="rel"></div>
<h2 class="mt">Recently viewed <small class="mu">(stored in localStorage)</small></h2><div class="grid" id="rec"></div></div>''')

pg("cart.html","Cart","cart",'''<div class="wrap"><h1 style="margin-top:30px">Your cart</h1><div class="cartgrid"><div class="box" id="items"></div>
<div class="box"><h3 style="margin-top:0">Order summary</h3><div id="sum"></div><a class="btn block mt" id="go" href="checkout.html">Checkout</a></div></div></div>''')

pg("checkout.html","Checkout","checkout",'''<div class="wrap"><h1 style="margin-top:30px">Checkout</h1><div class="cartgrid"><form class="box form" id="cf">
<h3 style="margin-top:0">Shipping details</h3><div class="f2"><label>First name<input required></label><label>Last name<input required></label></div>
<label>Email<input type="email" required></label><label>Phone<input type="tel"></label><label>Address<input required></label>
<div class="f2"><label>City<input required></label><label>Postal code<input required></label></div>
<h3>Payment (demo only)</h3><label>Card number<input placeholder="4242 4242 4242 4242" inputmode="numeric"></label>
<div class="f2"><label>Expiry<input placeholder="MM/YY"></label><label>CVC<input placeholder="123"></label></div>
<label class="chk"><input type="checkbox" required> I accept the <a href="privacy.html">Privacy Policy</a></label>
<button class="btn block">Place order</button></form>
<div class="box"><h3 style="margin-top:0">Summary</h3><div id="osum"></div><p class="mu">No real payment is taken. Do not enter real card data.</p></div></div></div>''')

pg("thank-you.html","Thank you","thanks",'''<div class="wrap page" style="text-align:center"><div style="font-size:80px">🎉</div><h1>Thank you for your order!</h1><p>Order <b id="oid"></b> total <b id="ot"></b> (demo).</p><a class="btn" href="shop.html">Continue shopping</a></div>''')

pg("about.html","About","about",'''<div class="wrap page prose"><h1>About G3 Shop</h1><p>G3 Shop is a fictional online store created to test cookie consent management platforms (CMPs). It includes a product catalogue, cart, checkout, newsletter, embeds and a Cookie Lab so you can verify banner behaviour, category blocking, consent logging and preference changes.</p><p>All names, prices and products are placeholders.</p></div>''')

pg("contact.html","Contact","contact",'''<div class="wrap page"><h1>Contact us</h1><div class="g2"><form class="box form" onsubmit="event.preventDefault();document.getElementById('ok').hidden=false">
<label>Name<input required></label><label>Email<input type="email" required></label><label>Message<textarea rows="4"></textarea></label>
<label class="chk"><input type="checkbox" required> I agree to the <a href="privacy.html">Privacy Policy</a></label><button class="btn">Send</button><p id="ok" class="ok" hidden>Sent (demo, nothing transmitted).</p></form>
<div class="box"><h3 style="margin-top:0">Visit us</h3><p>Chennai, Tamil Nadu, India (fictional)</p><iframe class="embed" title="Map" loading="lazy" data-consent-category="marketing" src="about:blank" data-src="https://www.openstreetmap.org/export/embed.html?bbox=80.20,13.00,80.30,13.10&amp;layer=mapnik"></iframe><p class="mu">Loads after consent when your CMP unblocks it (or via g3ApplyConsent).</p></div></div></div>''',data=False)

pg("privacy.html","Privacy Policy","privacy",'''<div class="wrap page prose"><h1>Privacy Policy</h1><p class="mu">Template text. Last updated October 2026.</p>
<h2>Who we are</h2><p>G3 Shop is a fictional store operating this demo site.</p>
<h2>Data we collect</h2><p>Order and shipping details, contact form and newsletter emails, plus device and usage data via analytics and marketing cookies, only with your consent.</p>
<h2>Legal bases</h2><p>Contract (orders), consent (non-essential cookies), legitimate interest (security).</p>
<h2>Your rights</h2><p>Access, correction, deletion, restriction, portability, objection, and withdrawing consent at any time through Cookie Settings in the footer.</p>
<h2>Retention</h2><p>Orders: 7 years. Newsletter: until you unsubscribe. Analytics: 14 months. Marketing: 90 days.</p>
<h2>Contact</h2><p>privacy@g3cyberspace.com (placeholder)</p></div>''',data=False)

pg("cookie-policy.html","Cookie Policy","cookiepolicy",'''<div class="wrap page prose"><h1>Cookie Policy</h1><div style="overflow-x:auto"><table><thead><tr><th>Name</th><th>Category</th><th>Purpose</th><th>Duration</th></tr></thead><tbody>
<tr><td>g3_session</td><td>Necessary</td><td>Session</td><td>1 day</td></tr>
<tr><td>g3_cart (localStorage)</td><td>Necessary</td><td>Shopping cart</td><td>Persistent</td></tr>
<tr><td>g3_theme, g3_lang, g3_recent</td><td>Preferences</td><td>Remember choices and recently viewed items</td><td>1 year</td></tr>
<tr><td>_ga_demo, _gid_demo</td><td>Analytics</td><td>Dummy analytics IDs</td><td>2 years / 1 day</td></tr>
<tr><td>_fbp_demo, g3_ads_demo</td><td>Marketing</td><td>Dummy ad IDs</td><td>90 / 30 days</td></tr></tbody></table></div>
<p>Change your choices anytime: <a href="#" class="opencs">Cookie Settings</a>.</p></div>''',data=False)

pg("404.html","Not found","404",'''<div class="wrap page" style="text-align:center"><div style="font-size:80px">🧭</div><h1>404 - Page not found</h1><a class="btn" href="index.html">Back to home</a></div>''',data=False)

pg("cookie-test.html","Cookie Lab","lab",'''<div class="wrap page"><h1>Cookie Lab</h1><p class="mu">Set dummy cookies, load trackers and verify your consent banner blocks or allows them.</p>
<div class="box"><h3 style="margin-top:0">1. Live state</h3><button class="btn sm" id="rf">Refresh</button> <button class="btn sm out" id="cl">Clear all cookies &amp; storage</button>
<div class="g2 mt"><div><b>document.cookie</b><pre id="oc"></pre></div><div><b>localStorage / sessionStorage</b><pre id="os"></pre></div></div><b>dataLayer (shop events)</b><pre id="od"></pre></div>
<div class="box mt"><h3 style="margin-top:0">2. Set cookies by category</h3><button class="btn sm" data-set="necessary">Necessary</button> <button class="btn sm" data-set="preferences">Preferences</button> <button class="btn sm" data-set="analytics">Analytics</button> <button class="btn sm" data-set="marketing">Marketing</button></div>
<div class="box mt"><h3 style="margin-top:0">3. Consent-gated scripts</h3><p class="mu">Tags use <code>type="text/plain"</code> and <code>data-consent-category</code>; a CMP should switch them on after consent.</p>
<table><thead><tr><th>Tracker</th><th>Category</th><th>Status</th></tr></thead><tbody><tr><td>Dummy Analytics</td><td>analytics</td><td id="st-analytics">blocked</td></tr><tr><td>Dummy Pixel</td><td>marketing</td><td id="st-marketing">blocked</td></tr></tbody></table></div>
<div class="box mt"><h3 style="margin-top:0">4. Third-party embed</h3><button class="btn sm" id="yt">Load YouTube</button><iframe id="ytf" class="embed" title="YouTube" data-consent-category="marketing" src="about:blank"></iframe></div>
<div class="box mt"><h3 style="margin-top:0">5. Checklist</h3><ul><li>Banner shows before any non-essential cookie is set</li><li>Reject all keeps only necessary storage (cart still works)</li><li>Accept all enables analytics and marketing</li><li>Granular toggles work; choice persists across pages</li><li>Footer Cookie Settings reopens the preference centre</li><li>Withdrawing consent removes cookies</li><li>Ownership verified: meta, well-known, DNS TXT</li></ul></div></div>''',
'''<script type="text/plain" data-consent-category="analytics">document.cookie="_ga_demo=GA1.2.123456789; max-age=63072000; path=/; SameSite=Lax";document.cookie="_gid_demo=GA1.2.987654; max-age=86400; path=/";var e=document.getElementById("st-analytics");if(e){e.textContent="RUNNING";e.className="ok"}</script>
<script type="text/plain" data-consent-category="marketing">document.cookie="_fbp_demo=fb.1.1700000000.111; max-age=7776000; path=/";document.cookie="g3_ads_demo=ad-"+Math.random().toString(36).slice(2,9)+"; max-age=2592000; path=/";var e=document.getElementById("st-marketing");if(e){e.textContent="RUNNING";e.className="ok"}</script>
<script src="js/cookie-test.js"></script>
''',data=False)

urls=[f for f in os.listdir(".") if f.endswith(".html") and f not in("404.html","thank-you.html","checkout.html")]
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join('<url><loc>%s/%s</loc></url>\n'%(D,"" if u=="index.html" else u) for u in sorted(urls))+'</urlset>\n')
open("robots.txt","w").write("User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n"%D)
open(".well-known/privacyops-verification.txt","w").write(T)
open("dns/dns-records.txt","w").write('''# OWNERSHIP VERIFICATION (method 3: DNS TXT) - add at your DNS provider
Type : TXT
Name : _privacyops-challenge   (full: _privacyops-challenge.g3cyberspace.com)
Value: privacyops-site-verification=%s
TTL  : 300

# Verify:  dig TXT _privacyops-challenge.g3cyberspace.com +short
'''%T)
print("ok")
