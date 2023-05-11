import requests

# Define the access token and page ID
access_token = 'YOUR_ACCESS_TOKEN'
page_id = 'YOUR_PAGE_ID'

# Define the API endpoint for creating a post
endpoint = f'https://graph.facebook.com/{page_id}/feed'

# Define the post data
data = {
    'message': 'Hello, world!'
}

# Define the headers for the API request
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Send a POST request to create the post
response = requests.post(endpoint, data=data, headers=headers)

# Check the response status code
if response.status_code == 200:
    print('Post created successfully.')
else:
    print(f'Error creating post: {response.status_code}')