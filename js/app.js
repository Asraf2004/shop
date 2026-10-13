/* G3 Shop - storefront logic. Cart uses localStorage (strictly necessary). */
var $=function(s,r){return(r||document).querySelector(s)},$$=function(s,r){return[].slice.call((r||document).querySelectorAll(s))};
var money=function(n){return"$"+n.toFixed(2)};
var find=function(id){return PRODUCTS.filter(function(p){return p.id==id})[0]};
var Store={
 get:function(k,d){try{return JSON.parse(localStorage.getItem(k))||d}catch(e){return d}},
 set:function(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}
};
var cart=function(){return Store.get("g3_cart",[])};
function saveCart(c){Store.set("g3_cart",c);badge()}
function badge(){var n=cart().reduce(function(a,i){return a+i.q},0);$$(".badge").forEach(function(b){b.textContent=n})}
function toast(m){var t=$("#toast");t.textContent=m;t.className="on";clearTimeout(t._t);t._t=setTimeout(function(){t.className=""},1800)}
/* Analytics hook: pushes to dataLayer. Your CMP / GTM decides whether it is allowed. */
function track(ev,data){window.dataLayer=window.dataLayer||[];var o={event:ev};for(var k in data)o[k]=data[k];window.dataLayer.push(o)}
function add(id,q){var c=cart(),i=c.filter(function(x){return x.id==id})[0];if(i)i.q+=q||1;else c.push({id:id,q:q||1});saveCart(c);var p=find(id);toast(p.name+" added to cart");track("add_to_cart",{item:p.name,value:p.price})}
function stars(r){var f=Math.round(r);return"★★★★★".slice(0,f)+"☆☆☆☆☆".slice(0,5-f)+" <span class='mu'>"+r+"</span>"}
function card(p){return'<div class="pc"><a href="product.html?id='+p.id+'"><div class="pimg" style="background:'+p.c+'">'+p.e+'</div></a><div class="pb">'+(p.old?'<span class="tag">SALE</span>':'')+'<h3><a href="product.html?id='+p.id+'">'+p.name+'</a></h3><div class="stars">'+stars(p.r)+'</div><div class="price">'+money(p.price)+(p.old?'<s>'+money(p.old)+'</s>':'')+'</div><button class="btn sm" onclick="add('+p.id+')">Add to cart</button></div></div>'}
var page=document.body.dataset.page;
var R={
 home:function(){
  $("#feat").innerHTML=PRODUCTS.slice(0,8).map(card).join("");
  $("#cats").innerHTML=CATS.map(function(c){return'<a class="cat" href="shop.html?cat='+c[0]+'"><b>'+c[1]+'</b>'+c[0]+'</a>'}).join("");
  $("#newsf").onsubmit=function(e){e.preventDefault();Store.set("g3_newsletter",{email:$("#newse").value,at:Date.now()});toast("Subscribed (demo)");this.reset()};
 },
 shop:function(){
  var q=new URLSearchParams(location.search),cat=q.get("cat")||"",term=q.get("q")||"";
  $("#fcats").innerHTML='<label><input type="radio" name="c" value=""'+(cat?'':' checked')+'> All</label>'+CATS.map(function(c){return'<label><input type="radio" name="c" value="'+c[0]+'"'+(cat==c[0]?' checked':'')+'> '+c[0]+'</label>'}).join("");
  function draw(){var c=($("input[name=c]:checked")||{}).value||"",s=$("#sort").value,t=($("#hq").value||term).toLowerCase();
   var l=PRODUCTS.filter(function(p){return(!c||p.cat==c)&&(!t||p.name.toLowerCase().indexOf(t)>-1)});
   if(s=="lo")l.sort(function(a,b){return a.price-b.price});if(s=="hi")l.sort(function(a,b){return b.price-a.price});if(s=="rt")l.sort(function(a,b){return b.r-a.r});
   $("#count").textContent=l.length+" products";$("#list").innerHTML=l.map(card).join("")||"<p>No products found.</p>";
   if(t)track("search",{term:t})}
  $$("input[name=c]").forEach(function(i){i.onchange=draw});$("#sort").onchange=draw;$("#hq").value=term;$("#hq").oninput=draw;draw();
 },
 product:function(){
  var p=find(new URLSearchParams(location.search).get("id"))||PRODUCTS[0];document.title=p.name+" | G3 Shop";
  var rv=Store.get("g3_recent",[]).filter(function(i){return i!=p.id});rv.unshift(p.id);Store.set("g3_recent",rv.slice(0,4)); /* preferences-type storage */
  track("view_item",{item:p.name,value:p.price});
  $("#pd").innerHTML='<div class="big" style="background:'+p.c+'">'+p.e+'</div><div><span class="mu">'+p.cat+'</span><h1>'+p.name+'</h1><div class="stars">'+stars(p.r)+'</div><p class="price" style="font-size:28px">'+money(p.price)+(p.old?'<s>'+money(p.old)+'</s>':'')+'</p><p>'+p.d+'</p><p><span class="qty"><button onclick="qd(-1)">−</button><span id="q">1</span><button onclick="qd(1)">+</button></span></p><button class="btn" onclick="add('+p.id+',+$(\'#q\').textContent)">Add to cart</button> <a class="btn out" href="cart.html">View cart</a><p class="mu mt">Free shipping over $75 · 30-day returns</p></div>';
  $("#rel").innerHTML=PRODUCTS.filter(function(x){return x.cat==p.cat&&x.id!=p.id}).slice(0,4).map(card).join("");
  var rc=rv.filter(function(i){return i!=p.id}).map(find);$("#rec").innerHTML=rc.length?rc.map(card).join(""):"<p class='mu'>Nothing yet.</p>";
 },
 cart:function(){draw()},
 checkout:function(){
  var c=cart();if(!c.length){location="cart.html";return}
  $("#osum").innerHTML=sum(c);
  $("#cf").onsubmit=function(e){e.preventDefault();var id="G3-"+Math.floor(Math.random()*9e5+1e5),t=total(c);
   Store.set("g3_last_order",{id:id,total:t,items:c.length});track("purchase",{order:id,value:t});saveCart([]);location="thank-you.html"};
 },
 thanks:function(){var o=Store.get("g3_last_order",{});$("#oid").textContent=o.id||"G3-000000";$("#ot").textContent=o.total?money(o.total):""}
};
function total(c){var s=c.reduce(function(a,i){return a+find(i.id).price*i.q},0);return s+(s>75||!s?0:6.99)}
function sum(c){var s=c.reduce(function(a,i){return a+find(i.id).price*i.q},0),sh=s>75||!s?0:6.99;return'<div class="row"><span>Subtotal</span><span>'+money(s)+'</span></div><div class="row"><span>Shipping</span><span>'+(sh?money(sh):"Free")+'</span></div><div class="row tot"><span>Total</span><span>'+money(s+sh)+'</span></div>'}
function qd(n){var e=$("#q");e.textContent=Math.max(1,+e.textContent+n)}
function chg(id,n){var c=cart();c.forEach(function(i){if(i.id==id)i.q+=n});saveCart(c.filter(function(i){return i.q>0}));draw()}
function draw(){var c=cart();$("#items").innerHTML=c.length?c.map(function(i){var p=find(i.id);return'<div class="ci"><div class="t" style="background:'+p.c+'">'+p.e+'</div><div><b>'+p.name+'</b><div class="mu">'+money(p.price)+'</div></div><span class="qty"><button onclick="chg('+p.id+',-1)">−</button><span>'+i.q+'</span><button onclick="chg('+p.id+',1)">+</button></span><b>'+money(p.price*i.q)+'</b></div>'}).join(""):'<p>Your cart is empty. <a href="shop.html">Start shopping</a></p>';$("#sum").innerHTML=sum(c);$("#go").style.display=c.length?"block":"none"}
/* Header search + footer cookie-settings wiring */
function openCookieSettings(e){if(e)e.preventDefault();var w=window;
 if(typeof w.openPrivacyOpsPreferences==="function")return w.openPrivacyOpsPreferences();
 if(w.PrivacyOps&&w.PrivacyOps.showPreferences)return w.PrivacyOps.showPreferences();
 if(w.__cmp)return w.__cmp("showPreferences");
 alert("No CMP preference centre found. Wire openCookieSettings() in js/app.js to your CMP.")}
document.addEventListener("DOMContentLoaded",function(){
 badge();$$(".opencs").forEach(function(a){a.onclick=openCookieSettings});
 var hs=$("#hs");if(hs)hs.onsubmit=function(e){e.preventDefault();location="shop.html?q="+encodeURIComponent($("#hq").value)};
 if(R[page])R[page]();
});
