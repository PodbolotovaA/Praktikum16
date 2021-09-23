class Guest:
    def __init__(self, guest, city, status):
        self.guest = guest
        self.city = city
        self.status = status

    def getGuest(self):
        return self.guest

    def getCity(self):
        return self.city

    def getStatus(self):
        return self.status

    def guest_info(self):
        return f'{self.getGuest()}, г. {self.getCity()}, статус: {self.getStatus()}'