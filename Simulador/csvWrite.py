#import csv

#import main

def reportAnalysis():
        i=1
        while i<=10:
            report = main.main(num_customers=50, num_hairdressers=2, num_secondary_hairdressers=2)
            i+=1
        #main.main(50, 1, 2)
        #main.main(50, 2, 1)
        #main.main(50, 2, 2)
        #main.main(50, 3, 2)

            with open('reports.csv', mode='a') as csv_file:
                report_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                report_writer.writerow([report["average_delay_queue_washing"],
                                            report["average_delay_queue_hairdressing"],
                                            report["average_delay_queue_payment"],
                                            report["average_num_in_queue_washing"],
                                            report["average_num_in_queue_hairdressing"],
                                            report["average_num_in_queue_payment"],
                                            report["washing_server_utilization"],
                                            report["hairdressing_server_utilization"],
                                            report["payment_server_utilization"],
                                            report["time_simulation_ended"]])

if __name__ == '__main__':
    reportAnalysis()