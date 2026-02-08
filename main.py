import requests
import selectorlib

URL = 'https://programmer100.pythonanywhere.com/tours/'

def scrape(url):
    """Scrape the page source from the URL"""

    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)['tour']
    return value


def event(event):
    with open("events.txt", "a") as file:
        file.write(event + "\n")


def read_event(filename):
    with open(filename , "r") as file:
        return file.read()
    
def send_email():
    print("Email was sent")



if __name__ == '__main__':
    scrapped = scrape(URL)
    extracted = extract(scrapped)
    print(extracted)

    if extracted != "No upcoming tours":
        content = read_event("events.txt")
        if extracted not in content:
            event(extracted)
            send_email()
    

