class MovieTicket:
    def __init__(self,movie_name):
        self.movie_name=movie_name
        self.seats_tot=100
        self.seats_booked=50
    def book_ticket(self,num):
        if num<=(self.seats_tot-self.seats_booked):
            print("Seats booked")
            self.seats_booked+=num
        else:
            print("Seats not available")
    def cancel_ticket(self,num):
        print("Seats cancelled")
        self.seats_booked-=num
    def available_seats(self):
        print(f"Available seats: {self.seats_tot-self.seats_booked}")
movie1=MovieTicket("Movie1")
movie1.book_ticket(100)
movie1.book_ticket(20)
movie1.available_seats()
movie1.cancel_ticket(34)
movie1.available_seats()



