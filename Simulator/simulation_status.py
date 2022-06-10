class SimulationStatus:

    def __init__(self, num_hairdressers,num_secondary_hairdressers,num_washing_stations,num_hairdressing_stations):
        self.simulation_clock = 0
        self.washing_station_free_status = [True for i in range(num_washing_stations)]
        self.washing_waiting_list = []
        self.hairdressing_station_free_status = [True for i in range(num_hairdressing_stations)]
        self.hairdressing_waiting_list = []
        self.payment_station_free_status = True
        self.payment_station_waiting_list = []
        self.num_in_queue_washing = 0
        self.num_in_queue_hairdressing = 0
        self.num_in_queue_payment = 0
        self.hairdresser_free_status = [True for i in range(num_hairdressers)]
        self.secondary_hairdresser_free_status = [True for i in range(num_secondary_hairdressers)]
        self.time_last_event = 0

    def changeWashingStationStatus(self, index):
        self.washing_station_free_status[index] = not self.washing_station_free_status[index]

    def changeWashingStationStatusAll(self):
        self.washing_station_free_status = [True for i in range(len(self.washing_station_free_status))] 

    def changeHairdressingStationStatus(self, index):
        self.hairdressing_station_free_status[index] = not self.hairdressing_station_free_status[index]

    def changeHairdressingStationStatusAll(self):
        self.hairdressing_station_free_status = [True for i in range(len(self.hairdressing_station_free_status))]

    def changePaymentStationStatus(self):
        self.payment_station_free_status = not self.payment_station_free_status

    def increaseNumInQueueWashing(self):
        self.num_in_queue_washing += 1

    def decreaseNumInQueueWashing(self):
        self.num_in_queue_washing -= 1

    def increaseNumInQueueHairdressing(self):
        self.num_in_queue_hairdressing += 1

    def decreaseNumInQueueHairdressing(self):
        self.num_in_queue_hairdressing -= 1

    def increaseNumInQueuePayment(self):
        self.num_in_queue_payment += 1

    def decreaseNumInQueuePayment(self):
        self.num_in_queue_payment -= 1

    def advanceSimulationClock(self, time_to_add):
        self.simulation_clock = time_to_add

    def updateTimeLastEvent(self):
        self.time_last_event = self.simulation_clock

    def addClientToWashingWaitingList(self,client):
        self.washing_waiting_list.append(client)
        self.increaseNumInQueueWashing()
    
    def addClientToHairdressingWaitingList(self,client):
        self.hairdressing_waiting_list.append(client)
        self.increaseNumInQueueHairdressing()

    def addClientToPaymentWaitingList(self,client):
        self.payment_station_waiting_list.append(client)
        self.increaseNumInQueueHairdressing()

    def obtainNextClientForWashing(self):
        nextClient = self.washing_waiting_list[0]
        self.washing_waiting_list.pop(0)
        self.decreaseNumInQueueWashing()
        return nextClient 

    def obtainNextClientForHairdressing(self):
        nextClient = self.hairdressing_waiting_list[0]
        self.hairdressing_waiting_list.pop(0)
        self.decreaseNumInQueueHairdressing()
        return nextClient 
    
    def obtainNextClientForPayment(self):
        nextClient = self.payment_station_waiting_list[0]
        self.payment_station_waiting_list.pop(0)
        self.decreaseNumInQueuePayment()
        return nextClient 

    def checkFreeWashingStation(self):
        for index in range(len(self.washing_station_free_status)):
            if self.washing_station_free_status[index]:
                return index
        return -1
    
    def checkFreeHairdressingStation(self):
        for index in range(len(self.secondary_hairdresser_free_status)):
            if self.hairdressing_station_free_status[index]:
                return index
        return -1

    def checkFreeHairdresser(self):
        for index in range(len(self.hairdresser_free_status)):
            if self.hairdresser_free_status[index]:
                return index
        return -1

    def checkFreeSecondaryHairdresser(self):
        for index in range(len(self.secondary_hairdresser_free_status)):
            if self.secondary_hairdresser_free_status[index]:
                return index
        return -1

    def changeHairdresserStatus(self, index):
        self.hairdresser_free_status[index] = not self.hairdresser_free_status[index]

    def changeSecondaryHairdresserStatus(self, index):
        self.secondary_hairdresser_free_status[index] = not self.secondary_hairdresser_free_status[index]

    def isAnyWashingStationGettingUsed(self):
        return False in self.washing_station_free_status
    
    def isAnyHairdressingStationGettingUsed(self):
        return False in self.hairdresser_free_status

