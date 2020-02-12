function getExtension(filename) {
    var parts = filename.split('.');
    return parts[parts.length - 1];
}

function isAudio(filename) {
    var ext = getExtension(filename);
    switch (ext.toLowerCase()) {
    case 'flac':
        return true;
    }
    return false;
}

$(function() {
    
    $('form[name="testform"]').submit(function() {
        function failValidation(msg) {
            alert(msg); // just an alert for now but you can spice this up later
            return false;
        }

        var file = $('#file');
        if (!isAudio(file.val())) {
            return failValidation('Your audio type is not supported by our system \n                                 🙁');
        }
        // success at this point
        // indicate success with alert for now
        
        alert('You have selected the right audio type \n                                 🙂');
        setTimeout(function(){document.getElementById("audiocheck").disabled = false;},3000);

        //document.getElementById("audiocheck").disabled = false;
        return false; // prevent form submitting anyway - remove this in your environment
    });

});