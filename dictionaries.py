capital = {'city':"Moscow", 'temperature':"20"}
print(capital['city'])
capital['temperature'] = str(int(capital['temperature']) - 5)
print(capital)
print(capital.get('country', "Russia"))
capital['date'] = '17.05.2020'
print(capital)