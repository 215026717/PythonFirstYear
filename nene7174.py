# Author: Mongezi Nene
# This program input an amount in cents and
# outputs the number of rands and cent pieces that amount consists of


#INPUT the amount in cents
cents = input("Enter cents here : ")
cents = int(cents)
rands = cents // 100#calculate rands
rem_tens_digits = cents - rands * 100#calculate the cents that remain after subtracting the rands
fifty_cents = (rem_tens_digits) // 50#calculate 50 cent pieces
rem_tens_digits1 = rem_tens_digits - fifty_cents * 50#calculate remaining cents after subtracting the 50 cent pieces
twenty_cents = (rem_tens_digits1) // 20#calculate 20 cent pieces
rem_tens_digits2 = rem_tens_digits1 - twenty_cents * 20#calculate remaining cents after subtracting the 20 cent pieces
ten_cents = (rem_tens_digits2) // 10#calculate 10 cent pieces
rem_units_digits = rem_tens_digits - rem_tens_digits // 10 * 10#calculate the remaining cents after subtracting the 10 cent pieces (now the units digits of the amount)
five_cents = rem_units_digits // 5#calculate the 5 cent pieces
rem_units_digits1 = rem_units_digits - five_cents * 5#calculate the remaining cents after subtracting the 5 cent pieces
one_cents = rem_units_digits1 // 1#calculate the 1 cent pieces

#output the rands and cents pieces
print(cents, "cents has")
print(rands, "rands          ", "\t", fifty_cents, "50 cent pieces")
print(twenty_cents, "20 cent pieces", "\t", ten_cents, "10 cent pieces")
print(five_cents, "5 cent pieces", "\t", one_cents, "1 cent pieces")
