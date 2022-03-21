class clockTime:

    def __init__(self, hours, minutes, seconds):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
    
    def setHours(self, val):
        self.hours = val

    def setMinutes(self, val):
        self.minutes = val
    
    def setSeconds(self, val):
        self.seconds = val
    
    def showTime(self):
        print("{}:{}:{}".format(self.hours,self.minutes,self.seconds))

ct = clockTime(int(input('hr: ')),int(input('min: ')),int(input('s: ')))
ct.showTime()