const navegacion = document.querySelector('.responsive')
document.addEventListener('click', (e)=> {
    if(e.target.matches('img')){
        navegacion.classList.toggle('agregar')
    }else{
        navegacion.classList.remove('agregar')
    }
})

