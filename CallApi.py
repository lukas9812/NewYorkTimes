import requests
import config

import ApiMethods

# Define the API endpoint and your API key
url = "https://api.nytimes.com/svc/books/v3/reviews.json?author=Stephen+King&api-key={}".format(config.api_key)


# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Process the response
    data = response.json()['results']
    propsCollection = ApiMethods.get_book_properties(data, 'book_title')
    
    for property in propsCollection:
        print(property)
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
    



