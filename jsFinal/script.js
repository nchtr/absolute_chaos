$(document).ready(function() {
    $('#srchB').click(function(event) {
      event.preventDefault();
      var query = $('#srchIn').val();
      var url = 'http://universities.hipolabs.com/search?country=Finland';
      if (query) {
        url += '&name=' + encodeURIComponent(query);
      }
      $.getJSON(url, function(data) {
        var resultHtml = '';
        $.each(data, function(index, univ) {
          var logoUrl = 'https://logo.clearbit.com/' + univ.web_pages[0];
          resultHtml += '<div class="univ">';
          resultHtml += '<img src="' + logoUrl + '" alt="' + univ.name + '">'; //иногда вылезает стоковый плейсхолдер
          resultHtml += '<h2><a href="' + univ.web_pages[0] + '">' + univ.name + '</a></h2>';
          resultHtml += '</div>';
        });
        $('#result').html(resultHtml);
      });
    });
  });

// я попробовал переместить в документ.реди но тогда отваливается обратный поиск(когда выполняешь поиск и потом отправляешь ничего в инпут, возвращается исходный список университетов)
var url = 'http://universities.hipolabs.com/search?country=Finland';
$.getJSON(url, function(data) {
    var resultHtml = '';
    $.each(data, function(index, univ) {
      var logoUrl = 'https://logo.clearbit.com/' + univ.web_pages[0];
      resultHtml += '<div class="univ">';
      resultHtml += '<img src="' + logoUrl + '" alt="' + univ.name + '">';
      resultHtml += '<h2><a href="' + univ.web_pages[0] + '">' + univ.name + '</a></h2>';
      resultHtml += '</div>';
    });
    $('#result').html(resultHtml);
  });

  