(function(){var $=function(s){return document.querySelector(s)};
function sc(n,v,a){document.cookie=n+"="+v+"; max-age="+a+"; path=/; SameSite=Lax"}
var C={necessary:function(){sc("g3_session","s-"+Date.now(),86400)},
preferences:function(){sc("g3_theme","light",31536000);try{localStorage.setItem("g3_lang","en")}catch(e){}},
analytics:function(){sc("_ga_demo","GA1.2."+Math.floor(Math.random()*1e9),63072000);sc("_gid_demo","GA1.2."+Date.now(),86400)},
marketing:function(){sc("_fbp_demo","fb.1."+Date.now(),7776000);sc("g3_ads_demo","ad-"+Math.random().toString(36).slice(2,9),2592000);try{sessionStorage.setItem("g3_mkt","m-"+Date.now())}catch(e){}}};
function render(){$("#oc").textContent=document.cookie?document.cookie.split("; ").join("\n"):"(no cookies)";var s=[],i,k;
try{for(i=0;i<localStorage.length;i++){k=localStorage.key(i);s.push("local   "+k+" = "+localStorage.getItem(k))}}catch(e){}
try{for(i=0;i<sessionStorage.length;i++){k=sessionStorage.key(i);s.push("session "+k+" = "+sessionStorage.getItem(k))}}catch(e){}
$("#os").textContent=s.length?s.join("\n"):"(empty)";var dl=window.dataLayer||[];$("#od").textContent=dl.length?JSON.stringify(dl,null,1):"(empty)"}
[].forEach.call(document.querySelectorAll("[data-set]"),function(b){b.onclick=function(){C[b.dataset.set]();render()}});
$("#rf").onclick=render;$("#cl").onclick=function(){document.cookie.split("; ").forEach(function(c){var n=c.split("=")[0];if(n)document.cookie=n+"=; max-age=0; path=/"});try{localStorage.clear();sessionStorage.clear()}catch(e){}render()};
$("#yt").onclick=function(){$("#ytf").src="https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ"};
/* Fallback activator: call window.g3ApplyConsent({analytics:true,marketing:false}) from your CMP callback */
window.g3ApplyConsent=function(st){window.g3Consent=st||{};
[].forEach.call(document.querySelectorAll('script[type="text/plain"][data-consent-category]'),function(o){if(!st[o.dataset.consentCategory]||o.dataset.done)return;o.dataset.done=1;var s=document.createElement("script");s.text=o.text;o.parentNode.insertBefore(s,o.nextSibling);render()});
[].forEach.call(document.querySelectorAll("iframe[data-src]"),function(f){if(st[f.dataset.consentCategory])f.src=f.dataset.src})};
if(window.g3Consent)window.g3ApplyConsent(window.g3Consent);render();setInterval(render,3000)})();
