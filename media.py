class Drama():  # Create drama class
    """This class stores information about tv dramas."""
# Set constructor to initialize new drama instances
    def __init__(self, drama_title, drama_description, drama_poster,
                 trailer_url, year_released, number_of_episodes):
        """ Constructor, the class initializer method.

        Args:
            drama_title (str): Stores the title of the drama
            drama_description (str): Synopsis of the drama
            drama_poster (str): Official poster imagery
            trailer_url (str): Drama trailer url on youtube
            year_released (int): This is year the drama was released
            number_of_episodes (int): Number of drama episodes

        Attributes:
            title (str): Stores the title of the drama
            drama_description (str): Synopsis of the drama
            poster_image_url (str): Official poster imagery
            trailer_youtube_url (str): Drama trailer on youtube
            year_released (int): This stores the release year of the drama
            episodes (int): Number of drama episodes
        """
        self.title = drama_title
        self.drama_description = drama_description
        self.poster_image_url = drama_poster
        self.trailer_youtube_url = trailer_url     # define instance variables
        self.year_released = year_released
        self.episodes = number_of_episodes
