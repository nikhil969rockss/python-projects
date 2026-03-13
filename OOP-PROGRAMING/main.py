import requests
import selectorlib
import sqlite3
import time

URL = 'https://programmer100.pythonanywhere.com/tours/'


class Event():
    def scrape(self,url):
        """Scrape the page source from the URL"""

        response = requests.get(url)
        source = response.text
        return source


    def extract(self,source):
        """Extract the required content from the html text string
        with using yaml file
        """
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)['tour']
        return value


class Database():

    def __init__(self):
        self.connection = sqlite3.connect("data.db")


    def formate_event(self,event):
        """Format the event in this format\n
        ["band","city","date"]
        """
        event = event.split(",")
        event = [i.strip(" ") for i in event]
        return event


    def add(self,event):
        """ add event to the database using sql"""

        event = self.formate_event(event=event)
        cusror = self.connection.cursor()
        cusror.execute("INSERT INTO events VALUES(?,?,?)", event)
        self.connection.commit()


    def read(self,event):
        """read query from the table {ie, events}"""
        
        event = self.formate_event(event=event)
        band, city, date = event
        cusror = self.connection.cursor()
        cusror.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", 
                    (band,city,date))
        rows = cusror.fetchall()
        return rows #list of tupels


def send_email():
    print("Email was sent")


if __name__ == '__main__':
    while True:
        event = Event()
        scrapped = event.scrape(URL)
        extracted = event.extract(scrapped)
        print(extracted)

        if extracted != "No upcoming tours":
            database = Database()
            rows = database.read(event=extracted)

            if not rows:
                database.add(extracted)
                send_email()

        time.sleep(2)

