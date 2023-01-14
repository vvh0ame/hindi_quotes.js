from requests import get
	
class HindiQuotes:
	def __init__(self) -> None:
		self.api = "https://hindi-quotes.vercel.app"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
		}

	def get_random_quote(
			self,
			type: str = None) -> dict:
		"""
		Get random quote in hindi language
		Parameters:
			type: (str): string <success, love, attitude, positive, motivational>
		Returns: 
			dict: random quote in hindi
		"""
		url = f"{self.api}/random"
		if type:
			url += "/{type}"
		return get(
			url, headers=self.headers).json()
