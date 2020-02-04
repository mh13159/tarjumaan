var progress = 0;

function startProgress()
{
    
    // change button to progress button, and add progress bar
    $('#submit').addClass('progress').html('<span id="progress-bar"></span>');
    
    // update progress bar every 0.5 second
    setInterval(function(){
            $('#progress-bar').width(progress);
             $("#progress-bar").css({"background":"#000", "display": "block", "height": "30px", "width": "0"});
            progress++;
        }, 500);
        
    $("#progress-bar").css({"backgroundColor": "black", "display":"block","height":"30px","width":"0"});
        


}
