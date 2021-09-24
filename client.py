import requests

def get_data(url):
    response = requests.get(url)
    data = response.content
    return data

if __name__ == '__main__':
    data = get_data("http://localhost:8080/")
    print(data)