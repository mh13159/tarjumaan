$(document).ready(
  function() {
    $('.target').change(
      function() {
        if ($(this).val()) {
          $('.target1').attr('disabled', false);
        }
      }
    );
});