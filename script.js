

  const loginPopup = document.querySelector(".login-popup");
  const close = document.querySelector(".close");
 const ingresarBtn=document.querySelector("#IngresarBtn");

 


  window.addEventListener("load",function(){
  
    var map= L.map('mapita').setView([-33.694113,-71.214489],18);

 L.tileLayer('https://maps.wikimedia.org/osm-intl/{z}/{x}/{y}.png', { 
   attribution:' <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>',
 }).addTo(map);
   // setTimeout(function(){
   //   loginPopup.classList.add("show");
   // },5000)


  let iconMarker = L.icon({
    iconUrl: 'https://www.nipnip.co.uk/wp-content/uploads/2020/04/Fleet-Maintenance-icon.png',
    iconSize: [60, 60],
    iconAnchor: [20, 20]
    
})

let marker2 = L.marker([-33.694113,-71.214489], { icon: iconMarker }).bindPopup('Estacion Duoc, Melipilla.').addTo(map)


  })

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

  

