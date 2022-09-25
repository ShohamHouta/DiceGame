import random
import logging

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")
logging.basicConfig(filename="log.log",
                    format="[%(levelname)s]%(module)s::%(funcName)s-->%(msg)s")


class Dice:

    def __init__(self) -> None:
        self.Sides = dict()
        for i in range(1, 7):
            self.Sides[i] = i
        logger.info(self.Sides)

    def Roll(self):

        self.side = random.randint(1, 6)
        logger.info(self.Sides[self.side])
        return self.Sides[self.side]

    
    def Draw(self,rolled_side):
        match rolled_side:
            case 1:
                print(""" -----
|     |
|  o  |
|     |
 -----""")
            case 2:
                print(""" -----
| o   |
|     |
|   o |
 -----""")
            case 3:
                print(""" -----
| o   |
|  o  |
|   o |
 -----""")
            case 4:
                print(""" -----
| o o |
|     |
| o o |
 -----""")
            case 5:
                print(""" -----
| o o |
|  o  |
| o o |
 -----""")
            case 6:
                print(""" -----
| o o |
| o o |
| o o |
 -----""")
