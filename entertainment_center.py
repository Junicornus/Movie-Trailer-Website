"""Creates a website from the listed movies below"""
import fresh_tomatoes
import media

# movie list with information about each instance from class Movie
# Class Movie is stored in module media.py


spirited_away = media.Movie("Spirited away",
                            "A Story of a girl discovering a magic world",
                            "https://bit.ly/2Qlfm08",
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://bit.ly/1oUhcTQ",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")

interstellar = media.Movie("Interstellar",
                           "An astronaut family love melodrama",
                           "https://bit.ly/249Vnlj",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

leon = media.Movie("Leon the professional",
                                    "Robbery drama",
                                    "https://bit.ly/1OqE1gr",
                                    "https://www.youtube.com/watch?v=yoxLYdARO_0")

alice = media.Movie("Alice in Wonderland",
                                  "A girl escapes into a dreamworld",
                                  "https://bit.ly/2CNdRnY",
                                  "https://www.youtube.com/watch?v=9POCgSRVvf0")

inception = media.Movie("Inception",
                        "A turnaround about truth, reality and dreams",
                        "https://bit.ly/2bs45Yo",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

# lists the movies included when using "movies":
movies = [spirited_away,
          avatar,
          interstellar,
          leon,
          alice,
          inception]

# generates an html webpage using module fresh_tomatoes.py:
fresh_tomatoes.open_movies_page(movies)
