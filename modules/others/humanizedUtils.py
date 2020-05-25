
from time import sleep
from random import random


class HumanizedUtils:

    def __init__(self, typeMinCharPerMinute, typeMaxCharPerMinute):
        self.typeMinCharPerMinute = typeMinCharPerMinute
        self.typeMaxCharPerMinute = typeMaxCharPerMinute

    def send_keys_slowed(self, element, text: str):
        for i in text:
            element.send_keys(i)
            waitUntilNextChar = 60 / (self.typeMinCharPerMinute + (random() * (self.typeMaxCharPerMinute-self.typeMinCharPerMinute)) )
            sleep(waitUntilNextChar)

    def randomSlow(self, min: float, max: float):
        sleep ( min + (random() * (max-min)))