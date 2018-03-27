import webbrowser

class Movie():
    
    """ Class for representing a movie """
    
    def __init__(self,movie_title,year,poster_image,trailer_youtube):

        """ Inits a Movie object """

        self.title = movie_title
        self.year = year
        self.poster_image_url = poster_image
        self.trailer_youtube_url= trailer_youtube
                   
    def show_trailer(self):
        """ Opens trailer in a web browser """
        webbrowser.open(self.trailer_youtube_url)
