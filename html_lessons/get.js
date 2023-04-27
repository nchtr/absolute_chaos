$(document).ready(function(){
    $.ajax({
        url: 'https://jsonplaceholder.typicode.com/todos',
        type: 'GET',
        dataType: 'json',
        success: function(data){
          var items = [];
          $.each(data, function(index, element){
            items.push('<li>' + element.title + '</li>');
          });
          $('ul').html(items.join(''));
        }
      });
});
