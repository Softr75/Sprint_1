time_values = '1h 45m,360s,25m,30m 120s,2h 60s'
parts = time_values.split(',')
for i in range(len(parts)):
    parts[i] = parts[i].replace(' ', '')

total_minutes = 0

for part in parts:
    tokens = part.replace('h', 'h ').replace('m', 'm ').replace('s', 's ').split()

    for token in tokens:
        value = int(token[:-1])
        unit = token[-1]
        if unit == 'h':
            total_minutes += value * 60
        elif unit == 's':
            total_minutes += value / 60
        else:
            total_minutes += value

print(int(total_minutes))