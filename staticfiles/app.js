(function($) {
    $(document).ready(function() {
        $("#id_fnacimiento").datepicker( { dateFormat: 'yy-mm-dd',changeMonth: true,changeYear: true,yearRange :  'c-113:c' } );
        //$("#id_codigo_postal").attr('disable','disable');

     /*check_id = $("#id_cliente option:selected").val();
     if(check_id == 2){
           $(".form-row.field-neumatico_cliente").css("display","block");
           $(".form-row.field-lubricante_cliente").css("display","");
           $(".form-row.field-bateria_cliente").css("display","");
        }else if(cliente == 3){
            $(".form-row.field-neumatico_cliente").css("display","");
            $(".form-row.field-lubricante_cliente").css("display","block");
            $(".form-row.field-bateria_cliente").css("display","");
        }else if(cliente == 4){
            $(".form-row.field-neumatico_cliente").css("display","");
            $(".form-row.field-lubricante_cliente").css("display","");
            $(".form-row.field-bateria_cliente").css("display","block");
        }else{
            $(".form-row.field-neumatico_cliente").css("display","");
            $(".form-row.field-lubricante_cliente").css("display","");
            $(".form-row.field-bateria_cliente").css("display","");
        }
*/

    $("select[name='cliente']").change(function(){
        //alert("change");

        $("#id_cliente option:selected").each(function () {
            cliente = $("#id_cliente option:selected").val();
         });

        //cliente = $("#id_cliente option:selected").val();
        //alert(cliente);
        if(cliente == 3){
           $(".form-row.field-neumatico_cliente").css("display","block");
           $(".form-row.field-lubricante_cliente").css("display","");
           $(".form-row.field-bateria_cliente").css("display","");
        }else if(cliente == 5){
            $(".form-row.field-neumatico_cliente").css("display","");
            $(".form-row.field-lubricante_cliente").css("display","block");
            $(".form-row.field-bateria_cliente").css("display","");
        }else if(cliente == 4){
            $(".form-row.field-neumatico_cliente").css("display","");
            $(".form-row.field-lubricante_cliente").css("display","");
            $(".form-row.field-bateria_cliente").css("display","block");
        }else{
            $(".form-row.field-neumatico_cliente").css("display","");
            $(".form-row.field-lubricante_cliente").css("display","");
            $(".form-row.field-bateria_cliente").css("display","");
            //$("option:selected").removeAttr("selected");
        }
    });
   });

})(django.jQuery);


   /* $("#id_cliente").change(function() {
    if($('#clientes option:selected').val()==2){
       $(".form-row field-neumatico_cliente").css("display","block");
        $(".form-row field-lubricante_cliente").css("display","");
        $(".form-row field-bateria_cliente").css("display","");
    }else{
       $(".field-lubricantes").css("display","block");
       $(".field-neumaticos").css("display","");
    }
});

if($('#id_cliente option:selected').val()==2){
       $(".field-neumaticos").css("display","block");
        $(".field-lubricantes").css("display","");
    }else{
       $(".field-lubricantes").css("display","block");
        $(".field-neumaticos").css("display","");
    }
*/