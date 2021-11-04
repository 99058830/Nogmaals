# name of student: Jordy van Zomeren
# number of student: 99058830
# purpose of program: Wisselgeld rekenmachine
# function of program: Veranderd geld naar een bepaald wisselgeld
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #Input voor het te betalen bedrag
paid = int(float(input('Paid amount: ')) * 100) #Input voor het al eerder betaalde bedrag
change = paid - toPay #Rekensom om wisselgeld terug te geven
changeList = []

if change > 0: #Checked of er uberhaupt wisselgeld nodig is
  coinValue = 500 #Value moet hoger omdat ik een munt stuk van 5,00 toe moest voegen
  
  while change > 0 and coinValue > 0: #als het groter is dan loop
    nrCoins = change // coinValue #om nrCoins een naam te geven

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #Print om de uitkomst uit te printen
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #Om uit te printen wat je terug krijgt
      changeList.append(str(nrCoins)+' coins of €'+str(format(float(coinValue/100),'.2f')))
      change -= nrCoinsReturned * coinValue #Rekensom voor change

# comment on code below: Als het 5 euro is krijg je 3 euro terug, als je 3 euro hebt krijg je 2 euro terug enz.
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #Als het 0 is kan het niet terug betaald worden, anders moet je printen
  print('Change not returned: ', str(change) + ' cents')
else:
  print('Here is your payout : ')
  x = 0
  for x in range(len(changeList)):
    print(str(changeList[x]))