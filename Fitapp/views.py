from django.shortcuts import render
import socket
socket.getaddrinfo('localhost', 8080)

 
#My Api key /oYagKFs6gYUk529LINE3Q==9HY5FtkqMNvRMzG4
def home(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': '/oYagKFs6gYUk529LINE3Q==9HY5FtkqMNvRMzG4'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})

