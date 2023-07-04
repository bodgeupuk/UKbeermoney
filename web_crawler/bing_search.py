```python
import requests
import json
from datetime import datetime

class BingSearch:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {'Ocp-Apim-Subscription-Key': self.api_key}
        self.search_url = "https://api.bing.microsoft.com/v7.0/search"

    def search(self, query, count=50, offset=0, mkt='en-GB'):
        params = {"q": query, "count": count, "offset": offset, "mkt": mkt}
        response = requests.get(self.search_url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_current_month_promotions(self):
        current_month = datetime.now().strftime('%B')
        query = f"{current_month} uk promotions offering free cash incentives refer a friend signup bonus or signup promotion"
        return self.search(query)

if __name__ == "__main__":
    api_key = "YOUR_BING_API_KEY"
    bing_search = BingSearch(api_key)
    promotions = bing_search.get_current_month_promotions()
    print(json.dumps(promotions, indent=4))
```