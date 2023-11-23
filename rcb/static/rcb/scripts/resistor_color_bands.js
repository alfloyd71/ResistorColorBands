band_01=document.getElementById("image2")
function changeColor() {
  band_01_select_value = document.getElementById("id_firstband").value;
  band_02_select_value = document.getElementById("id_secondband").value;

  document.getElementById("demo").innerHTML = "You selected: "+band_02_select_value;
  
  
  switch(band_01_select_value){
    case "Black": 
      band_01.src="{% static 'rcb/images/fourbands/firstband/black_firstband_mod4.png' %}"
      break
    case "Brown": 
      band_01.src="{% static 'rcb/images/fourbands/firstband/brown_firstband_mod4.png' %}"
      break
    case "Red": 
      band_01.src="{% static 'rcb/images/fourbands/firstband/red_firstband_mod4.png' %}"
      break
    case "Orange": 
      band_01.src="{% static 'rcb/images/fourbands/firstband/orange_firstband_mod4.png' %}"
      break
    case "Yellow": 
      band_01.src="{% static 'rcb/images/fourbands/firstband/yellow_firstband_mod4.png' %}"
      break
    case "Green": 
      band_01.src="{% static 'rcb/images/fourbands/firstband/green_firstband_mod5.png' %}"
      break
      case "Blue": 
      band_01.src="{% static 'rcb/images/fourbands/firstband/blue_firstband_mod4.png' %}"
      break
    case "Violet": 
      band_01.src="{% static 'rcb/images/fourbands/firstband/violet_firstband_mod4.png' %}"
      break
    case "Grey": 
      band_01.src="{% static 'rcb/images/fourbands/firstband/grey_firstband_mod4.png' %}"
      break
    case "White": 
      band_01.src="{% static 'rcb/images/fourbands/firstband/white_firstband_mod4.png' %}"
      break
  }
}