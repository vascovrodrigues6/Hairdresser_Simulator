from simulation_status import SimulationStatus
from statistical_counters import StatisticalCounters
from events import Events

class ReportGenerator:
    
    def reportGenerator(events: Events, simulation_status: SimulationStatus, statistical_counters: StatisticalCounters):
        average_delay_queue_washing = statistical_counters.total_delay_washing / statistical_counters.num_custs_delayed_washing if statistical_counters.num_custs_delayed_washing > 0 else 0
        average_delay_queue_hairdressing = statistical_counters.total_delay_hairdressing / statistical_counters.num_custs_delayed_hairdressing if statistical_counters.num_custs_delayed_hairdressing > 0 else 0
        average_delay_queue_payment = statistical_counters.total_delay_payment / statistical_counters.num_custs_delayed_payment if statistical_counters.num_custs_delayed_payment > 0 else 0
        average_num_in_queue_washing = statistical_counters.area_num_in_q_washing / simulation_status.simulation_clock
        average_num_in_queue_hairdressing = statistical_counters.area_num_in_q_hairdressing / simulation_status.simulation_clock
        average_num_in_queue_payment = statistical_counters.area_num_in_q_payment / simulation_status.simulation_clock
        washing_server_utilization = statistical_counters.area_washing_status / simulation_status.simulation_clock
        hairdressing_server_utilization = statistical_counters.area_hairdressing_status / simulation_status.simulation_clock
        payment_server_utilization = statistical_counters.area_payment_status / simulation_status.simulation_clock
        time_simulation_ended = simulation_status.simulation_clock
        return {"average_delay_queue_washing": average_delay_queue_washing, "average_delay_queue_hairdressing": average_delay_queue_hairdressing, "average_delay_queue_payment": average_delay_queue_payment,
                "average_num_in_queue_washing": average_num_in_queue_washing, "average_num_in_queue_hairdressing": average_num_in_queue_hairdressing, "average_num_in_queue_payment": average_num_in_queue_payment,
                "washing_server_utilization": washing_server_utilization, "hairdressing_server_utilization": hairdressing_server_utilization, "payment_server_utilization": payment_server_utilization, 
                "time_simulation_ended": time_simulation_ended}