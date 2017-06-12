/**
 * Created by Robert on 12-Jun-17.
 */
$("#undo").click(function(){
    try{
        document.execCommand("undo");
    }catch(err){
        alert("Your browser does not support undo! Use control + Z.");
    }
})
$("#redo").click(function(){
    try{
        document.execCommand("redo");
    }catch(err){
        alert("Your browser does not support redo! Use control + Y.");
    }
});
$("#bold").click(function(){
    try{
        document.execCommand("bold");
    }catch(err){
        alert("Your browser does not support bold! Use control + B.");
    }
})
$("#italic").click(function(){
    try{
        document.execCommand("italic");
    }catch(err){
        alert("Your browser does not support undo! Use control + I.");
    }
})
$("#underline").click(function(){
    try{
        document.execCommand("underline");
    }catch(err){
        alert("Your browser does not support underline! Use control + U.");
    }
})
$("#leftAlign").click(function(){
    try{
        document.execCommand("justifyleft");
    }catch(err){
        alert("Your browser does not support alignments!");
    }
})
$("#centreAlign").click(function(){
    try{
        document.execCommand("justifyCenter");
    }catch(err){
        alert("Your browser does not support alignments!");
    }
})
$("#rightAlign").click(function(){
    try{
        document.execCommand("justifyRight");
    }catch(err){
        alert("Your browser does not support alignments!");
    }
})
$("#fullAlign").click(function(){
    try{
        document.execCommand("justifyFull");
    }catch(err){
        alert("Your browser does not support alignments!");
    }
})
$("#largeFont").click(function(){
    try{
        document.execCommand("fontSize", false, "6");
        var fontElements = document.getElementsByTagName("font");
        for (var i = 0, len = fontElements.length; i < len; ++i) {
            if (fontElements[i].size == "6") {
                fontElements[i].removeAttribute("size");
                fontElements[i].style.fontSize = "25px";
            }
        }
    }catch(err){
        alert("Your browser does not support different font sizes!");
    }
});
$("#regularFont").click(function(){
    try{
        document.execCommand("fontSize", false, "4");
        var fontElements = document.getElementsByTagName("font");
        for (var i = 0, len = fontElements.length; i < len; ++i) {
            if (fontElements[i].size == "4") {
                fontElements[i].removeAttribute("size");
                fontElements[i].style.fontSize = "16px";
            }
        }
    }catch(err){
        alert("Your browser does not support different font sizes!");
    }
});
$("#smallFont").click(function(){
    try{
        document.execCommand("fontSize", false, "2");
        var fontElements = document.getElementsByTagName("font");
        for (var i = 0, len = fontElements.length; i < len; ++i) {
            if (fontElements[i].size == "2") {
                fontElements[i].removeAttribute("size");
                fontElements[i].style.fontSize = "12px";
            }
        }
    }catch(err){
        alert("Your browser does not support different font sizes!");
    }
});
$(document).on('keydown', function(e){
    if(e.ctrlKey && e.which === 83){ // Check for the Ctrl key being pressed, and if the key = [S] (83)
        console.log('Ctrl+S!');
        e.preventDefault();
        return false;
    }
});