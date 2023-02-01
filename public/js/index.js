var glo, i
fetch('/list_videos')
  .then((response) => response.json())
  .then((data) => {
    i = 0
    document.getElementById("video_player").innerHTML ='<source src="videos/' + data[i]+ '" type="video/mp4"></source>'
    document.getElementById("filename").innerText = 'videos/' + data[i]
    glo = data
  });


function pev(){
    if (i == 0) return;
    i = i - 1
    document.getElementById("video_player").src = 'videos/' + glo[i]
    document.getElementById("video_player").load()
    document.getElementById("video_player").play()
    document.getElementById("filename").innerText = 'videos/' + glo[i]
}

function nex(){
    if (i == (glo.length - 1)) return;
    i = i + 1
    document.getElementById("video_player").src = 'videos/' + glo[i]
    document.getElementById("video_player").load()
    document.getElementById("video_player").play()
    document.getElementById("filename").innerText = 'videos/' + glo[i]
}