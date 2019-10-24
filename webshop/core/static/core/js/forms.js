
	
	//var telefono = parseInt(tel, 10);
/*function enviar () {
	$('#formulario').submit(function(e) {
        e.preventDefault();
        console.log(nombre);
     $.ajax({
         data: {'nombre': nombre,
                'correo':correo,
                'telefono': 456,
                'mensaje': mensaje},
         url: 'mensajes/',
         type: 'POST',
         success : function(data) {
                console.log(data[3]);
         },
         error : function(message) {
                 console.log(message);
                 console.log("Hubo error en el ajax");
              }
         });
        }); 
}*/

$( document ).ready(function() {
	$('#formulario').submit(function(e) {
        e.preventDefault();
        var nombre = $("#nom").val();
		var correo = $("#correo").val();
		var tel = $("#telefono").val();
		var mensaje = $("#mensaje").val();
		var lista = [nombre,correo,tel,mensaje];
		var obj = {"nombre":nombre, "correo":correo,"tel":tel,"mensaje":mensaje};
     $.ajax({
         data: {'lista':JSON.stringify(obj)},
         url: 'mensajes/',
         type: 'POST',
         success : function(data) {
                $("#resultado").html(data);
                $("#nom").val("");
                $("#correo").val("");
                $("#telefono").val("");
                $("#mensaje").val("");
                $("#resultado").css({
                	display:'block'
                });
         },
         error : function(message) {
                 console.log(message);
                 console.log("Hubo error en el ajax");
              }
         });
        });
	$('#nom,#correo,#telefono,#mensaje').keyup(function(event) {
		$("#resultado").css({
                	display:'none'
                });
	});
});
