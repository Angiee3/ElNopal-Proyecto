
(()=>{
    let classes = ["f0", "f1", "f2", "f3", "f4"];
let classIndex = 2;

document.getElementById('aumentar').addEventListener('click', ()=>{
    let previousClass = classIndex;
    classIndex++;
    classIndex = (classIndex== classes.length) ? classes.length - 1: classIndex;
    changeClass(previousClass, classIndex ); 
});

document.getElementById('disminuir').addEventListener('click', ()=>{
    let previousClass = classIndex;
    classIndex--;
    classIndex = (classIndex < 0) ? 0 : classIndex;
    changeClass(previousClass, classIndex);
});

let changeClass = (previous, next)=>{
    if(previous != next){
        let htmlElement = document.querySelector('html');
        htmlElement.classList.remove(classes[previous]);
        htmlElement.classList.add(classes[next]);
        
    }
};
document.getElementById('restaurar').addEventListener( 'click', ()=>{
    location.reload();
});
changeClass()

let darktheme = ()=>{
    let selectores = document.querySelectorAll('[data-dark]')
    let cards = document.querySelectorAll('[data-cards]')
    const icons1 = document.getElementById('user');
    const icons2 = document.getElementById('carrito');
    const imagen = document.getElementById('nopal');
    const icons3 = document.getElementById('ayuda');
    const icons4 = document.getElementById('salir');
    const icons5 = document.querySelectorAll('#edit');
    const icons6 = document.querySelectorAll('#eliminar');
    const icons7 = document.querySelectorAll('#imprimir');
    const icons8 = document.querySelectorAll('#excel');
    const icons9 = document.querySelectorAll('#pdf');
    const icons10 = document.querySelectorAll('#mark');
    const icons11 = document.querySelectorAll('#plus');
    const icons12 = document.querySelectorAll('#eye');
    const icons13 = document.querySelectorAll('#closed');
    const textcolor = document.querySelectorAll('#texto');
    const textcolormodal = document.querySelectorAll('#textomodal');
    const mode_cards = document.querySelectorAll('#mode-cards')
    const modedark_admin = document.querySelectorAll('[data-admin]') 
    let colorTexto = document.querySelectorAll('[data-color]')
    document.addEventListener('click', (e)=>{
        if(e.target.matches('#dark')){
            selectores.forEach(item =>{
               if(item){
                if(item.classList.toggle('dark-mode')){
                    imagen ?  imagen.src = '/static/img/Logo-dark.png' : imagen
                    icons1 ? icons1.src = '/static/img/icons/userdark.svg' : icons1
                    icons2 ? icons2.src = '/static/img/icons/shopping-car-dark.svg' : icons2
                    icons3 ? icons3.src = '/static/img/icons/helpdark.svg' : icons3
                    icons4 ? icons4.src = '/static/img/icons/exitdark.svg' : icons4
                    console.log(colorTexto);
                    colorTexto ? colorTexto.forEach(item=>{item.classList.add('dark-mode')}) : colorTexto
                    if(icons5){
                        icons5.forEach(item=>{
                            item.src = '/static/img/icons/editdark.svg'
                        })
                    }
                    if(icons6){
                        icons6.forEach(item=>{
                            item.src = '/static/img/icons/deletedark.svg'
                        })
                    }
                    if(icons7){
                        icons7.forEach(item=>{
                            item.src = '/static/img/icons/printdark.svg'
                        })
                    }
                    if(icons8){
                        icons8.forEach(item=>{
                            item.src = '/static/img/icons/exceldark.svg'
                        })
                    }
                    if(icons9){
                        icons9.forEach(item=>{
                            item.src = '/static/img/icons/pdfdark.svg'
                        })
                    }
                    if(icons10){
                        icons10.forEach(item=>{
                            item.src = '/static/img/icons/markdark.svg'
                        })
                    }
                    if(icons11){
                        icons11.forEach(item=>{
                            item.src = '/static/img/icons/plusdark.svg'
                        })
                    }
                    if(icons12){
                        icons12.forEach(item=>{
                            item.src = '/static/img/icons/eyedark.svg'
                        })
                    }
                    if(icons13){
                        icons13.forEach(item=>{
                            item.src = '/static/img/icons/closedark.svg'
                        })
                    }
                    if(textcolor){
                        textcolor.forEach(item =>{
                            item.style.color='#fff'
                        })
                    }
                    if(textcolormodal){
                        textcolormodal.forEach(item =>{
                            item.style.color='#000'
                        })
                    }
                   if(mode_cards){
                    mode_cards.forEach(items=>{
                        items.classList.add('mode-cards')
                        console.log(items);
                    })
                   }
                }else{
                    imagen ? imagen.src = '/static/img/Logo.png' : imagen
                    icons1 ?  icons1.src = '/static/img/icons/user.svg' : icons1
                    icons2 ? icons2.src = '/static/img/icons/shopping-car.svg': icons2    
                    icons3 ? icons3.src = '/static/img/icons/help.svg' : icons3
                    icons4 ? icons4.src = '/static/img/icons/exit.svg' : icons4
                    colorTexto ? colorTexto.forEach(item=>{item.classList.remove('dark-mode')}) : colorTexto
                    if(icons5){
                        icons5.forEach(item=>{
                            item.src = '/static/img/icons/update.svg'
                        })
                    }
                    if(icons6){
                        icons6.forEach(item=>{
                            item.src = '/static/img/icons/delete.svg'
                        })
                    }
                    if(icons7){
                        icons7.forEach(item=>{
                            item.src = '/static/img/icons/print.svg'
                        })
                    }
                    if(icons8){
                        icons8.forEach(item=>{
                            item.src = '/static/img/icons/excel.svg'
                        })
                    }
                    if(icons9){
                        icons9.forEach(item=>{
                            item.src = '/static/img/icons/pdf.svg'
                        })
                    }
                    if(icons10){
                        icons10.forEach(item=>{
                            item.src = '/static/img/icons/mark.svg'
                        })
                    }
                    if(icons11){
                        icons11.forEach(item=>{
                            item.src = '/static/img/icons/plus.svg'
                        })
                    }
                    if(icons12){
                        icons12.forEach(item=>{
                            item.src = '/static/img/icons/eye.svg'
                        })
                    }
                    if(icons13){
                        icons13.forEach(item=>{
                            item.src = '/static/img/icons/close.svg'
                        })
                    }
                    if(textcolor){
                        textcolor.forEach(item =>{
                            item.style.color='#223016'
                        })
                    }
                    if(textcolormodal){
                        textcolormodal.forEach(item =>{
                            item.style.color='#fff'
                        })
                    }
                    if(mode_cards){
                        mode_cards.forEach(items=>{
                            items.classList.remove('mode-cards')
                            console.log(items);
                        })
                    }
                }
            }
            })
        }
        if(e.target.matches("#dark")){
           let fondo_contenedor = document.querySelector('#contenedor__productos') 
           fondo_contenedor ? fondo_contenedor.classList.toggle('mode-cards') : fondo_contenedor
        }
        if(e.target.matches('#dark')){
            if(cards){
                cards.forEach(items=>{
                    items.classList.toggle('mode-cards')
                })
            }
        }

        if(e.target.matches('#dark')){
            modedark_admin ? modedark_admin.forEach(item => { item.classList.toggle('dark-mode')}) : modedark_admin
        }
    })
    
    
}
darktheme();
})()