$(document).ready(
  function() {
    $('.convertfile').change(
      function() {
        if ($(this).val()) {
          $('.downloadfile').attr('disabled', false);
        }
      }
    );
});