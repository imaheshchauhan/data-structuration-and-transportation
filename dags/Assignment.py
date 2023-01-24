from collections import Counter
from datetime import datetime,date
from time import mktime
import json
from dataclasses import dataclass
import requests
from airflow.decorators import dag, task

BASE_URL = "https://opensky-network.org/api"

def to_seconds_since_epoch(input_date: str) -> int:
  return int(mktime(date.fromisoformat(input_date).timetuple()))

@dataclass
class Flight:
    icao24: str
    firstSeen: str
    estDepartureAirport: str
    lastSeen: str
    estArrivalAirport: str
    callsign: str
    estDepartureAirportHorizDistance: str
    estDepartureAirportVertDistance: str
    estArrivalAirportHorizDistance: str
    estArrivalAirportVertDistance: str
    departureAirportCandidatesCount: str
    arrivalAirportCandidatesCount: str


def from_dict(obj) -> Flight :
    _icao24 = str(obj.get("icao24"))
    _firstSeen = str(obj.get("firstSeen"))
    _estDepartureAirport = str(obj.get("estDepartureAirport"))
    _lastSeen = str(obj.get("lastSeen"))
    _estArrivalAirport = str(obj.get("estArrivalAirport"))
    _callsign = str(obj.get("callsign"))
    _estDepartureAirportHorizDistance = str(obj.get("estDepartureAirportHorizDistance"))
    _estDepartureAirportVertDistance = str(obj.get("estDepartureAirportVertDistance"))
    _estArrivalAirportHorizDistance = str(obj.get("estArrivalAirportHorizDistance"))
    _estArrivalAirportVertDistance = str(obj.get("estArrivalAirportVertDistance"))
    _departureAirportCandidatesCount = str(obj.get("departureAirportCandidatesCount"))
    _arrivalAirportCandidatesCount = str(obj.get("arrivalAirportCandidatesCount"))
    return Flight(_icao24, _firstSeen, _estDepartureAirport, _lastSeen, _estArrivalAirport, _callsign, _estDepartureAirportHorizDistance, _estDepartureAirportVertDistance, _estArrivalAirportHorizDistance, _estArrivalAirportVertDistance, _departureAirportCandidatesCount, _arrivalAirportCandidatesCount)



@dag(
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False
)

def assignment():
    @task
    def read_flights(url: str) -> json:
        

        params = {
            "airport": "LFPG", # ICAO code for CDG
            "begin": to_seconds_since_epoch("2022-12-01"),
            "end": to_seconds_since_epoch("2022-12-02")
        }

        cdg_flights = f"{url}/flights/departure"

        response = requests.get(cdg_flights, params=params)

        flights = response.text
        return flights
        #counter = Counter([flight["estArrivalAirport"] for flight in flights if (flight["estArrivalAirport"] is not None and flight["estArrivalAirport"] != "LFPG")])
        #return counter

    
    @task
    def write_in_json(raw: str) -> None:
        for flight in json.loads(raw):
            print(from_dict(flight))
        data = json.loads(raw)
        with open("./dags/flights.json", "w") as f:
            json.dump(data, f)
        

    flights = read_flights(BASE_URL)
    jsonFlight = write_in_json(flights)
    


_ = assignment()
