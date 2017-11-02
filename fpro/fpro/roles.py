from rolepermissions.roles import AbstractUserRole


class Arrangor(AbstractUserRole):
    available_permissions = {
        'view_edit_all_shifts': True,
        'view_concerts': True,
        'view_scene_info': True,
    }


class BookingSjef(AbstractUserRole):
    available_permissions = {
        'view_dates': True,
        'accept_booking': True,
        'view_bookings': True,
        'view_economy': True,
    }


class BookingAnsvarlig(AbstractUserRole):
    available_permissions = {
        'send_bookingoffer': True,
        'search_band': True,
        'search_concerts': True,
        'search_band_info': True,
        'tech_needs': True,
        'view_bookings': True,
        'send_review': True,
    }


class Tekniker(AbstractUserRole):
    available_permissions = {
        'view_my_shifts': True,
    }


class Manager(AbstractUserRole):
    available_permissions = {
        'send_techneeds': True,
		'register_songs' : True,
    }

class PrManager(AbstractUserRole):
    available_permissions = {
        'view_bookings': True,
        'view_pr_information': True,
    }

class ServeringsAnsvarlig(AbstractUserRole):
    available_permissions = {
            'can_serve_food': True,
    }

