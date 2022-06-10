from rotines import Rotines
from report_generator import ReportGenerator
import UI
import ReportUI


def main(num_customers,num_hairdressers,num_secondary_hairdressers,num_washing_stations=2,num_hairdressing_stations=3,minimumArrivalRate=15,maximumArrivalRate=20,minimumHairwashRate=5,maximumHairwashRate=10,minimumHaircutRate=15,maximumHaircutRate=25,minimumHairdyeRate=30,maximumHairdyeRate=60,minimumHairdryRate=5,maximumHairdryRate=10,minimumPaymentRate=3,maximumPaymentRate=5):
    initilized_parameters = Rotines.Initialization_Rotine(num_hairdressers,num_secondary_hairdressers,num_washing_stations,num_hairdressing_stations,minimumArrivalRate,maximumArrivalRate,minimumHairwashRate,maximumHairwashRate,minimumHaircutRate,maximumHaircutRate,minimumHairdyeRate,maximumHairdyeRate,minimumHairdryRate,maximumHairdryRate,minimumPaymentRate,maximumPaymentRate)
    simulation_status = initilized_parameters["simulation_status"]
    statistical_counters = initilized_parameters["statistical_counters"]
    events_list = initilized_parameters["events_list"]

    number_of_clients = 0

    while number_of_clients <= num_customers: 
        nextEvent = Rotines.Temporization_Rotine(events_list,simulation_status) 
        #print(nextEvent)
        if nextEvent == -1:
            break
        Rotines.Statistical_Update_Rotine(simulation_status,statistical_counters)
        if nextEvent["eventType"] == "Customer Arrival" or nextEvent["eventType"] == "First Customer Arrival":
            if number_of_clients == num_customers-1:
                Rotines.Arrival_Event_Rotine(events_list,simulation_status,statistical_counters,False)
            else:
                Rotines.Arrival_Event_Rotine(events_list,simulation_status,statistical_counters,True) 
            number_of_clients += 1
            continue    
        if nextEvent["eventType"] == "First hair wash Event":
            Rotines.Washing_End_Event(events_list,simulation_status,statistical_counters,False)
            continue
        if nextEvent["eventType"] == "Last hair wash Event":
            Rotines.Washing_End_Event(events_list,simulation_status,statistical_counters,True)
            continue
        if nextEvent["eventType"] == "Hair cut Event":
            Rotines.Haircut_End_Event(events_list,simulation_status,statistical_counters)
            continue
        if nextEvent["eventType"] == "Hair dye Event":
            Rotines.Hairdye_End_Event(events_list,simulation_status,statistical_counters)
            continue
        if nextEvent["eventType"] == "Hair dry Event":
            Rotines.Hairdry_End_Event(events_list,simulation_status,statistical_counters)
            continue
        if nextEvent["eventType"] == "Payment Event":
            Rotines.Payment_End_Event(events_list,simulation_status,statistical_counters)
            continue
    ReportUI.Report(ReportGenerator.reportGenerator(events_list,simulation_status,statistical_counters))
    #return ReportGenerator.reportGenerator(events_list,simulation_status,statistical_counters)
    print(ReportGenerator.reportGenerator(events_list,simulation_status,statistical_counters))

if __name__ == "__main__":
    UI.Ui()

    #main(num_customers=3,num_hairdressers=2,num_secondary_hairdressers=2) #https://stackoverflow.com/questions/42747469/how-to-pass-arguments-to-main-function-within-python-module