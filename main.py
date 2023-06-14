# QAP-127, 17.7.3

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму будущего депозита: "))

deposit = [round(money*(1+per_cent['ТКБ']/100), 2)]
deposit.append(round(money*(1+per_cent['СКБ']/100), 2))
deposit.append(round(money*(1+per_cent['ВТБ']/100), 2))
deposit.append(round(money*(1+per_cent['СБЕР']/100), 2))

deposit.sort(reverse=True)

print("Максимальная сумма, которую вы можете заработать -- " + str(deposit[0]))
