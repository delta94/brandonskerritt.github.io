import csv

class finance():
    """
    Idea is:
    during the month any income earned goes into a NatWest account
    On the first monday of the next month (when interest is paid):
    * move all left over-funds from Monzo to NatWest
    * Move 80% from the account to Monzo
        - this leaves 20% extra each month
        - effectively compound saving for my emergency fund
        - leave in NatWest for the interest rate (currently 1.5%)
    * using 10% from my monzo account, buy something like cryptocurrencies
        - high risk, high reward
        - if it doesn't go up, it's only 10%
        - if it does, I've made a bit of money
    * using 40% from my monzo account, invest into low - mid stuff
        - bonds mainly
        - and equities
        - Currently I'm paying a robo-advisor (like AI, but barely AI) to do this for me
        - it diverisifes it really well and I don't any fees on the first 5k
        - it may not be optimal but it works and I don't know enough about investing to comftorably do it myself
        - Also the founder checks out as a sound guy, he's not looking to make money he's more into
        - "Wow this is a really cool problem we can work on"
        - Only 30% of my bonds are UK based so if Brexit causes mayhem it should be okay :)
    * put some of the rest of the money into pots like holiday, christmas etc
        - using IFFT automate a weekly amount to be moved from a pot to my account

    most of this isn't automated yet, but OpenBanking is a thing now, imagine if this was possible
    
    Ideas for this app:
    * I currently have IFFT set up to auto-track all my Monzo expenses in google sheets
        - would be cool if I could have a sumary in this program
    * Log all my income into a google sheets
        - have the summary here also
        - for tax purposes too
    * Rate me on how good I did this 
    * track my browser usage to see if I actually use the subscriptions I'm subscribed to
    * Look at peer-to-peer lending
    * Read Tim Hales book on investing
    * Consider getting a Vanguard ETF next tax year
    * Correlate FitBit data with Monzo data
        - I have a suspicion that when I don't work out on a day I spend more on chocolate
        - we can prove this using FitBit data

    ** ATTRIBUTES **
    - initial_take_out
        how much is initially taken out of the bank account (leaving 20%)
    - updated_take_Out
        this is the same as initial_take_out but is updated in the program when 10% is removed
    - high_vol
        10% of updated_take_out
        remove 10% from updated_take_out
    - invest
        40% of updated_take_out
        remove 40% from updated_take_out
    - other_savings
        the rest of the 50% (the full updated_take_out) or 50% of initial_take_out
    
    ** METHODS **
    - __init__
        constructor
    - update_take_out
        used to update the attribute of same name
    - check
        checks to see if the result of adding high_vol + invest + other_savings is = to initial_take_out
    - printAll
        prints all the attributes nicely
    """

    def __init__(self, x):
        """ Constructor method """
        self.initial_natwest = x 
        # TODO replace latest with CSV value
        latest = 360

        # If you've put in £50 and theres £100 in the account this will mess it up
        ## that's why absolute is used.
        # I also want to save 20% of the natwest account in the savings itself
        newly_added = float(abs(self.initial_natwest - latest))
        self.initial_take_out = float(newly_added * 0.8)
        self.updated_take_out = float(self.initial_take_out)

        self.high_vol = 0.0
        self.invest = 0.0
        self.other_savings = 0.0

        # 10% for cryptocurrency
        self.high_vol = self.updated_take_out * 0.10
        self.updateTakeout(self.high_vol)

        # 40% for low - mid range investments
        self.invest = self.updated_take_out * 0.40
        self.updateTakeout(self.invest)

        self.left_with = self.initial_take_out - (self.invest + self.high_vol)

        self.left_over = self.initial_natwest - self.initial_take_out

    def updateTakeout(self, money):
        """ Method to update the updated_take_out attrbutes"""
        self.updated_take_out = self.updated_take_out - money
    
    def check(self):
        addition = self.other_savings + self.invest + self.high_vol

        if addition == self.initial_take_out:
            return True
        else:
            return False
    
    def printAll(self):
        print("\nYou should take out £" + str(round(self.initial_take_out)) + " out of your NatWest account")
        print("You should put £" + str(round(self.high_vol)) + " into cryptocurrencies")

        if self.high_vol > 100:
            print("    * Split 4 ways this is £" + str(round(self.high_vol / 4.00)))
            print("    * Split 3 ways this is £" + str(round(self.high_vol / 3.0)))

        print("You should put £" + str(round(self.invest)) + " into low-midrange investments")
        print("This leaves you with £" + str(round(self.left_with)))
        print("    * Split over 4 weeks this is £" + str(round(self.left_with / 4.0)))
        print("    * 10% to put into a holiday pot is £" + str(round(self.left_with * 0.10)))
        print("Left in your NatWest is £" + str(self.left_over))

        if (self.left_with / 4.0) > 45.0:
            print("Overall this was a good financial month, well done!!")
            print("You should consider these things: ")
            print("    * Putting 10% (£" + str(round(self.left_with * 0.10)) + ") into a holiday pot")
            print("    * Reinvesting 20% (£" + str(round(self.left_with * 0.20)) + ") into the NatWest account")
        else:
            print("You'll have a better month ;)")

x = int(input("How much money do you have in your account? "))
obj = finance(x)
obj.printAll()