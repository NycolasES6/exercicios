let items = document.querySelector("#items")
let imgs = document.querySelectorAll("img")

let tams =450
let idx = 0
let nImage = imgs.length - 1
let tempS = 5000


items.addEventListener("wheel", event =>{
    if(event.deltaY > 0){
        moveSlide(tams)
    }else{
        moveSlide(tams)
    }
})

function moveSlide(x, id)
{
    idx++
    if (idx > nImage) {
        x = tams*(nImage * -1)
        idx = 0
    }
    items.scrollBy(x, 0)
}

setInterval(() => {
    moveSlide(tams)
}, tempS);