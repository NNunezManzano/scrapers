"""
This site use an API with POST method to get the listed companies.
"""

import requests
import json

# Define the API endpoint URL
url = 'https://45bwzj1sgc-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(3.35.1)%3B%20Browser%3B%20JS%20Helper%20(3.11.3)&x-algolia-application-id=45BWZJ1SGC&x-algolia-api-key=MjBjYjRiMzY0NzdhZWY0NjExY2NhZjYxMGIxYjc2MTAwNWFkNTkwNTc4NjgxYjU0YzFhYTY2ZGQ5OGY5NDMxZnJlc3RyaWN0SW5kaWNlcz0lNUIlMjJZQ0NvbXBhbnlfcHJvZHVjdGlvbiUyMiUyQyUyMllDQ29tcGFueV9CeV9MYXVuY2hfRGF0ZV9wcm9kdWN0aW9uJTIyJTVEJnRhZ0ZpbHRlcnM9JTVCJTIyeWNkY19wdWJsaWMlMjIlNUQmYW5hbHl0aWNzVGFncz0lNUIlMjJ5Y2RjJTIyJTVE'  # Replace with the actual API endpoint URL

# Define the query string parameters
params = {
    'x-algolia-agent': 'Algolia for JavaScript (3.35.1); Browser; JS Helper (3.11.3)',
    'x-algolia-application-id': '45BWZJ1SGC',
    'x-algolia-api-key': 'MjBjYjRiMzY0NzdhZWY0NjExY2NhZjYxMGIxYjc2MTAwNWFkNTkwNTc4NjgxYjU0YzFhYTY2ZGQ5OGY5NDMxZnJlc3RyaWN0SW5kaWNlcz0lNUIlMjJZQ0NvbXBhbnlfcHJvZHVjdGlvbiUyMiUyQyUyMjllQ0NvbXBhbnlCeV9MYXVuY2hfRGF0ZV9wcm9kdWN0aW9uJTIyJTVEJnRhZ0ZpbHRlcnM9JTVCJTIyeWNkY19wdWJsaWMlMjIlNUQmYW5hbHl0aWNzVGFncz0lNUIlMjJ5Y2RjJTIyJTVE'
}

# Define the form data payload
payload = {
    "requests": [
        {
            "indexName": "YCCompany_production",
            "params": "facetFilters=%5B%5B%22batch%3AS22%22%2C%22batch%3AW23%22%5D%5D&facets=%5B%22top_company_by_revenue%22%2C%22top_company%22%2C%22isHiring%22%2C%22nonprofit%22%2C%22highlight_black%22%2C%22highlight_latinx%22%2C%22highlight_women%22%2C%22batch%22%2C%22industries%22%2C%22subindustry%22%2C%22regions%22%2C%22tags_highlighted%22%2C%22tags%22%2C%22status%22%2C%22app_video_public%22%2C%22demo_day_video_public%22%2C%22app_answers%22%2C%22question_answers%22%5D&hitsPerPage=1000&maxValuesPerFacet=1000&page=0&query=&tagFilters="
        },
        {
            "indexName": "YCCompany_production",
            "params": "analytics=false&clickAnalytics=false&facets=batch&hitsPerPage=0&maxValuesPerFacet=1000&page=0&query="
        }
    ]
}

# Make the POST request
response = requests.post(url,params=params, json=payload)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse and work with the response data
    data = response.json()
    # Process the response data as needed
    
    with open('site.json', 'w') as store_json:
        json.dump(data, store_json, indent = 4)
        
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)  # Print the response content for debugging

