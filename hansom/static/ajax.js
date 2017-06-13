/**
 * Created by Robert and Keane on 12-Jun-17.
 */
var contents = "";
var name = "";

$('body').on('focus', '[contenteditable]', function() {
    var $this = $(this);
    $this.data('before', $this.html());
    contents = $this;

}).on('blur keyup paste input', '[contenteditable]', function() {
    var $this = $(this);
    if ($this.data('before') !== $this.html()) {
        $this.data('before', $this.html());
        $this.trigger('change');
    }
    contents = $this;
});

$(function() {
        $('#save').click(function() {
          var name = $('#note').val();
          var pass = $('#txtPassword').val();
          $.ajax({
              url: '/signUpUser',
              data: $('form').serialize(),
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

