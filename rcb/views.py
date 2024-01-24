from django.shortcuts import render
from pageupdated.models import PageUpdate
from .forms import RCBForm
from django.http import  HttpResponseRedirect, HttpResponse

# Create your views here.
def resistor_ccodes(request):
    last_updated="Today's date"
    resistor4band_image = ""
    firstband='Brown'
    secondband='Black'
    thirdband='Black'
    fourthband='Brown'
    
    band1str="1"
    band2str="1"
    band3str='x1Ω'#0-black(x1Ω) 
    resistance="11"#int(band1str+band2str)x1Ω = 11Ω
    calculated='11 x1Ω'
    band3float=.1
    ohms='Ω'
    
    submitted=False

    #band1 colors set flag for selected
    band1black=False
    band1brown=False
    band1red=False
    band1orange=False
    band1yellow=False
    band1green=False
    band1blue=False
    band1violet=False
    band1grey=False
    band1white=False

    #band2 colors set flag for selected
    band2black=False
    band2brown=False
    band2red=False
    band2orange=False
    band2yellow=False
    band2green=False
    band2blue=False
    band2violet=False
    band2grey=False
    band2white=False

    #band3 colors set flag for selected
    band3black=False
    band3brown=False
    band3red=False
    band3orange=False
    band3yellow=False
    band3green=False
    band3blue=False
    band3violet=False
    band3grey=False
    band3white=False
    band3gold=False
    band3silver=False

    #band4 colors set flag for selected
    band4brown=False
    band4red=False
    band4green=False
    band4blue=False
    band4violet=False
    band4grey=False
    band4gold=False
    band4silver=False


      

    firstband=''
    secondband=''
    thirdband=''
    fourthband=''

    form = RCBForm()
    pagename="Resistor Color Bands"
    last_updated=PageUpdate.objects.get(update_page=pagename).update_date
    if request.method == 'POST':
 
        print(request.POST)
        firstband=request.POST['firstband']
        secondband=request.POST['secondband']
        thirdband=request.POST['thirdband']
        fourthband=request.POST['fourthband']
        resistance=request.POST['resistancevalue']

        form = RCBForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            response=HttpResponseRedirect('?submitted=True&firstband=%s&secondband=%s&thirdband=%s&fourthband=%s&resistancevalue=%s' %(firstband,secondband,thirdband,fourthband,resistance))
            #response.set_cookie('city', city)                             
            return response
    else:
        form = RCBForm()
        
        if 'submitted' in request.GET:
            submitted = True
        if 'firstband' in request.GET:
            firstband=request.GET['firstband']
        else:
            firstband='Black'
        if 'secondband' in request.GET:
            secondband=request.GET['secondband']
        else:
            secondband='Black'
        if 'thirdband' in request.GET:
            thirdband=request.GET['thirdband']
        else:
            thirdband='Black'
        if 'fourthband' in request.GET:
            fourthband=request.GET['fourthband']
        else:
            fourthband='Brown'
        if 'resistancevalue' in request.GET:
            resistance=request.GET['resistancevalue']
        print(firstband)

        # set firstband color selection
        band1pth="rcb/images/fourbands/firstband/"
        band1=''
        if firstband=="Black":
            band1black=True
            band1=band1pth+'black_firstband_mod4.png'
            band1str="0"
        if firstband=="Brown":
            band1brown=True
            band1=band1pth+'brown_firstband_mod4.png'
            band1str="1"
        if firstband=="Red":
            band1red=True
            band1=band1pth+'red_firstband_mod4.png'
            band1str="2"
        if firstband=="Orange":
            band1orange=True
            band1=band1pth+'orange_firstband_mod5.png'
            band1str="3"
        if firstband=="Yellow":
            band1yellow=True
            band1=band1pth+'yellow_firstband_mod4.png'
            band1str="4"
        if firstband=="Green":
            band1green=True
            band1=band1pth+'green_firstband_mod5.png'
            band1str="5"
        if firstband=="Blue":
            band1blue=True
            band1=band1pth+'blue_firstband_mod4.png'
            band1str="6"
        if firstband=="Violet":
            band1violet=True
            band1=band1pth+'violet_firstband_mod4.png'
            band1str="7"
        if firstband=="Grey":
            band1grey=True
            band1=band1pth+'grey_firstband_mod4.png'
            band1str="8"
        if firstband=="White":
            band1white=True
            band1=band1pth+'white_firstband_mod4.png'
            band1str="9"

        # set secondband color selection
        band2pth="rcb/images/fourbands/secondband/"
        band2=''
        if secondband=="Black":
            band2black=True
            band2=band2pth+'black_secondband_mod4.png'
            band2str="0"
        if secondband=="Brown":
            band2brown=True
            band2=band2pth+'brown_secondband_mod4.png'
            band2str="1"
        if secondband=="Red":
            band2red=True
            band2=band2pth+'red_secondband_mod4.png'
            band2str="2"
        if secondband=="Orange":
            band2orange=True
            band2=band2pth+'orange_secondband_mod5.png'
            band2str="3"
        if secondband=="Yellow":
            band2yellow=True
            band2=band2pth+'yellow_secondband_mod4.png'
            band2str="4"
        if secondband=="Green":
            band2green=True
            band2=band2pth+'green_secondband_mod5.png'
            band2str="5"
        if secondband=="Blue":
            band2blue=True
            band2=band2pth+'blue_secondband_mod4.png'
            band2str="6"
        if secondband=="Violet":
            band2violet=True
            band2=band2pth+'violet_secondband_mod4.png'
            band2str="7"
        if secondband=="Grey":
            band2grey=True
            band2=band2pth+'grey_secondband_mod4.png'
            band2str="8"
        if secondband=="White":
            band2white=True
            band2=band2pth+'white_secondband_mod4.png'
            band2str="9"

        # set thirdband color selection
        band3pth="rcb/images/fourbands/thirdband/"
        band3=''
        if thirdband=="Black":
            band3black=True
            band3=band3pth+'black_thirdband_mod4.png'
            band3str="x1Ω"
            ohms='Ω'
            band3float=1
        if thirdband=="Brown":
            band3brown=True
            band3=band3pth+'brown_thirdband_mod4.png'
            band3str="x10Ω"
            ohms='Ω'
            band3float=10
        if thirdband=="Red":
            band3red=True
            band3=band3pth+'red_thirdband_mod4.png'
            band3str="x100Ω"
            ohms='Ω'
            band3float=100
        if thirdband=="Orange":
            band3orange=True
            band3=band3pth+'orange_thirdband_mod4.png'
            band3str="x1kΩ"
            ohms='kΩ'
            band3float=1000
        if thirdband=="Yellow":
            band3yellow=True
            band3=band3pth+'yellow_thirdband_mod7.png'
            band3str="x10kΩ"
            ohms='0kΩ'
            band3float=10000
        if thirdband=="Green":
            band3green=True
            band3=band3pth+'green_thirdband_mod4.png'
            band3str="x100kΩ"
            ohms='00kΩ'
            band3float=100000
        if thirdband=="Blue":
            band3blue=True
            band3=band3pth+'blue_thirdband_mod4.png'
            band3str="x1MΩ"
            ohms='MΩ'
            band3float=1000000
        if thirdband=="Violet":
            band3violet=True
            band3=band3pth+'violet_thirdband_mod4.png'
            band3str="x10MΩ"
            ohms='0MΩ'
            band3float=10000000
        if thirdband=="Grey":
            band3grey=True
            band3=band3pth+'grey_thirdband_mod4.png'
            band3str="x100MΩ"
            ohms='00MΩ'
            band3float=100000000
        if thirdband=="White":
            band3white=True
            band3=band3pth+'white_thirdband_mod4.png'
            band3str="x1GΩ"
            ohms='GΩ'
            band3float=1000000000
        if thirdband=="Gold":
            band3gold=True
            band3=band3pth+'gold_thirdband_mod4.png'
            band3float=.1
            ohms='Ω'
        if thirdband=="Silver":
            band3silver=True
            band3=band3pth+'silver_thirdband_mod4.png'
            band3float=.01
            ohms='Ω'
        
        #calculated=band1str+band2str+" "+band3str
        if thirdband=="Black" or thirdband=="Brown" or thirdband=="Red":
            calculated=str(int(band1str+band2str)*int(band3float))+ohms
        else:
            if thirdband=="Gold" or thirdband=="Silver":
                i=int(band1str+band2str)
                c=i*band3float
                if thirdband=="Silver":
                    calculated=str(round(c,2))+ohms
                else:
                    calculated=str(round(c,1))+ohms
            else:
                calculated=str(int(band1str+band2str))+ohms

        # set fourthband color selection
        band4pth="rcb/images/fourbands/fourthband/"
        band4=''
        if fourthband=='Brown':
            band4brown=True
            band4=band4pth+"brown_mod4.png"
        if fourthband=='Red':
            band4red=True
            band4=band4pth+"red_mod4.png"
        if fourthband=='Green':
            band4green=True
            band4=band4pth+"green_mod4.png"
        if fourthband=='Blue':
            band4blue=True
            band4=band4pth+"blue_mod4.png"
        if fourthband=='Violet':
            band4violet=True
            band4=band4pth+"violet_mod4.png"
        if fourthband=='Grey':
            band4grey=True 
            band4=band4pth+"grey_mod4.png"  
        if fourthband=='Gold':
            band4gold=True
            band4=band4pth+"gold_mod4.png"
        if fourthband=='Silver':
            band4silver=True
            band4=band4pth+"silver_mod4.png"

    print('band4brown',band4brown)


    band1pth="rcb/images/fourbands/firstband/"
    band2pth="rcb/images/fourbands/secondband/"
    band3pth="rcb/images/fourbands/thirdband/"
    
    resistor4band_image = "rcb/images/fourbands/resistor_4band/resistor-4bands.png"
    
    
    context = {'submitted':submitted,'last_updated': last_updated, 
               'band1':band1,'band2':band2,'band3':band3,'band4':band4, 
               'band1black':band1black,'band1brown':band1brown,'band1red':band1red,'band1orange':band1orange,
               'band1yellow':band1yellow,'band1green':band1green,'band1yellow':band1yellow,
               'band1green':band1green,'band1blue':band1blue,'band1violet':band1violet,
               'band1grey':band1grey,'band1white':band1white, 'band2black':band2black,
               'band2brown':band2brown, 'band2red':band2red, 'band2orange':band2orange,
               'band2yellow':band2yellow, 'band2green':band2green, 'band2blue':band2blue,
               'band2violet':band2violet,'band2grey':band2grey,'band2white':band2white,
               'band3black':band3black,'band3brown':band3brown,'band3red':band3red,'band3orange':band3orange,
               'band3yellow':band3yellow,'band3green':band3green,'band3yellow':band3yellow,
               'band3green':band3green,'band3blue':band3blue,'band3violet':band3violet,
               'band3grey':band3grey,'band3white':band3white,'band3gold':band3gold,'band3silver':band3silver,
               'band4brown':band4brown,'band4red':band4red,'band4green':band4green,'band4blue':band4blue,
               'band4violet':band4violet,'band4grey':band4grey,'band4gold':band4gold,'band4silver':band4silver,
               'resistance':resistance, 'calculated':calculated,'resistor4band_image':resistor4band_image,


               }
    return render(request,"rcb/index.html", context)
    #return render(request, 'sitemap.xml', {"foo": "bar"}, content_type="application/xhtml+xml")