from simulation_status import SimulationStatus
from statistical_counters import StatisticalCounters
from events import Events

class Rotines:

    def Initialization_Rotine(num_hairdressers:int,num_secondary_hairdressers:int,num_washing_stations:int,num_hairdressing_stations:int,minimumArrivalRate:int,maximumArrivalRate:int,minimumHairwashRate:int,maximumHairwashRate:int,minimumHaircutRate:int,maximumHaircutRate:int,minimumHairdyeRate:int,maximumHairdyeRate:int,minimumHairdryRate:int,maximumHairdryRate:int,minimumPaymentRate:int,maximumPaymentRate:int):
        simulation_status = SimulationStatus(num_hairdressers,num_secondary_hairdressers,num_washing_stations,num_hairdressing_stations)
        statistical_counters = StatisticalCounters()
        events_list = Events(minimumArrivalRate,maximumArrivalRate,minimumHairwashRate,maximumHairwashRate,minimumHaircutRate,maximumHaircutRate,minimumHairdyeRate,maximumHairdyeRate,minimumHairdryRate,maximumHairdryRate,minimumPaymentRate,maximumPaymentRate)
        Events.generateFirstArrivalEvent(events_list)
        return {'simulation_status': simulation_status, 'statistical_counters': statistical_counters ,'events_list': events_list}

    def Temporization_Rotine(events: Events, simulation_status: SimulationStatus):
        if Events.isCurrentEventListEmpty(events):
            return -1
        else:
            nextEvent = Events.obtainNextEvent(events)
            SimulationStatus.updateTimeLastEvent(simulation_status)
            SimulationStatus.advanceSimulationClock(simulation_status,nextEvent["time"])
            nextEvent = {"eventType": nextEvent["eventType"], "time": simulation_status.simulation_clock} 
            Events.addHistoricalEvent(events, nextEvent)
            return nextEvent

    def Statistical_Update_Rotine(simulation_status: SimulationStatus, statistical_counters: StatisticalCounters):
        time_since_last_event = simulation_status.simulation_clock - simulation_status.time_last_event
        new_area_num_in_q_washing = statistical_counters.area_num_in_q_washing + statistical_counters.num_in_queue_washing * time_since_last_event
        new_area_num_in_q_hairdressing = statistical_counters.area_num_in_q_hairdressing + statistical_counters.num_in_queue_hairdressing * time_since_last_event
        new_area_num_in_q_payment = statistical_counters.area_num_in_q_payment + statistical_counters.num_in_queue_payment * time_since_last_event
        StatisticalCounters.updateAreaNumInQWashing(statistical_counters, new_area_num_in_q_washing)
        StatisticalCounters.updateAreaNumInQHairdressing(statistical_counters, new_area_num_in_q_hairdressing)
        StatisticalCounters.updateAreaNumInQPayment(statistical_counters, new_area_num_in_q_payment)        
        new_area_washing_status = statistical_counters.area_washing_status + SimulationStatus.isAnyWashingStationGettingUsed(simulation_status) * time_since_last_event
        StatisticalCounters.updateAreaWashingStatus(statistical_counters, new_area_washing_status) #Não está certo devido ao clock
        new_area_hairdressing_status = statistical_counters.area_hairdressing_status + SimulationStatus.isAnyHairdressingStationGettingUsed(simulation_status) * time_since_last_event
        StatisticalCounters.updateAreaHairdressingStatus(statistical_counters, new_area_hairdressing_status)
        new_area_payment_status = statistical_counters.area_payment_status + (not simulation_status.payment_station_free_status) * time_since_last_event
        StatisticalCounters.updateAreaPaymentStatus(statistical_counters, new_area_payment_status)

    def Arrival_Event_Rotine(events: Events, simulation_status: SimulationStatus, statistical_counters: StatisticalCounters, generateNext: bool):
        print("Client arrived at " + str(simulation_status.simulation_clock))
        if generateNext:
            nextArrival = Events.generateArrivalEvent(events)
            nextEvent = {"eventType": nextArrival["eventType"], "time": simulation_status.simulation_clock + nextArrival["generatedTime"]}
            Events.addEvent(events, nextEvent)
        isWashingStationFree = SimulationStatus.checkFreeWashingStation(simulation_status)
        isSecondaryHairdresserAvailable = SimulationStatus.checkFreeSecondaryHairdresser(simulation_status)
        if isWashingStationFree != -1 or isSecondaryHairdresserAvailable != -1:
            SimulationStatus.changeWashingStationStatus(simulation_status,isWashingStationFree)
            SimulationStatus.changeSecondaryHairdresserStatus(simulation_status, isSecondaryHairdresserAvailable)
            StatisticalCounters.updateNumInQWashing(statistical_counters)
            washingEvent = Events.generateFirstHairWashEvent(events)
            nextEvent = {"eventType": washingEvent["eventType"], "time": simulation_status.simulation_clock + washingEvent["generatedTime"]}
            Events.addEvent(events,nextEvent)
        else:
            SimulationStatus.addClientToWashingWaitingList(simulation_status, [simulation_status.simulation_clock,"first"])

    def Washing_End_Event(events: Events, simulation_status: SimulationStatus, statistical_counters: StatisticalCounters, isLast: bool):
        if isLast:
            print("Client ended washing post for the last time at " + str(simulation_status.simulation_clock))
        else:
            print("Client ended washing post for the first time at " + str(simulation_status.simulation_clock))
        if len(simulation_status.washing_waiting_list) == 0:
            SimulationStatus.changeWashingStationStatusAll(simulation_status)
        else:
            nextClient = SimulationStatus.obtainNextClientForWashing(simulation_status)
            delay = simulation_status.simulation_clock - simulation_status.time_last_event
            if delay > 0:
                StatisticalCounters.updateTotalDelayWashing(statistical_counters, delay)
                StatisticalCounters.updateNumCustsDelayedWashing(statistical_counters)
            StatisticalCounters.updateNumInQWashing(statistical_counters)
            eventType = nextClient[1]
            eventTime = nextClient[0]
            if eventType == "last":
                washingEvent = Events.generateLastHairWashEvent(events)
                nextEvent = {"eventType": washingEvent["eventType"], "time": eventTime + washingEvent["generatedTime"]}
                Events.addEvent(events, nextEvent)
            else:
                washingEvent = Events.generateFirstHairWashEvent(events)
                nextEvent = {"eventType": washingEvent["eventType"], "time": eventTime + washingEvent["generatedTime"]}
                Events.addEvent(events, nextEvent)
        if not isLast:
            generatedEventNumber = Events.generateCustomerEventsProbability(events)
            isHairdressingStationFree = SimulationStatus.checkFreeHairdressingStation(simulation_status)
            isHairdresserAvailable = SimulationStatus.checkFreeHairdresser(simulation_status)
            if generatedEventNumber <= 50:
                if isHairdressingStationFree != -1 or isHairdresserAvailable != -1:
                    SimulationStatus.changeHairdressingStationStatus(simulation_status, isHairdressingStationFree)
                    SimulationStatus.changeHairdresserStatus(simulation_status, isHairdresserAvailable)
                    StatisticalCounters.updateNumInQHairdressing(statistical_counters)
                    haircutEvent = Events.generateHairCutEvent(events)
                    nextEvent = {"eventType": haircutEvent["eventType"], "time": simulation_status.simulation_clock + haircutEvent["generatedTime"]}
                    Events.addEvent(events, nextEvent)
                else:
                    SimulationStatus.addClientToHairdressingWaitingList(simulation_status, [simulation_status.simulation_clock,"haircut"])
                    #SimulationStatus.addClientToHairdressingWaitingList(simulation_status, simulation_status.simulation_clock)
            if generatedEventNumber > 50 and generatedEventNumber <= 85:
                if isHairdressingStationFree != -1 or isHairdresserAvailable != -1:
                    SimulationStatus.changeHairdressingStationStatus(simulation_status, isHairdressingStationFree)
                    SimulationStatus.changeHairdresserStatus(simulation_status, isHairdresserAvailable)
                    StatisticalCounters.updateNumInQHairdressing(statistical_counters)
                    hairdryingEvent = Events.generateHairDryEvent(events)
                    nextEvent = {"eventType": hairdryingEvent["eventType"], "time": simulation_status.simulation_clock + hairdryingEvent["generatedTime"]}
                    Events.addEvent(events, nextEvent)
                else:
                    SimulationStatus.addClientToHairdressingWaitingList(simulation_status, [simulation_status.simulation_clock,"hairdry"])
                    #SimulationStatus.addClientToHairdressingWaitingList(simulation_status, simulation_status.simulation_clock)
            if generatedEventNumber > 85:
                if isHairdressingStationFree != -1 or isHairdresserAvailable != -1:
                    SimulationStatus.changeHairdressingStationStatus(simulation_status, isHairdressingStationFree)
                    SimulationStatus.changeHairdresserStatus(simulation_status, isHairdresserAvailable)
                    StatisticalCounters.updateNumInQHairdressing(statistical_counters)
                    hairdyeingEvent = Events.generateHairDyeEvent(events)
                    nextEvent = {"eventType": hairdyeingEvent["eventType"], "time": simulation_status.simulation_clock + hairdyeingEvent["generatedTime"]}
                    Events.addEvent(events, nextEvent)
                else:
                    SimulationStatus.addClientToHairdressingWaitingList(simulation_status, [simulation_status.simulation_clock,"hairdye"])
                    #SimulationStatus.addClientToHairdressingWaitingList(simulation_status, simulation_status.simulation_clock)
        else:
            isHairdressingStationFree = SimulationStatus.checkFreeHairdressingStation(simulation_status)
            isHairdresserAvailable = SimulationStatus.checkFreeHairdresser(simulation_status)
            if isHairdressingStationFree != -1 or isHairdresserAvailable != -1:
                SimulationStatus.changeHairdressingStationStatus(simulation_status, isHairdressingStationFree)
                SimulationStatus.changeHairdresserStatus(simulation_status, isHairdresserAvailable)
                StatisticalCounters.updateNumInQHairdressing(statistical_counters)
                hairdryEvent = Events.generateHairDryEvent(events)
                nextEvent = {"eventType": hairdryEvent["eventType"], "time": simulation_status.simulation_clock + hairdryEvent["generatedTime"]}
                Events.addEvent(events, nextEvent)
            else:
                SimulationStatus.addClientToHairdressingWaitingList(simulation_status, [simulation_status.simulation_clock,"hairdry"])
                    
    def Haircut_End_Event(events: Events, simulation_status: SimulationStatus, statistical_counters: StatisticalCounters):
        print("Client ended haircut at " + str(simulation_status.simulation_clock))
        if len(simulation_status.hairdressing_waiting_list) == 0:
            SimulationStatus.changeHairdressingStationStatusAll(simulation_status)            
        else:
            nextClient = SimulationStatus.obtainNextClientForHairdressing(simulation_status)
            delay = simulation_status.simulation_clock - simulation_status.time_last_event
            if delay > 0:
                StatisticalCounters.updateTotalDelayPayment(statistical_counters, delay)
                StatisticalCounters.updateNumCustsDelayedPayment(statistical_counters)
            StatisticalCounters.updateNumInQPayment(statistical_counters)
            eventType = nextClient[1]
            eventTime = nextClient[0]

            if eventType == "haircut":
                haircutEvent = Events.generateHairCutEvent(events)
                nextEvent = {"eventType": haircutEvent["eventType"], "time": eventTime + haircutEvent["generatedTime"]}
                Events.addEvent(events, nextEvent)
            if eventType == "hairdry":
                hairdryEvent = Events.generateHairDryEvent(events)
                nextEvent = {"eventType": hairdryEvent["eventType"], "time": eventTime + hairdryEvent["generatedTime"]}
                Events.addEvent(events, nextEvent)
            if eventType == "hairdye":
                hairdyeEvent = Events.generateHairDyeEvent(events)
                nextEvent = {"eventType": hairdyeEvent["eventType"], "time": eventTime + hairdyeEvent["generatedTime"]}
                Events.addEvent(events, nextEvent)
        isWashingStationFree = SimulationStatus.checkFreeWashingStation(simulation_status)
        isSecondaryHairdresserAvailable = SimulationStatus.checkFreeSecondaryHairdresser(simulation_status)
        if isWashingStationFree != -1 or isSecondaryHairdresserAvailable != -1:
            SimulationStatus.changeWashingStationStatus(simulation_status,isWashingStationFree)
            SimulationStatus.changeSecondaryHairdresserStatus(simulation_status, isSecondaryHairdresserAvailable)
            StatisticalCounters.updateNumInQWashing(statistical_counters)
            washingEvent = Events.generateLastHairWashEvent(events)
            nextEvent = {"eventType": washingEvent["eventType"], "time": simulation_status.simulation_clock + washingEvent["generatedTime"]}
            Events.addEvent(events, nextEvent)
        else:
            SimulationStatus.addClientToWashingWaitingList(simulation_status, [simulation_status.simulation_clock,"last"])

    def Hairdye_End_Event(events: Events, simulation_status: SimulationStatus, statistical_counters: StatisticalCounters):
        print("Client ended hairdye at " + str(simulation_status.simulation_clock))
        if len(simulation_status.hairdressing_waiting_list) == 0:
            SimulationStatus.changeHairdressingStationStatusAll(simulation_status)            
        else:
            nextClient = SimulationStatus.obtainNextClientForHairdressing(simulation_status)
            delay = simulation_status.simulation_clock - simulation_status.time_last_event
            if delay > 0:
                StatisticalCounters.updateTotalDelayPayment(statistical_counters, delay)
                StatisticalCounters.updateNumCustsDelayedPayment(statistical_counters)
            StatisticalCounters.updateNumInQPayment(statistical_counters)
            eventType = nextClient[1]
            eventTime = nextClient[0]

            if eventType == "haircut":
                haircutEvent = Events.generateHairCutEvent(events)
                nextEvent = {"eventType": haircutEvent["eventType"], "time": eventTime + haircutEvent["generatedTime"]}
                Events.addEvent(events, nextEvent)
            if eventType == "hairdry":
                hairdryEvent = Events.generateHairDryEvent(events)
                nextEvent = {"eventType": hairdryEvent["eventType"], "time": eventTime + hairdryEvent["generatedTime"]}
                Events.addEvent(events, nextEvent)
            if eventType == "hairdye":
                hairdyeEvent = Events.generateHairDyeEvent(events)
                nextEvent = {"eventType": hairdyeEvent["eventType"], "time": eventTime + hairdyeEvent["generatedTime"]}
                Events.addEvent(events, nextEvent)

        isWashingStationFree = SimulationStatus.checkFreeWashingStation(simulation_status)
        isSecondaryHairdresserAvailable = SimulationStatus.checkFreeSecondaryHairdresser(simulation_status)
        if isWashingStationFree != -1 or isSecondaryHairdresserAvailable != -1:
            SimulationStatus.changeWashingStationStatus(simulation_status,isWashingStationFree)
            SimulationStatus.changeSecondaryHairdresserStatus(simulation_status, isSecondaryHairdresserAvailable)
            StatisticalCounters.updateNumInQWashing(statistical_counters)
            washingEvent = Events.generateLastHairWashEvent(events)
            nextEvent = {"eventType": washingEvent["eventType"], "time": simulation_status.simulation_clock + washingEvent["generatedTime"]}
            Events.addEvent(events, nextEvent)
        else:
            SimulationStatus.addClientToWashingWaitingList(simulation_status, [simulation_status.simulation_clock,"last"])

    def Hairdry_End_Event(events: Events, simulation_status: SimulationStatus, statistical_counters: StatisticalCounters):
        print("Client ended hairdry at " + str(simulation_status.simulation_clock))
        if len(simulation_status.hairdressing_waiting_list) == 0:
            SimulationStatus.changeHairdressingStationStatusAll(simulation_status)            
        else:
            nextClient = SimulationStatus.obtainNextClientForHairdressing(simulation_status)
            delay = simulation_status.simulation_clock - simulation_status.time_last_event
            if delay > 0:
                StatisticalCounters.updateTotalDelayPayment(statistical_counters, delay)
                StatisticalCounters.updateNumCustsDelayedPayment(statistical_counters)
            StatisticalCounters.updateNumInQPayment(statistical_counters)
            eventType = nextClient[1]
            eventTime = nextClient[0]

            if eventType == "haircut":
                haircutEvent = Events.generateHairCutEvent(events)
                nextEvent = {"eventType": haircutEvent["eventType"], "time": eventTime + haircutEvent["generatedTime"]}
                Events.addEvent(events, nextEvent)
            if eventType == "hairdry":
                hairdryEvent = Events.generateHairDryEvent(events)
                nextEvent = {"eventType": hairdryEvent["eventType"], "time": eventTime + hairdryEvent["generatedTime"]}
                Events.addEvent(events, nextEvent)
            if eventType == "hairdye":
                hairdyeEvent = Events.generateHairDyeEvent(events)
                nextEvent = {"eventType": hairdyeEvent["eventType"], "time": eventTime + hairdyeEvent["generatedTime"]}
                Events.addEvent(events, nextEvent)

        if simulation_status.payment_station_free_status:
            SimulationStatus.changePaymentStationStatus(simulation_status)
            StatisticalCounters.updateNumInQPayment(statistical_counters)
            paymentEvent = Events.generatePaymentEvent(events)
            nextEvent = {"eventType": paymentEvent["eventType"], "time": simulation_status.simulation_clock + paymentEvent["generatedTime"]}
            Events.addEvent(events, nextEvent)
        else:
            SimulationStatus.addClientToPaymentWaitingList(simulation_status, simulation_status.simulation_clock)

    def Payment_End_Event(events: Events, simulation_status: SimulationStatus, statistical_counters: StatisticalCounters):
        print("Client ended paying at " + str(simulation_status.simulation_clock))
        if len(simulation_status.payment_station_waiting_list) == 0:
            SimulationStatus.changePaymentStationStatus(simulation_status)            
        else:
            nextClient = SimulationStatus.obtainNextClientForPayment(simulation_status)
            delay = simulation_status.simulation_clock - simulation_status.time_last_event
            if delay > 0:
                StatisticalCounters.updateTotalDelayPayment(statistical_counters, delay)
                StatisticalCounters.updateNumCustsDelayedPayment(statistical_counters)
            StatisticalCounters.updateNumInQPayment(statistical_counters)
            paymentEvent = Events.generatePaymentEvent(events)
            nextEvent = {"eventType": paymentEvent["eventType"], "time": nextClient + paymentEvent["generatedTime"]}
            Events.addEvent(events, nextEvent)

