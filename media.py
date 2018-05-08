import webbrowser


class Movie():
    """Class that describes the attributes of movies

    Note:
        Do not include the 'udacity' parameter in the "Args" section

    Args:
        movie_title(str): Movie's title
        movie_storyline(str): Movie's storyline
        poster_image(str): Movie's poster image
        trailer_youtube(str): Movie's trailer via youtube

    Attributes:
        movie_title(str): Movie's title
        movie_storyline(str): Movie's storyline
        poster_image(str): Movie's poster image
        trailer_youtube(str): Movie's trailer via youtube

    Methods:
        show_trailer(str): opens the movie's trailer in the webbrower
"""

    def __init__(udacity, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        udacity.title = movie_title
        udacity.storyline = movie_storyline
        udacity.poster_image_url = poster_image
        udacity.trailer_youtube_url = trailer_youtube

    def show_trailer(udacity):
        """Opens the movie trailer in the webbrowswer

        Args:
            shower_trailer(str): opens the movie's trailer in
            the webbrowser

        Returns:
        None.

        """
        webbrowser.open(udacity.trailer_youtube_url)
