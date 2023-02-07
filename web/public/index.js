var statusClear = false;

const params = new Proxy(new URLSearchParams(window.location.search), {
    get: (searchParams, prop) => searchParams.get(prop),
  });
path_video = params.path_video;
path_gt_0 = params.path_gt_0;
path_gt_1 = params.path_gt_1;
document.getElementById("path_video").value = path_video;
document.getElementById("path_gt_0").value = path_gt_0;
document.getElementById("path_gt_1").value = path_gt_1;


var ws = new WebSocket("ws://localhost:8000/ws0?path_video=" + path_video + "&path_gt=" + path_gt_0);
let image = document.getElementById("frame0");
image.onload = function(){
    URL.revokeObjectURL(this.src); 
} 
ws.onmessage = function(event) {
    if (typeof event.data === 'string') 
        document.getElementById("textArea").innerHTML = event.data;
    else
        image.src = URL.createObjectURL(event.data);
};

var ws1 = new WebSocket("ws://localhost:8000/ws1?path_video=" + path_video + "&path_gt=" + path_gt_1);
let image1 = document.getElementById("frame1");
image1.onload = function(){
    URL.revokeObjectURL(this.src); 
} 
ws1.onmessage = function(event) {
    if (typeof event.data === 'string') 
        document.getElementById("textArea").innerHTML = event.data;
    else
        image1.src = URL.createObjectURL(event.data);
};

// function start(){
//     statusClear = false;
//     path_video = document.getElementById("path_video").value;
//     path_gt_0 = document.getElementById("path_gt_0").value;
//     path_gt_1 = document.getElementById("path_gt_1").value;
//     var ws = new WebSocket("ws://localhost:8000/ws0?path_video=" + path_video + "&path_gt=" + path_gt_0);
//     let image = document.getElementById("frame0");
//     image.onload = function(){
//         URL.revokeObjectURL(this.src); 
//     } 
//     ws.onmessage = function(event) {
//         if (typeof event.data === 'string') 
//             document.getElementById("textArea").innerHTML = event.data;
//         else
//             image.src = URL.createObjectURL(event.data);
//     };

//     var ws1 = new WebSocket("ws://localhost:8000/ws1?path_video=" + path_video + "&path_gt=" + path_gt_1);
//     let image1 = document.getElementById("frame1");
//     image1.onload = function(){
//         URL.revokeObjectURL(this.src); 
//     } 
//     ws1.onmessage = function(event) {
//         if (typeof event.data === 'string') 
//             document.getElementById("textArea").innerHTML = event.data;
//         else
//             image1.src = URL.createObjectURL(event.data);
//     };
// }

