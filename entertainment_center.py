import media
import fresh_tomatoes

# These are instances of movies to be shown on the website, including title, storyline,
# link to movie poster via movie's wikipedia page and the youtube movie trailer.

the_great_escape = media.Movie("The Great Escape",
                        "250 prisoners escape from a WWII concentration camp",
                        "http://upload.wikimedia.org/wikipedia/en/c/c7/Great_escape.jpg",
                        "https://www.youtube.com/watch?v=r9Q_WESQUVw")


shawshank_redemption = media.Movie("Shawshank Redemption",
                     "A man imprisioned for murdering his wife never gives up hope",
                     "http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                     "https://www.youtube.com/watch?v=-6hB3S9bIaco")

philadelphia_story = media.Movie("The Philadelphia Story",
                     "A man an two reporters are uninvited guests to his ex-wife's wedding",
                     "http://upload.wikimedia.org/wikipedia/commons/5/54/The-Philadelphia-Story-%281940%29.jpg",
                     "https://www.youtube.com/watch?v=o1PEW45pOog")

north_by_northwest = media.Movie("North by Northwest",
                     "A man accused of murder is recruited to be an unwitting spy",
                     "http://upload.wikimedia.org/wikipedia/commons/8/83/Northbynorthwest1.jpg",
                     "https://www.youtube.com/watch?v=ek7T9Gyl_J4")

midnight_in_paris = media.Movie("Midnight in Paris",
                     "Going back in time to meet authors",
                     "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                     "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
                     "A really real reality show",
                     "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                     "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [the_great_escape, shawshank_redemption, philadelphia_story, north_by_northwest, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)

