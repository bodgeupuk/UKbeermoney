```python
import json
from html_formatter import format_to_html

class DataStorage:
    def __init__(self):
        self.promotion_data = []

    def store_data(self, data):
        self.promotion_data.append(data)

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.promotion_data, f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            self.promotion_data = json.load(f)

    def format_data_to_html(self):
        html_content = format_to_html(self.promotion_data)
        with open('promotions.html', 'w') as f:
            f.write(html_content)

if __name__ == "__main__":
    storage = DataStorage()
    storage.load_from_file('promotions.json')
    storage.format_data_to_html()
```