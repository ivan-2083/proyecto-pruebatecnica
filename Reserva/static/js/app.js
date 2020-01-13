var arreglo = []

$("#formulario").submit(function(){
    var respuestas = $(this).serializeObject();
    //agrego al formulario
    arreglo.push(respuestas)
    $("#arreglo").html("")
    arreglo.forEach(elemento => {
        console.log(elemento)
        $("#arreglo").append
                       ('<div class="col-md-2">'+
                        '<img class="img-fluid" src="'+elemento.foto+'" alt="" srcset="">'+
                        '<h6>'+elemento.correo+'</h6>'+
                        '<p>'+elemento.pais+'</p>'+
                        '</div>')
    });

    return false;
})

// MDB Lightbox Init
$(function () {
    $("#mdb-lightbox-ui").load("mdb-addons/mdb-lightbox-ui.html");
});

$.fn.serializeObject = function() {
 var o = {};
 var a = this.serializeArray();
    $.each(a, function() {
    if (o[this.name]) {
    if (!o[this.name].push) {
    o[this.name] = [o[this.name]];
    }
    o[this.name].push(this.value || '');
    } else {
    o[this.name] = this.value || '';
    }
    });
    return o;
 };

 //Validaciones de Registro
 $(function(){
    $("#formulariousers").validate({
        rules:{
            correo:{
                required:true,
                email: true
            },
            run:{
                required:true
            },
            nombre:{
                required: true
            },
            fnacimiento:{
                required: true
            },
            region:{
                required: true
            },
            comuna:{
                required: true
            },
            raza:{
                required: true
            },
            descripcion:{
                required: true
            },
        },
        messages:{
            correo:{
                required:"Debe ingresar su correo",
                email: "Debe ingresar un correo de formato correcto"
            },
            run:{
                required:"Debe ingresar su RUN"
            },
            nombre:{
                required:"Debe ingresar su nombre",
            },
            fnacimiento:{
                required:"Debe ingresar su fecha de nacimiento",
                max: "Se debe ser mayor de 18 anos"
            },
            telefono:{
                pattern:"Ingrese un numero valido"
            },
            raza:{
                required:"Debe ingresar una raza"
            },
            descripcion:{
                required:"Debe ingresar una descripcion"
            },
        }
    })
    
})

// Solo admite letras en el Nombre
$(document).ready(function(){
    $("#soloLetras").keypress(function(event){
        var inputValue = event.which;
        if(!(inputValue >= 65 && inputValue <= 122) && (inputValue != 32 && inputValue != 0)) { 
            event.preventDefault(); 
        }
    });
});

//Comunas y regiones de chile
$('#region').geoRegionalizacion({
    regionDependiente: '#comuna'
});

//Validacion de Rut
$('.input_rut').rut();
 //Validaciones de Registro