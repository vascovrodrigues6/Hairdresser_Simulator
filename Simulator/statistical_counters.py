class StatisticalCounters:

    def __init__(self):
        self.num_custs_delayed_washing = 0
        self.num_custs_delayed_hairdressing = 0
        self.num_custs_delayed_payment = 0
        self.total_delay_washing = 0
        self.total_delay_hairdressing = 0
        self.total_delay_payment = 0
        self.area_num_in_q_washing = 0
        self.area_num_in_q_hairdressing = 0
        self.area_num_in_q_payment = 0
        self.area_washing_status = 0
        self.area_hairdressing_status = 0
        self.area_payment_status = 0
        self.num_in_queue_washing = 0
        self.num_in_queue_hairdressing = 0
        self.num_in_queue_payment = 0


    def updateNumCustsDelayedWashing(self):
        self.num_custs_delayed_washing += 1

    def updateNumCustsDelayedHairdressing(self):
        self.num_custs_delayed_hairdressing += 1

    def updateNumCustsDelayedPayment(self):
        self.num_custs_delayed_payment += 1

    def updateTotalDelayWashing(self, delay):
        self.total_delay_washing += delay

    def updateTotalDelayHairdressing(self, delay):
        self.total_delay_hairdressing += delay

    def updateTotalDelayPayment(self, delay):
        self.total_delay_payment += delay

    def updateAreaNumInQWashing(self, area_num_in_q):
        self.area_num_in_q_washing = area_num_in_q

    def updateAreaNumInQHairdressing(self, area_num_in_q):
        self.area_num_in_q_hairdressing = area_num_in_q

    def updateAreaNumInQPayment(self, area_num_in_q):
        self.area_num_in_q_payment = area_num_in_q

    def updateAreaWashingStatus(self, area_washing_status):
        self.area_washing_status = area_washing_status

    def updateAreaHairdressingStatus(self, area_hairdressing_status):
        self.area_hairdressing_status = area_hairdressing_status

    def updateAreaPaymentStatus(self, area_payment_status):
        self.area_payment_status = area_payment_status

    def updateNumInQWashing(self):
        self.num_in_queue_washing += 1

    def updateNumInQHairdressing(self):
        self.num_in_queue_hairdressing += 1

    def updateNumInQPayment(self):
        self.num_in_queue_payment += 1