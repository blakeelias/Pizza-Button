$( ".result" ).html("<b>test</b>");

$('#account').submit(function (event) {
    var name = $("input#name").val();
    var address = $("input#address").val();
    var phone = $("input#phone").val();
    //alert(name);
    
    
});

new Restaurant('/rd/147').makeRestaurantRequest('https://r-test.ordr.in', [], '', 'GET', function (data) {
$( ".result" ).html(data);
});