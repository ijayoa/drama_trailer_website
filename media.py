class Drama():
	#constant class variable to keep finite list of drama status
	STATUS = ["completed","ongoing"]

	#constructor to initialize new drama instances
	def __init__(self, drama_title, drama_description, drama_poster, trailer_url, year_released, number_of_episodes):
		self.title = drama_title
		self.drama_description = drama_description
		self.poster_image_url = drama_poster
		self.trailer_youtube_url = trailer_url
		self.year_released = year_released
		self.episodes = number_of_episodes


