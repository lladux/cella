


function animacionHeader(){
    const animacion=document.getElementById('header-botones');
    
    if(!animacion.classList.contains('animacionHead-inicio')){
        animacion.classList.add('animacionHead-inicio')
        if(animacion.classList.contains('animacionHead-fin')){
            animacion.classList.remove('animacionHead-fin')
        }
    }else{
        animacion.classList.add("animacionHead-fin");
        animacion.classList.remove('animacionHead-inicio');
    }
}


function renombrar(viejoNombre,tipodato){`<input type='hidden' name='oldName' value='${viejoNombre}'> <input type='hidden' name='Tipo' value='${tipodato}'>`
    const formulario = document.getElementById("renombrarContext");
    
    if(tipodato==='dir'){

        formulario.innerHTML=`<input type='hidden' name='oldName' value='${viejoNombre}'> <input type='hidden' name='type' value='${tipodato}'>`;
    }else{
        formulario.innerHTML=`<input name='extension' checked type="checkbox">Mantener extencion</input> <input type='hidden' name='oldName' value='${viejoNombre}'> <input type='hidden' name='type' value='${tipodato}'>`;
    }
    window.renombrarMenu.showModal()
}




function FundirUp(){
    const inputDirUp = document.getElementById("dirUp");
    const divArvosLista= document.getElementById("listDataArchivos");
    let ListaArchivo='';
    Array.from(inputDirUp.files).forEach((i)=>{
        ListaArchivo=ListaArchivo+i.webkitRelativePath+'|';
    })
    
    
    divArvosLista.innerHTML=`<input name='listaArchvios' type='hidden' value='${ListaArchivo}' />`;
}