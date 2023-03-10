num_ap = int(input('Введіть номер квартири: '))
floor = int(input('Введіть кількість поверхів: '))
ap_fl = int(input('Введіть кількість квартир на поверсі: '))

def num_apartament():
     pid = floor * ap_fl
     if num_ap % pid:
          num_pid = num_ap // pid + 1
     else:
          num_pid = num_ap // pid
     if num_ap % pid:
          num_fl = (num_ap % pid // ap_fl) + 1
     else:
          num_fl = floor
     print(str(num_pid) + ' підїзд')
     print(str(num_fl) + ' поверх')

num_apartament()