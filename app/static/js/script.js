function handleEvent(e){
    e.preventDefault();
}
function sendData(){
    document.querySelector('form').addEventListener('submit',handleEvent)

    const fd = new FormData(document.querySelector('form'))
    const xhr = new XMLHttpRequest()

    xhr.open('POST','/process',true)
    document.getElementById("prediction").innerHTML = "Processing request ..."

    xhr.onreadystatechange = function(){
        if(xhr.readyState == XMLHttpRequest.DONE){
            document.getElementById("prediction").innerHTML="The reslate price is : $"+xhr.responseText;
        }
    }
    xhr.onload = function(){}
    xhr.send(fd);

}