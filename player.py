import logging
from Dice import Dice

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")
logging.basicConfig(filename="log.log",
                    format="[%(levelname)s]%(module)s::%(funcName)s-->%(msg)s")


class Player:

    def __init__(self, balance) -> None:
        self.balance = balance
        self.dices = []
        logger.info(f"Player Created with balance of {self.balance}")

    def Bet(self, betting_amount):
        self.balance -= betting_amount
        logger.info(f"Current balance {self.balance}")
        return self.balance

    def Dice_count(self,dice_amount):
        for _ in range(dice_amount):
            dice = Dice()
            self.dices.append(dice)
        return self.dices

    def Roll(self):
        for dice in self.dices:
            rolled = dice.Roll()
            dice.Draw(rolled)
        return rolled
    def newBalance(self, added_amount):
        self.balance += added_amount
        return self.balance
