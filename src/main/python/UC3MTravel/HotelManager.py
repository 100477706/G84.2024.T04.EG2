import json
from .HotelManagementException import HotelManagementException
from .HotelReservation import HotelReservation


class HotelManager:
    def __init__(self):
        pass

    def validatecreditcard(self, x):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        # Comprobamos si la tarjeta tiene 16 dígitos
        if len(str(x)) != 16:
            return False

        # Convertimos el número a lista y obtenemos el supuesto valor del último dígito según Luhn
        num_lista = []
        for a in range(len(str(x))-1):
            num_lista.append(str(x)[a])

        # Guardamos la suma del algoritmo de Luhn en la variable suma
        suma = 0
        # Cada dígito par lo duplicamos y sumamos cada dígito del resultado a suma
        # Cada dígito impar lo sumamos directamente a suma
        for a in range(len(num_lista)):
            if a % 2 != 0:
                suma += int(num_lista[a])
            else:
                num_actual = int(num_lista[a])
                num_actual *= 2
                if num_actual >= 10:
                    suma += int(str(num_actual)[0]) + int(str(num_actual)[1])
                else:
                    suma += num_actual
        # Calculamos el resultado del último dígito
        ultimo_digito = (suma * 9) % 10
        # Comprobamos si el último dígito es el que debería ser según Luhn
        if str(ultimo_digito) == str(x)[len(str(x)) - 1]:
            return True
        else:
            return False


    def ReaddatafromJSOn( self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise HotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            c = DATA["CreditCard"]
            p = DATA["phoneNumber"]
            req = HotelReservation(IDCARD="12345678Z",creditcardNumb=c,nAMeAndSURNAME="John Doe",phonenumber=p,room_type="single",numdays=3)
        except KeyError as e:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.validatecreditcard(c):
            raise HotelManagementException("Invalid credit card number")

        # Close the file
        return req