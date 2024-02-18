import json
from .HotelManagementException import HOTEL_MANAGEMENT_EXCEPTION
from .HotelReservation import HOTEL_RESERVATION


class HOTEL_MANAGER:
    def __init__(self):
        pass

    def ValidateCreditCard(self, tarjeta):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        return True

    def ReaddatafromJSOn(self, fi):

        try:
            with open(fi, encoding="utf-8") as variable_f:
                data = json.load(variable_f)
        except FileNotFoundError as variable_e:
            raise HOTEL_MANAGEMENT_EXCEPTION("Wrong file or file path") from variable_e
        except json.JSONDecodeError as variable_e:
            raise HOTEL_MANAGEMENT_EXCEPTION("JSON Decode Error - Wrong JSON Format")\
                from variable_e

        try:
            variable_c = data["CreditCard"]
            variable_p = data["phoneNumber"]
            req = HOTEL_RESERVATION(id_card="12345678Z", credit_card_numb=variable_c,
                                    name_and_surname="John Doe", phone_number=variable_p,
                                    room_type="single", num_days=3)
        except KeyError as variable_e:
            raise HOTEL_MANAGEMENT_EXCEPTION("JSON Decode Error - Invalid JSON Key") from variable_e
        if not self.ValidateCreditCard(variable_c):
            raise HOTEL_MANAGEMENT_EXCEPTION("Invalid credit card number")

        # Close the file
        return req
