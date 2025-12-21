from geopy.geocoders import Nominatim



def result_filtter(res:list):
    output =''
    for i in res:
        
        i = str(i).strip()
        if str(i)[0:3] == 'شهر'and str(i)[3] == ' ':
            text = str(i).replace('شهر' , '' , 1)
            output+=(text + ',')
        elif 'دهستان' in i :
            text = str(i).replace('دهستان','')
            output+=(text + ',')
            
            
        elif 'منطقه' in i:
            text = str(i).replace('منطقه','')
            output+=(text + ',')
            
            
        else:
            pass
        if str(i)[0:7] == 'شهرستان' :
            text = str(i).replace('شهرستان','')
            output+=(text + ',')
        
        if 'استان' in i:
            text = str(i).replace('استان','')
            output+=text
        
    return output



def find_name_city(lat , lon):
    geolocator = Nominatim(user_agent="my_geocoder")


    location = geolocator.reverse((lat,lon) , language='fa')
    
    output = result_filtter(str(location).strip().split(','))
    return output

