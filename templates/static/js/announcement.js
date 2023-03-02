let mainPhoto = document.getElementById("mainPhoto");
let mainName = mainPhoto.getAttribute("name");

function updateImage(event) {
    let image = event.target;
    mainPhoto.src = image.src; 
}

function createImagesEventListener()
{
    //get all ".btn" elements (in array format)
    let imagesCarrousel = Array.from(document.getElementsByClassName("imgCarousel"));

    for(let item of imagesCarrousel){
        item.addEventListener('click', updateImage);
    }
}

function moveCarousel(btn) {
    let listImages = document.getElementById('carousel')
    let  btnPrevious = document.querySelector('.previous')
    let mover  = 150
    let posicaoXDireita = mover
    let posicaoXEsquerda = -mover

    if (btn == 'next') {
        listImages.scrollBy(posicaoXDireita, 0)
    }else {
        listImages.scrollBy(posicaoXEsquerda, 0)
    }

    if (listImages.scrollLeft > 0){
        btnPrevious.classList.remove('d-none');
        btnPrevious.classList.add('d-flex');
    }else {
        btnPrevious.classList.remove('d-flex');
        btnPrevious.classList.add('d-none'); 
    }
}

createImagesEventListener()





