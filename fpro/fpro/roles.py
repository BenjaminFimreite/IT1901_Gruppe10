from rolepermissions.roles import AbstractUserRole

class Arrangor(AbstractUserRole):
    available_permissions = {
            'eksempel_bruker_rettighet' : True,
            }


class BookingSjef(AbstractUserRole):
    available_permissions = {
            'en_annen_bruker_rettighet' : True,
            }

class BookingAnsvarlig(AbstractUserRole):
    available_permissions = {
            'enda_en_rettighet' : True,
            }

class Tekniker(AbstractUserRole):
    available_permissions = {
            'rettighet_yeye' : True,
            }

