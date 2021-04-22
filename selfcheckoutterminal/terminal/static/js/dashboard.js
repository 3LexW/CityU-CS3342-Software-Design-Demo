hideAllInputs()

document.getElementById('newText').addEventListener("click", showText);
document.getElementById('newScan').addEventListener("click", showScan);
document.getElementById('newPhoto').addEventListener("click", showPhoto);
document.getElementById('toPayment')

function showText(){
    hideAllInputs();
    document.getElementById("textinput").classList.remove('hidden');
}

function showScan(){
    hideAllInputs();
    document.getElementById("scaninput").classList.remove('hidden');
}
function showPhoto(){
    hideAllInputs();
    document.getElementById("imageinput").classList.remove('hidden');
}

function hideAllInputs(){
    let inputs = document.getElementsByClassName('newInput');
    for (var i = 0; i < inputs.length; i++){
        inputs[i].classList.add('hidden');
    }
}