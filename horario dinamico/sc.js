function carregar(){        
    var msg = document.getElementById('msg')//pega o id para permitir modificações
    var img = document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()//pega o hoario
    msg.innerHTML = `Agora sao ${hora} horas.`
    if (hora >= 0 && hora < 12 ){//inicio do aninhamento
        //bom dia
        img.src ='img/manha.png'
        document.body.style.background='#e7bf93'
        
    }else if( hora >= 12 && hora < 18){
        //boa tarde
        img.src ='img/tarde.png'
        document.body.style.background='#694024'
    }else{
        //boa noite
        img.src ='img/noite.png'
        document.body.style.background = '#042025'
    }//fim do aninhamento

}