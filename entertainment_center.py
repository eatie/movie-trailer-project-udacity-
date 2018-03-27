import media
import fresh_tomatoes

# declare favorite movies, with 4 args each:

toy_story = media.Movie("Toy Story",
                        1995,
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     2009,
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

dunkirk = media.Movie("Dunkirk",
                      2017,
                      "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU")

logan = media.Movie("Logan",
                    2017,
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")

the_shape_of_water = media.Movie("The Shape of Water",
                                 2017,
                                 "https://upload.wikimedia.org/wikipedia/en/3/37/The_Shape_of_Water_%28film%29.png",
                                 "https://www.youtube.com/watch?v=XFYWazblaUA")

baby_driver = media.Movie("Baby Driver",
                          2017,
                          "https://upload.wikimedia.org/wikipedia/en/8/8e/Baby_Driver_poster.jpg",
                          "https://www.youtube.com/watch?v=z2z857RSfhk")

# assign individual movies to movies array
movies = [toy_story, avatar, dunkirk, logan, the_shape_of_water, baby_driver]

# call movie trailer page method and pass movies array
fresh_tomatoes.open_movies_page(movies)
