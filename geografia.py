from geopy.geocoders import Nominatim

def ubica_direccion(direccion: str)-> tuple:
    """
    Devuelve una tupla con la latitud y la longitud de una dirección recibida por parámetro
    """
    geolocator = Nominatim(user_agent="my_app") #replace my_app with your app name
    location = geolocator.geocode(direccion)

    return (location.latitude, location.longitude)

if __name__ == "__main__":
    latitud, longitud = ubica_direccion("berrueta 7 Irun")
    print("Latitud:", latitud)
    print("Longitud:", longitud)