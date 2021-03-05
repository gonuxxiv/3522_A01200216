"""
Implements the observer pattern and simulates a simple auction.
"""
import random


class Auctioneer:
    """
    The auctioneer acts as the "core". This class is responsible for
    tracking the highest bid and notifying the bidders if it changes.
    """

    def __init__(self):
        """
        Initialize Auctioneer object.
        All initial attributes are set by default.
        """
        self.bidders = []
        self._highest_bid = 0
        self._highest_bidder = None
        self._previous_highest_bidder = "Starting Bid"

    def get_highest_bid(self):
        """
        Get highest bid
        :return: float
        """
        return self._highest_bid

    def get_highest_bidder(self):
        """
        Get highest bidder.
        :return: Bidder object
        """
        return self._highest_bidder

    def get_previous_highest_bidder(self):
        """
        Get previous highest bidder
        :return: Bidder object
        """
        return self._previous_highest_bidder

    def set_highest_bid(self, bid):
        """
        Set new highest bid.
        :param bid: float
        """
        self._highest_bid = bid

    def set_highest_bidder(self, bidder):
        """
        Set new current highest bidder.
        :param bidder: Bidder object
        """
        self._highest_bidder = bidder

    def set_previous_highest_bidder(self, bidder):
        """
        Set new previous highest bidder.
        :param bidder: Bidder object
        """
        self._previous_highest_bidder = bidder

    def register_bidder(self, bidder):
        """
        Adds a bidder to the list of tracked bidders.
        :param bidder: object with __call__(auctioneer) interface.
        """
        self.bidders.append(bidder)

    def reset_auctioneer(self):
        """
        Resets the auctioneer. Removes all the bidders and resets the
        highest bid to 0.
        """
        self.bidders.clear()

    def begin_auction(self):
        """
        Execute auction until there is no new bid.
        """
        while self.get_previous_highest_bidder() != self.get_highest_bidder():
            self._notify_bidders()
        print(f"\nThe winner of the auction is: {self.get_highest_bidder()} at {self.get_highest_bid()}")

    def _notify_bidders(self):
        """
        Executes all the bidder callbacks. Should only be called if the
        highest bid has changed.
        """
        for bidder in self.bidders:
            bidder(self)

    def accept_bid(self, bid, bidder):
        """
        Accepts a new bid and updates the highest bid. This notifies all
        the bidders via their callbacks.
        :param bid: a float.
        :precondition bid: should be higher than the existing bid.
        :param bidder: The object with __call__(auctioneer) that placed
        the bid.
        """
        print(f"{bidder.get_name()} bidded {bid} in response to "
              f"{self.get_previous_highest_bidder()}'s "
              f"bid of {self.get_highest_bid()}!")
        self.set_highest_bid(bid)
        self.set_previous_highest_bidder(self.get_highest_bidder())
        self.set_highest_bidder(bidder)


class Bidder:
    """
      Represents bidder
    """

    def __init__(self, name, budget=100, bid_probability=0.35, bid_increase_perc=1.1):
        """
        Initialize a bidder.
        :param name: string, name of bidder
        :param budget: integer, biding budget
        :param bid_probability: float, probability for bidding
        :param bid_increase_perc: float, bid increase rate
        """
        self.name = name
        self.bid_probability = bid_probability
        self.budget = budget
        self.bid_increase_perc = bid_increase_perc
        self.highest_bid = 0

    def get_name(self):
        """
        Get name of this bidder
        :return: string, name of bidder
        """
        return self.name

    def get_highest_bid(self):
        """
        Get highest bid amount of this bidder
        :return: float, highest bid amount
        """
        return self.highest_bid

    def __call__(self, auctioneer):
        """
        Execute bidding sequence.
        :param auctioneer: Auctioneer object
        """
        attempting_bid = auctioneer.get_highest_bid() * self.bid_increase_perc
        if auctioneer.get_highest_bidder() != self.name:
            if attempting_bid <= self.budget:
                if random.random() <= self.bid_probability:
                    self.highest_bid = attempting_bid
                    auctioneer.accept_bid(attempting_bid, self)

    def __str__(self):
        """
        Print the object.
        :return: a name of the bidder object
        """
        return self.name


class Auction:
    """
    Simulates an auction. Is responsible for driving the auctioneer and
    the bidders.
    """

    def __init__(self, bidders):
        """
        Initialize an auction. Requires a list of bidders that are
        attending the auction and can bid.
        :param bidders: sequence type of objects of type Bidder
        """
        self.auctioneer = Auctioneer()
        for bidder in bidders:
            self.auctioneer.register_bidder(bidder)

    def simulate_auction(self, item, start_price):
        """
        Starts the auction for the given item at the given starting
        price. Drives the auction till completion and prints the results.
        :param item: string, name of item.
        :param start_price: float
        """
        print(f"Auctioning {item} starting at {start_price}")
        self.auctioneer.set_highest_bid(start_price)
        self.auctioneer.begin_auction()

        auction_result = {x.get_name(): x.get_highest_bid() for x in self.auctioneer.bidders}

        print("\nHighest Bids Per Bidder")
        for x, y in auction_result.items():
            print(f"Bidder: {x} Highest Bid: {y}")


def add_bidder():
    """
    Create new bidder object and return it.
    :return: Bidder object
    """
    name = input("\nEnter name of the bidder: ").title()
    budget = int(input("Enter bidder budget: "))
    bid_probability = float(input("Enter bid probability: "))
    bid_increase_perc = float(input("Enter bid increase percentage: "))
    return Bidder(name, budget, bid_probability, bid_increase_perc)


def main():
    """
    The main of the program. Execute auction simulation.
    """
    bidders = []

    print("\nWelcome to the auction menu!")
    print("-----------------------")

    try:
        auction_item = input("Enter bid item: ").title()
        starting_price = int(input("Enter starting price: "))

        user_input = None
        while user_input != 1 and user_input != 3 and user_input != 4:
            print("\nChoose the following options")
            print("-----------------------")
            print("1. Use hard-coded bidders")
            print("2. Add a custom bidders")
            print("3. Start auction")
            print("4. Quit")
            string_input = input("Please enter your choice (1-3) ")

            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                # Hard-coding the bidders.
                bidders.append(Bidder("Jojo", 3000, random.random(), 1.2))
                bidders.append(Bidder("Melissa", 7000, random.random(), 1.5))
                bidders.append(Bidder("Priya", 15000, random.random(), 1.1))
                bidders.append(Bidder("Kewei", 800, random.random(), 1.9))
                bidders.append(Bidder("Scott", 4000, random.random(), 2))
            elif user_input == 2:
                bidders.append(add_bidder())
            elif user_input == 3:
                pass
            elif user_input == 4:
                pass
            else:
                print("\nCould not process the input. Please enter a"
                      " number from 1 - 3.")

        if user_input != 4:
            if len(bidders) != 0:
                print("\n\nStarting Auction!!")
                print("------------------")
                my_auction = Auction(bidders)
                my_auction.simulate_auction(auction_item, starting_price)
            else:
                print("\nAuction ended: No registered bidders")
        else:
            print("\nAuction ended")
    except ValueError as e:
        print(f"\nTypeError caught! Exception: {e}")
    except KeyboardInterrupt:
        print(f"\n\nProgram stopped!")


if __name__ == '__main__':
    main()
