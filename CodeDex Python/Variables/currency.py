#Currency program that checks value of currency left over in USD

yuan = int(input('What do you have left in yuan? '))
currentYuanRate = .15
yen = int(input('What do you have left in yen? '))
currentYenRate = .0076
won = int(input('What do you have left in won? '))
currentWonRate = .00080

usd = (yuan * currentYuanRate) + (yen * currentYenRate) + (won * currentWonRate)

print(usd)