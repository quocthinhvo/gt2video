var statusClear = false;
function start(){
    statusClear = false;
    path_video = document.getElementById("path_video").value;
    path_gt_0 = document.getElementById("path_gt_0").value;
    path_gt_1 = document.getElementById("path_gt_1").value;
    var ws = new WebSocket("ws://localhost:8000/ws0?path_video=" + path_video + "&path_gt=" + path_gt_0);
    let image = document.getElementById("frame0");
    image.onload = function(){
        URL.revokeObjectURL(this.src); 
    } 
    ws.onmessage = function(event) {
        if (statusClear === true){
            ws.close();
            return;
        }
        if (typeof event.data === 'string') 
            document.getElementById("textArea").innerHTML = event.data;
        else
            image.src = URL.createObjectURL(event.data);
    };

    var ws1 = new WebSocket("ws://localhost:8000/ws0?path_video=" + path_video + "&path_gt=" + path_gt_1);
    let image1 = document.getElementById("frame1");
    image1.onload = function(){
        URL.revokeObjectURL(this.src); 
    } 
    ws1.onmessage = function(event) {
        if (statusClear === true){
            ws1.close();
            return;
        }
        if (typeof event.data === 'string') 
            document.getElementById("textArea").innerHTML = event.data;
        else
            image1.src = URL.createObjectURL(event.data);
    };
}

