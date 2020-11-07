

  const loginPopup = document.querySelector(".login-popup");
  const close = document.querySelector(".close");
 const ingresarBtn=document.querySelector("#IngresarBtn");


 
  window.addEventListener("load",function(){
  
  





  })



  






function showMap(){

    var map= L.map('mapita').setView([-33.694113,-71.214489],13);

 L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { 
   attribution:' <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>',
 }).addTo(map);
  

  let iconMarker = L.icon({
    iconUrl: 'https://cdn.mapmarker.io/api/v1/pin?size=178&background=%23FE9200&icon=fa-bicycle&color=%23FFFFFF&voffset=0&hoffset=1&',
    iconSize: [70, 70],
    iconAnchor: [40, 40],
    popupAnchor:  [-5, -30]
    
})

let estacion = L.marker([-33.685689,-71.2144432,19], { icon: iconMarker }).bindPopup('Plaza de Armas <br> Bicicletas:10 ').addTo(map)


let estacionDuoc = L.marker([-33.694113,-71.214489], { icon: iconMarker }).bindPopup(' Duoc <br> Bicicletas:12 ').addTo(map)

let estacionLider = L.marker([-33.6808439,-71.2039486,21], { icon: iconMarker }).bindPopup('Lider <br> Bicicletas:30 ').addTo(map)



  



}

  function showPopup(){
        const timeLimit = 5 // seconds;
        let i=0;
        const timer = setInterval(function(){
         i++;
         if(i == timeLimit){
          clearInterval(timer);
          loginPopup.classList.add("show");
         } 
         console.log(i)
        },1000);
  }

  ingresarBtn.addEventListener("click",function(){
    loginPopup.classList.add("show");

  })


  close.addEventListener("click",function(){
    loginPopup.classList.remove("show");
  })

  

