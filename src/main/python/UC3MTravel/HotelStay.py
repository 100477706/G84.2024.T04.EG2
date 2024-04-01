""" Class HotelStay (GE2.2) """
from datetime import datetime
import hashlib


class HOTEL_STAY:
    def __init__(self, id_card, localizer, num_days, room_type):
        self.__alg = "SHA-256"
        self.__type = room_type
        self.__idcard = id_card
        self.__localizer = localizer
        justnow = datetime.utcnow()
        self.__arrival = justnow.strftime('%d/%m/%Y %H:%M')
        # timestamp is represented in seconds.miliseconds
        # to add the number of days we must express numdays in seconds
        self.__departure = datetime.utcfromtimestamp(datetime.timestamp(justnow) +\
                                                     (num_days * 24 * 60 * 60)).strftime(
            '%d/%m/%Y %H:%M')
        self.__room_key = hashlib.sha256(self.SignatureString().encode()).hexdigest()

    def SignatureString(self):
        """Composes the string to be used for generating the key for the room"""
        return "{alg:" + self.__alg + ",typ:" + self.__type + ",localizer:" + \
            self.__localizer + ",arrival:" + self.__arrival + \
            ",departure:" + self.__departure + "}"

    @property
    def id_card(self):
        """Property that represents the product_id of the patient"""
        return self.__idcard

    @id_card.setter
    def id_card(self, value):
        self.__idcard = value

    @property
    def localizer(self):
        """Property that represents the order_id"""
        return self.__localizer

    @localizer.setter
    def localizer(self, value):
        self.__localizer = value

    @property
    def arrival(self):
        """Property that represents the phone number of the client"""
        return self.__arrival

    @property
    def room_key(self):
        """Returns the sha256 signature of the date"""
        return self.__room_key

    @property
    def departure(self):
        """Returns the issued at value"""
        return self.__departure

    @departure.setter
    def departure(self, value):
        self.__departure = value
