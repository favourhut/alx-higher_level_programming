$("document").ready(function() { 
    $("DIV#add_item").click(function(){
      $("UL.my_list").append("<li>Item</li>");
    });
    
    $("DIV#remove_item").click(function() {
      $("UL.my_list:last").remove();
    });

  $("document").click(function() {
    $("UL.my_list").empty();
    });
});