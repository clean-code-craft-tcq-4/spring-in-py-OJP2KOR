class EmailAlert:
    def __init__(self):
        pass
        
    emailSent = True

    
class LEDAlert:
    def __init__(self):
        pass
        
    ledGlows = True


class StatsAlerter:
    def __init__(self, maxThreshold, list):
        self.maxThreshold = maxThreshold
        self.list = list

    def checkAndAlert(self, list):
        pass
