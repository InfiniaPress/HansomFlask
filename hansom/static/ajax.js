/**
 * Created by Robert and Keane on 12-Jun-17.
 */
var contents = "";
var name = "";

$(function() {
        $('#save').click(function() {
          contents = $('#note').val();
          name = $('#noteName').val();
          $.ajax({
              url: '/',
              data: {"name":name,"contents":contents,},
              type: 'POST',
              success: function(response) {
                  console.log(response);
              },
              error: function(error) {
                  console.log(error);
              }
          });
        });
      });

