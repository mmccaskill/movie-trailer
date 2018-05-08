import webbrowser

class Movie():

# this defines the movie title, storyline, poster and youtube trailer

    def __init__(udacity, movie_title, movie_storyline, poster_image, trailer_youtube):
        udacity.title = movie_title
        udacity.storyline = movie_storyline
        udacity.poster_image_url = poster_image
        udacity.trailer_youtube_url = trailer_youtube

# this opens the movie trailer

    def show_trailer(udacity):
        webbrowser.open(udacity.trailer_youtube_url)
        
