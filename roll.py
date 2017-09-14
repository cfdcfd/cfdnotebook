import random
class Roll():
    '''
    set roll
    '''
    def __init__(self, size):
        self.size = size
        self.num = 0

    def roll(self):
        '''
        roll
        '''
        self.num = random.randint(1, self.size)

roll_4 = Roll(4)
roll_6 = Roll(6)
roll_8 = Roll(8)
roll_12 = Roll(12)
roll_20 = Roll(20)
for i in range(10):
    roll_20.roll()
    print(roll_20.num)


 bysgr_tuser