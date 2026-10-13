# G3 Shop - ecommerce test site for consent management

Pure static site (HTML/CSS/JS), no build needed. Relative paths, so it works from file://, Vercel, Netlify, GitHub Pages or nginx.

## Pages
index, shop (filter/sort/search), product, cart, checkout, thank-you, about, contact, privacy, cookie-policy, cookie-test (Cookie Lab), 404

## Structure
```
*.html  css/style.css  js/data.js (products)  js/app.js (cart/shop)  js/cookie-test.js
.well-known/privacyops-verification.txt   (ownership: well-known file)
dns/dns-records.txt                       (ownership: DNS TXT, add at DNS provider)
tools/build.py                            (regenerates all HTML, edit then: python3 tools/build.py)
```

## Ownership verification
1. Meta tag: in `<head>` of every page. 2. File: `/.well-known/privacyops-verification.txt`. 3. DNS TXT: see `dns/dns-records.txt`.

## Add your CMP
Paste your script in the marked slot in `<head>` (edit `tools/build.py` and rebuild, or find/replace in the HTML). Footer "Cookie Settings" calls `openCookieSettings()` in `js/app.js`; point it to your CMP API.

## Storage map (what to expect in your scan)
- Necessary: `g3_cart`, `g3_last_order` (localStorage), `g3_session`
- Preferences: `g3_recent`, `g3_theme`, `g3_lang`
- Analytics: `_ga_demo`, `_gid_demo`, plus `dataLayer` events (view_item, add_to_cart, search, purchase)
- Marketing: `_fbp_demo`, `g3_ads_demo`, YouTube and map iframes (data-src)
- Newsletter email: `g3_newsletter`

Change domain: `sed -i "s#g3cyberspace.com#YOUR-HOST#g" *.html sitemap.xml robots.txt`

## Deploy
Vercel: `vercel --prod` in this folder. VPS: copy with `cp -a` (keeps `.well-known`), serve with nginx.
