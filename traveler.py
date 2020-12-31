import time as tm
class t_traveler():
    
    def __init__(self):   
        
        self.laps = []
        self.lap_name = []
    
    def start(self):
        self.now = tm.time()
        print('Timer Started')
        
    def end(self):
        self.later = tm.time()
        print('Timer Stopped')
        
    def lap(self,lap_name='Lap'):
        seg_time = tm.time() - self.now
        self.laps.append(f'{seg_time}')
        self.lap_name.append(lap_name)
        print(f'{lap_name} recorded:')
        print(f'{lap_name} {len(self.laps)}:{int(seg_time)}')
        
    def clear(self):
        self.stop = None
        self.now = None
        self.laps = []
        self.lap_name = []
    def details(self):
        try:
  
            counter = 0
            seconds = int(self.later - self.now)
            minutes = int(seconds / 60)
            hours = int(minutes / 60)
            print(f'Process took {hours} hours, {minutes} minutes, {seconds} second')

            if self.laps:
                print(f'Total Laps: {len(self.laps)}')

                for lap in self.laps:
                    counter += 1

                    seconds = int(float(lap))
                    minutes = int(seconds / 60)
                    hours = int(minutes / 60)
                    print(f'{self.lap_name[counter - 1]} {counter}: {hours} hours, {minutes} minutes, {seconds} second')
        except TypeError:
            print('Please Run Timer ,Prior to getting details')
