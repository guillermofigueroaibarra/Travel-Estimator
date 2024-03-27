'''

    Author: Guillermo Figueroa
    Date: 05/14/2021
    Prog: trip.py
    Class: CIS2531
                 
'''



class Trip:

    
    # dictionary with countries and its corresponding daily expenses cost
    cities = {"Hanoi, Viet Nam":19.80,
    "Saigon (Ho Chi Minh City), Viet Nam":20.64,
    "Vientiane, Laos":20.64,
    "Yangon, Myanmar":20.84,
    "Hoi An, Viet Nam":21.59,
    "Pokhara, Nepal":21.87,
    "Chiang Mai, Thailand":22.79,
    "Quito, Ecuador":22.80,
    "Phnom Penh, Cambodia":23.04,
    "Buenos Aires, Argentina":23.32,
    "Colombo, Sri Lanka":23.37,
    "Manila, Philippines":23.46,
    "Jakarta, Indonesia":23.48,
    "Granada (Nicaragua), Nicaragua":23.82,
    "Delhi, India":23.84,
    "Kathmandu, Nepal":23.91,
    "Goa, India":24.99,
    "Luang Prabang, Laos":25.10,
    "Zanzibar City, Tanzania":25.42,
    "La Paz, Bolivia":25.76,
    "Istanbul, Turkey":26.30,
    "Cartagena, Colombia":26.51,
    "Cusco, Peru":27.81,
    "Lima, Peru":27.81,
    "Bangkok, Thailand":28.07,
    "Cancun, Mexico":28.35,
    "Siem Reap, Cambodia":28.50,
    "Bucharest, Romania":28.74,
    "San Jose, Costa Rica":29.58,
    "Belgrade, Serbia":30.00,
    "Kuta, Bali, Indonesia":30.11,
    "Phuket, Thailand":30.71,
    "Arusha, Tanzania":30.82,
    "Mumbai, India":31.75,
    "Xian, China":32.22,
    "Santa Ana, El Salvador":32.24,
    "Kiev, Ukraine":32.96,
    "Mexico City, Mexico":33.07,
    "Beirut, Lebanon":33.77,
    "Budapest, Hungary":33.81,
    "Sofia, Bulgaria":33.81,
    "Montevideo, Uruguay":34.31,
    "Krakow, Poland":34.44,
    "Rio de Janeiro, Brazil":34.60,
    "Taipei, Taiwan":35.05,
    "Fez, Morocco":36.10,
    "Marrakech, Morocco":36.38,
    "Santiago, Chile":36.93,
    "Kuala Lumpur, Malaysia":37.09,
    "Boracay Island, Philippines":38.00,
    "Riga, Latvia":38.17,
    "Warsaw, Poland":38.56,
    "Antigua, Guatemala":38.67,
    "Dakar, Senegal":39.08,
    "Sarajevo, Bosnia and Herzegovina":39.88,
    "Vilnius, Lithuania":40.00,
    "Panama City, Panama":40.10,
    "Shanghai, China":41.24,
    "Cairo, Egypt":41.39,
    "Beijing, China": 42.33,
    "Amman, Jordan":43.80,
    "Saint Petersburg, Russia":43.87,
    "Bratislava, Slovakia":44.05,
    "Zagreb, Croatia":44.10,
    "Cesky Krumlov, Czechia":44.14,
    "Cape Town, South Africa":45.88,
    "Moscow, Russia":46.16,
    "Split, Croatia":48.76,
    "Roatán Island, Honduras":48.91,
    "Santorini, Greece":49.15,
    "Prague, Czechia":50.05,
    "Seoul, South Korea":51.2,
    "Nairobi, Kenya":52.52,
    "Tenerife, Spain":53.68,
    "Tallinn, Estonia":54.37,
    "San Pedro (Ambergris Caye), Belize":54.43,
    "Hong Kong, Hong Kong":54.55,
    "Singapore, Singapore":57.29,
    "Valletta, Malta":57.44,
    "Lisbon, Portugal":58.66,
    "Ljubljana, Slovenia":60.49,
    "Naples, Italy":63.66,
    "Athens, Greece":65.85,
    "Ibiza, Spain":66.83,
    "Cairns, Australia":68.24,
    "Montreal, Canada":68.35,
    "New Orleans, United States":69.80,
    "Macau, Macao":70.08,
    "Tokyo, Japan":71.09,
    "Berlin, Germany":71.22,
    "Bruges, Belgium":72.56,
    "Madrid, Spain":73.41,
    "Nice, France":73.41,
    "Dubrovnik, Croatia":75.11,
    "Auckland, New Zealand":75.9,
    "Abu Dhabi, United Arab Emirates":76.54,
    "Dubai, United Arab Emirates":77.22,
    "Milan, Italy":77.44,
    "Sydney, Australia":80.94,
    "Barcelona, Spain":81.10,
    "Las Vegas, United States":81.40,
    "Luxembourg City, Luxembourg":81.46,
    "Florence, Italy":82.20,
    "Brisbane, Australia":82.52,
    "Edinburgh, United Kingdom":82.68,
    "Los Angeles, United States":83.72,
    "Miami Beach, United States":85.08,
    "Rome, Italy":85.61,
    "Vienna, Austria":87.93,
    "Washington D.C., United States":89.30,
    "Salzburg, Austria":89.39,
    "Melbourne, Australia":89.92,
    "Brussels, Belgium":90.00,
    "Helsinki, Finland":90.00,
    "Dublin, Ireland":90.49,
    "Queenstown, New Zealand":90.80,
    "Hamburg, Germany":90.85,
    "Munich, Germany":91.83,
    "Reykjavik, Iceland":92.10,
    "Paris, France":92.68,
    "Vancouver, Canada":92.81,
    "Honolulu, United States":93.00,
    "Oslo, Norway":94.03,
    "Toronto, Canada":94.88,
    "Tel Aviv, Israel":95.26,
    "Bergen, Norway":97.44,
    "Stockholm, Sweden":99.64,
    "Chicago, United States":99.90,
    "Copenhagen, Denmark":101.31,
    "Interlaken, Switzerland":102.78,
    "London, United Kingdom":104.20,
    "San Francisco, United States":107.69,
    "Boston, United States":110.52,
    "Amsterdam, Netherlands":120.07,
    "New York City, United States":123.58,
    "Venice, Italy":124.88,
    "Zurich, Switzerland":137.78}


    


    def __init__(self, city, days):
        self.__city = city
        self.__days = days


    # getter and setter for the city
    @property
    def city(self):
        if self.__city in Trip.cities:
            return self.__city
        else:
            return False
    @city.setter
    def city(self, city):
        self.__city = city


    # getter and setter for the number of days
    @property
    def days(self):
        return self.__days
        
    @days.setter
    def days(self, days):
        self.__days = days





    # method to calculate the cost
    @property
    def cost(self):
        totalCost = 0
        totalCost = float(Trip.cities.get(self.__city)) * int(self.__days)
        return totalCost


    # method to display cheap cities
    @classmethod
    def cheapCities(self):

        cheapCities = ''
        
        for city, dailyCost in Trip.cities.items():
            if  dailyCost < 37:
                cheapCities += ' "' + city + '" '
        return cheapCities

    
    # method to display  midRange price cities
    @classmethod
    def midRangeCities(self):

        midRangeCities = ''
        for city, dailyCost in Trip.cities.items():

            if dailyCost > 37 and dailyCost < 76:
                midRangeCities += ' "' + city + '" '
        return midRangeCities
    
                
    # method to display expensive cities
    @classmethod
    def expensiveCities(self):

        expensiveCities = ''
        
        for city, dailyCost in Trip.cities.items():

            if dailyCost > 76:
                expensiveCities += ' "' + city + '" '
        return expensiveCities





