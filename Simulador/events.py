import random

class Events:
    
    def __init__(self,minimumArrivalRate,maximumArrivalRate,minimumHairwashRate,maximumHairwashRate,minimumHaircutRate,maximumHaircutRate,minimumHairdyeRate,maximumHairdyeRate,minimumHairdryRate,maximumHairdryRate,minimumPaymentRate,maximumPaymentRate):
        self.current_event_list = []
        self.historical_event_list = [] 
        self.minimumArrivalRate = minimumArrivalRate    
        self.maximumArrivalRate = maximumArrivalRate
        self.minimumHairwashRate = minimumHairwashRate 
        self.maximumHairwashRate = maximumHairwashRate
        self.minimumHaircutRate = minimumHaircutRate 
        self.maximumHaircutRate = maximumHaircutRate
        self.minimumHairdyeRate = minimumHairdyeRate 
        self.maximumHairdyeRate = maximumHairdyeRate
        self.minimumHairdryRate = minimumHairdryRate 
        self.maximumHairdryRate = maximumHairdryRate
        self.minimumPaymentRate = minimumPaymentRate 
        self.maximumPaymentRate = maximumPaymentRate

    def addEvent(self, newEvent):
        self.current_event_list.append(newEvent)
        self.current_event_list = sorted(self.current_event_list, key = lambda i: i['time'])

    def addHistoricalEvent(self, newEvent):
        self.historical_event_list.append(newEvent)

    def removeEvent(self, newEvent):
        self.current_event_list.remove(newEvent) 

    def generateFirstArrivalEvent(self):
        time = random.randint(self.minimumArrivalRate,self.maximumArrivalRate)
        arrivalEvent = {"eventType": "First Customer Arrival", "time": time}
        self.addEvent(arrivalEvent)

    def generateArrivalEvent(self):
        time = random.randint(self.minimumArrivalRate,self.maximumArrivalRate)
        return {"eventType": "Customer Arrival", "generatedTime": time}

    def generateFirstHairWashEvent(self):
        time = random.randint(self.minimumHairwashRate,self.maximumHairwashRate)
        return {"eventType": "First hair wash Event", "generatedTime": time}

    def generateLastHairWashEvent(self):
        time = random.randint(self.minimumHairwashRate,self.maximumHairwashRate)
        return {"eventType": "Last hair wash Event", "generatedTime": time}

    def generateHairCutEvent(self):
        time = random.randint(self.minimumHaircutRate,self.maximumHaircutRate)
        return {"eventType": "Hair cut Event", "generatedTime": time}

    def generateHairDyeEvent(self):
        time = random.randint(self.minimumHairdyeRate,self.maximumHairdyeRate)
        return {"eventType": "Hair dye Event", "generatedTime": time}

    def generateHairDryEvent(self):
        time = random.randint(self.minimumHairdryRate,self.maximumHairdryRate)
        return {"eventType": "Hair dry Event", "generatedTime": time} 

    def generatePaymentEvent(self):
        time = random.randint(self.minimumPaymentRate,self.maximumPaymentRate)
        return {"eventType": "Payment Event", "generatedTime": time}             

    def generateCustomerEventsProbability(self):
        return random.randint(0,100)

    def isCurrentEventListEmpty(self):
        return len(self.current_event_list) == 0     

    def obtainNextEvent(self):
        nextEvent = self.current_event_list[0]
        self.current_event_list.pop(0)
        return nextEvent        