#!/usr/bin/env python3
#Small program to display precious metal future prices on polybar. Written by Zeb.


#Import stuff and set roundBy number to keep decimals in check.
from yahoo_fin import stock_info as si
import argparse
roundBy = 1

metals = ['SI=F', 'GC=F', 'PL=F', 'PA=F', 'HG=F']
prices = []
for i in range(len(metals)):
    prices.insert(i, str(round(si.get_live_price(metals[i]), roundBy)))

def displayArgs():
    #Args to display
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", '--silver', help='display the price of silver (in troy ounces).', action="store_true")
    parser.add_argument("-g", '--gold', help='display the price of gold (in troy ounces).', action="store_true")
    parser.add_argument("-p", '--platinum', help='display the price of platinum (in troy ounces).', action="store_true")
    parser.add_argument("-a", '--palladium', help='display the price of palladium (in troy ounces).', action="store_true")
    parser.add_argument("-c", '--copper', help='display the price of copper (in pounds).', action="store_true")
    args = parser.parse_args()
    metal = ""
    
    #Parse the args
    if args.silver:
        metal += "Ag: $" + prices[0] + "/oz | "
    if args.gold:
        metal += "Au: $" + prices[1] + "/oz | "
    if args.platinum:
        metal += "Pt: $" + prices[2] + "/oz | "
    if args.palladium:
        metal += "Pd: $" + prices[3] + "/oz | "
    if args.copper:
        metal += "Cu: $" + prices[4] + "/lb | "
        
    #Display the args (if they exist)
    if metal == "":
        print("No metal chosen to display! Use --help to know more!")
    else:
        print(metal)

if __name__ == '__main__':
    displayArgs()

