const windowWidth = window.innerWidth;
const search = document.querySelector('#search')

if (windowWidth < 576){
  const order = document.querySelector('.order-select')
  const option = document.createElement('option')

  option.setAttribute("selected", "")
  option.setAttribute("hidden", "hidden")
  option.innerHTML = 'Ordenar por:'
  order.appendChild(option)
}

const filterStock = document.querySelector('.filter-stock')

if (windowWidth < 768) {
  
}

const btnOpenFilter = document.querySelector('.btn-open-filter')
const btnOpenFilterText = document.querySelector('.btn-open-text')
const btnCloseFilter = document.querySelector('.btn-close-filter')

function openFilter() {
  const filter = document.querySelector('.filter-stock')
  filter.classList.remove('d-none')
  console.log('teste')
}

btnOpenFilterText.addEventListener('click', openFilter);
btnOpenFilter.addEventListener('click', openFilter);

btnCloseFilter.addEventListener('click', function (){
  const filter = document.querySelector('.filter-stock')
  filter.classList.add('d-none')
} );

