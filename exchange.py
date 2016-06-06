from Tkinter import *
import os
import subprocess


def calculate_inr():

#currency to bitcoins
    currency = e2.get()
    value = e1.get()


    btc_str = subprocess.check_output("curl \"https://blockchain.info/tobtc?currency=%(currency)s&value=%(value)s\" -s" %locals(), shell=True)
    btc = float(btc_str)
    Label(master, text="BTC").grid(row=2)
    e3.grid(row=2, column=1)
    e3.insert(10,btc)


# 1 bitcoin = ? INR

    btc_inr_rate = subprocess.check_output("curl \"https://api.btcxindia.com/ticker_hour/\" -s | jq '.last_traded_price'",shell=True)
    Label(master, text="BTC-INR RATE").grid(row=3)
    e4.grid(row=3, column=1)
    e4.insert(10,btc_inr_rate.strip())


# Bitcoins to INR
    btc_inr_rate = int(btc_inr_rate)
    total_inr = btc * btc_inr_rate
    Label(master, text="INR").grid(row=4)
    e5.grid(row=4, column=1)
    e5.insert(10,total_inr)

master = Tk()
Label(master, text="Value").grid(row=0)
Label(master, text="Currency").grid(row=0 , column=3)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)


e1.grid(row=0, column=1)
e2.grid(row=0, column=4)

e1.insert(10, "500")
e2.insert(10,"USD")

Button(master, text='Quit', command=master.quit).grid(row=5, column=0, sticky=W, pady=4)
Button(master, text='Convert', command=calculate_inr).grid(row=5, column=1, sticky=W, pady=4)

mainloop( )
