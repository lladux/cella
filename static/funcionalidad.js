
function menuResponsive(){
    const animationMenu= document.getElementById('menuResponsiveID');
    if(!animationMenu.classList.contains('menuResponsive-Start')){
        animationMenu.classList.add('menuResponsive-Start');
        window.scrollTo(0,0)
        document.body.style.maxHeight='100vh';
        document.body.style.overflow='hidden'
        if(animationMenu.classList.contains('menuResponsive-End')){
            animationMenu.classList.remove('menuResponsive-End');
        }
    }else{
        document.body.style.maxHeight='auto';
        document.body.style.overflow='auto'
        animationMenu.classList.add("menuResponsive-End");
        animationMenu.classList.remove('menuResponsive-Start');
    }
}
//Save old name and type of data in inputs 
function rename(viejoNombre,tipodato){`<input type='hidden' name='oldName' value='${viejoNombre}'> <input type='hidden' name='Tipo' value='${tipodato}'>`
    const form = document.getElementById("renombrarContext");
    if(tipodato==='dir'){
        form.innerHTML=`<input type='hidden' name='oldName' value='${viejoNombre}'> <input type='hidden' name='type' value='${tipodato}'>`;
    }else{
        form.innerHTML=`<input name='extension' checked type="checkbox">Mantener extencion</input> <input type='hidden' name='oldName' value='${viejoNombre}'> <input type='hidden' name='type' value='${tipodato}'>`;
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