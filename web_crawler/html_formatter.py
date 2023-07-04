```python
from jinja2 import Environment, FileSystemLoader

def format_html(promotions):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('promo_template.html')

    output = template.render(promotions=promotions)
    return output

def save_html(html_str, filename):
    with open(filename, 'w') as f:
        f.write(html_str)

def format_and_save(promotions, filename):
    html_str = format_html(promotions)
    save_html(html_str, filename)
```

You will need to create a directory named 'templates' in the same directory as this script, and inside 'templates', create a file named 'promo_template.html' with the following content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>UK Promotions</title>
</head>
<body>
    <table>
        <tr>
            <th>Promotion Name</th>
            <th>Description</th>
            <th>Link</th>
        </tr>
        {% for promo in promotions %}
        <tr>
            <td>{{ promo.promotion_name }}</td>
            <td>{{ promo.promotion_description }}</td>
            <td><a href="{{ promo.promotion_link }}">Go to Promotion</a></td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

This template will be used to generate the HTML page with the scraped promotions.