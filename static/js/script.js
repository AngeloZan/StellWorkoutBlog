function enableBodyScroll() {
    if (document.readyState === 'complete') {
      document.body.style.position = '';
      document.body.style.overflowY = '';
  
      if (document.body.style.marginTop) {
        const scrollTop = -parseInt(document.body.style.marginTop, 10);
        document.body.style.marginTop = '';
        window.scrollTo(window.pageXOffset, scrollTop);
      }
    } else {
      window.addEventListener('load', enableBodyScroll);
    }
}
  
function disableBodyScroll({ savePosition = false } = {}) {
    if (document.readyState === 'complete') {
        if (document.body.scrollHeight > window.innerHeight) {
        if (savePosition) document.body.style.marginTop = `-${window.pageYOffset}px`;
        document.body.style.position = 'fixed';
        document.body.style.overflowY = 'scroll';
        }
    } else {
        window.addEventListener('load', () => disableBodyScroll({ savePosition }));
    }
}

function closeMessages() {
    const messagesDiv = document.querySelector('#messages_div')
    messagesDiv.style.display = 'none'
}

const navSlide = () => {
    const burger = document.querySelector('.burger')
    const nav = document.querySelector('.nav-links')
    const navLinks = document.querySelectorAll('.nav-links li')
    const navBar = document.querySelector('#nav_bar')
    const isFixed = window.getComputedStyle(navBar, null).position == 'fixed'
    const content = document.querySelector('.content')
    const site = document.querySelector('.site')

    burger.addEventListener('click', ()=>{
        nav.classList.toggle('nav-active')

        if (! isFixed) {
            if (nav.classList.contains('nav-active')) {
                navBar.style.position = 'fixed'
                content.style.paddingTop = '4em'
                disableBodyScroll()
            } else {
                navBar.style.position = 'relative'
                content.style.paddingTop = '0'
                enableBodyScroll()
            }
        }

        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = ''
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.5}s`
            }
        })

        burger.classList.toggle('toggle')
    })    
}

const app = () => {
    navSlide()
}

app()
