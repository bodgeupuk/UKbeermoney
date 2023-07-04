Shared Dependencies:

1. **Scrapy**: This Python library is used for web crawling and is shared across all files as the primary tool for extracting data from the web.

2. **Bing Search GPT API**: This API is used in "web_crawler/scrapy_spider.py" and "web_crawler/bing_search.py" to fetch search results.

3. **Promotion Data Schema**: This is the structure of the data that is being scraped and stored. It is used in "web_crawler/scrapy_spider.py", "web_crawler/nlp_processing.py", and "web_crawler/data_storage.py". It includes fields like 'promotion_name', 'promotion_link', 'promotion_description', etc.

4. **NLP Techniques**: These are used in "web_crawler/nlp_processing.py" to identify relevant promotion content and may be referenced in "web_crawler/scrapy_spider.py" for filtering the scraped data.

5. **HTML Formatting Functions**: These are used in "web_crawler/html_formatter.py" to format the scraped data into a structured HTML page. They may be referenced in "web_crawler/data_storage.py" to store the data in the desired format.

6. **Pagination Handling Functions**: These are used in "web_crawler/scrapy_spider.py" to handle the pagination of search results and may be referenced in "web_crawler/bing_search.py" to fetch all pages of search results.

7. **Promotion Data**: This is the actual data that is being scraped, processed, stored, and formatted. It is shared across all files.

8. **HTML Element IDs**: These are used in "web_crawler/html_formatter.py" to identify specific elements in the HTML page. They include IDs like 'promo_table', 'promo_link', etc.

9. **Scraped Data Storage**: This is the storage location (could be a database or a file system) where the scraped data is stored. It is used in "web_crawler/data_storage.py" and may be referenced in "web_crawler/html_formatter.py" to fetch the data for formatting.