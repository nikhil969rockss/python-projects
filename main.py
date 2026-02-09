import requests
import selectorlib
import sqlite3
import time

URL = 'https://programmer100.pythonanywhere.com/tours/'

connection = sqlite3.connect("data.db")

def scrape(url):
    """Scrape the page source from the URL"""

    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    """Extract the required content from the html text string
    with using yaml file
    """
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)['tour']
    return value


def formate_event(event):
    """Format the event in this format\n
    ["band","city","date"]
    """
    event = event.split(",")
    event = [i.strip(" ") for i in event]
    return event


def add_event(event):
    """ add event to the database using sql"""

    event = formate_event(event=event)
    cusror = connection.cursor()
    cusror.execute("INSERT INTO events VALUES(?,?,?)", event)
    connection.commit()


def read_event(event):
    """read query from the table {ie, events}"""
    
    event = formate_event(event=event)
    band, city, date = event
    cusror = connection.cursor()
    cusror.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", 
                   (band,city,date))
    rows = cusror.fetchall()
    return rows #list of tupels


def send_email():
    print("Email was sent")


if __name__ == '__main__':
    while True:
        scrapped = scrape(URL)
        extracted = extract(scrapped)
        print(extracted)

        if extracted != "No upcoming tours":
            rows = read_event(event=extracted)

            if not rows:
                add_event(extracted)
                send_email()

        time.sleep(2)

