const menu = document.querySelector('.menu-toggle');
const nav = document.querySelector('#nav');
function closeMenu(){if(!menu||!nav)return;menu.setAttribute('aria-expanded','false');nav.classList.remove('is-open');}
if(menu&&nav){menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));nav.classList.toggle('is-open',open);});nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));document.addEventListener('keydown',event=>{if(event.key==='Escape'&&menu.getAttribute('aria-expanded')==='true'){closeMenu();menu.focus();}});window.matchMedia('(min-width: 601px)').addEventListener('change',closeMenu);}
document.querySelectorAll('[data-year]').forEach(el=>el.textContent=new Date().getFullYear());
