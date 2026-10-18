(function(){
  var root=document.documentElement,btn=document.getElementById('theme');
  var modes=['auto','light','dark'],labels={auto:'🌗 Auto',light:'☀️ Claro',dark:'🌙 Oscuro'};
  var m='auto';try{m=localStorage.getItem('theme')||'auto'}catch(e){}
  function apply(){if(m==='auto')root.removeAttribute('data-theme');else root.setAttribute('data-theme',m);btn.textContent=labels[m]}
  btn.addEventListener('click',function(){m=modes[(modes.indexOf(m)+1)%3];try{localStorage.setItem('theme',m)}catch(e){}apply()});
  apply();document.getElementById('y').textContent=new Date().getFullYear();
})();
