from typing import List, Dict
from abc import ABC, abstractmethod
from collections import defaultdict


class Movie:
    def __init__(self, name: str, genre: str):
        self.name = name
        self.genre = genre

class Show:
    def __init__(self, movie: Movie, cinema_hall: str, show_time: str):
        self.movie = movie
        self.cinema_hall = cinema_hall
        self.show_time = show_time

class CinemaHall:
    def __init__(self, name: str, city: str):
        self.name = name
        self.city = city
        self.shows: List[Show] = []

    def addShow(self, show: Show):
        self.shows.append(show)

    def removeShow(self, show: Show):
        self.shows.remove(show)

# Abstract class for Show Added Observers
class ShowAddedObserver(ABC):
    @abstractmethod
    def onShowAdded(self, show: Show, cinema: CinemaHall):
        pass

# Observer 1: City -> Movie -> [Cinema Hall names]
class CityMovieSearch(ShowAddedObserver):
    def __init__(self):
        self.data: Dict[str, Dict[str, List[str]]] = defaultdict(lambda: defaultdict(list))

    def onShowAdded(self, show: Show, cinema: CinemaHall):
        city = cinema.city
        movie = show.movie.name
        if cinema.name not in self.data[city][movie]:
            self.data[city][movie].append(cinema.name)

    def getCinemaShowingMovie(self, city: str, movie: str) -> List[str]:
        return self.data[city][movie]
    
# Observer 2: Cinema -> Movie -> [ShowTimes]
class CinemaMovieSearch(ShowAddedObserver):
    def __init__(self):
        self.data: Dict[str, Dict[str, List[str]]] = defaultdict(lambda: defaultdict(list))

    def onShowAdded(self, show: Show, cinema: CinemaHall):
        self.data[cinema.name][show.movie.name].append(show.show_time)

    def getShowTimesForMovie(self, cinema: str, movie: str) -> List[str]:
        return self.data[cinema][movie]

# Class that will populate our observers
class ShowService:
    def __init__(self):
        self.observers: List[ShowAddedObserver] = []

    def registerObserver(self, observer: ShowAddedObserver):
        self.observers.append(observer)
    
    def notifyObservers(self, show: Show, cinema: CinemaHall):
        for observer in self.observers:
            observer.onShowAdded(show, cinema)

    def addShowToCinema(self, cinema: CinemaHall, show: Show):
        cinema.addShow(show)
        self.notifyObservers(show, cinema)

class Ticket:
    def __init__(self, show: Show, user: str):
        self.show = show
        self.user = user
    
class BookingService:
    def __init__(self):
        self.booked_tickets: List[Ticket] = []

    def bookTicket(self, user: str, show: Show) -> Ticket:
        ticket = Ticket(show, user)
        self.booked_tickets.append(ticket)
        print(f"Ticket booked for {user} for {show.movie.name} at {show.show_time}")
        return ticket
    
    def cancelTicket(self, ticket: Ticket):
        self.booked_tickets.remove(ticket)

# *************************************************************************************

cinema = CinemaHall('PVR Phoenix', 'Bangalore')
movie = Movie('Inception', 'Action')
show = Show(movie, 'PVR Phoenix', '6:00 PM')

show_service = ShowService()

city_search = CityMovieSearch()
cinema_search = CinemaMovieSearch()

show_service.registerObserver(city_search)
show_service.registerObserver(cinema_search)

show_service.addShowToCinema(cinema, show)

print(city_search.getCinemaShowingMovie('Bangalore', 'Inception'))
print(cinema_search.getShowTimesForMovie('PVR Phoenix', 'Inception'))

booking_service = BookingService()
ticket = booking_service.bookTicket('Shubham', show)
booking_service.cancelTicket(ticket)


        
    
