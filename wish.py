import time
timestamp = time.strftime('%H,%M,%S')
if timestamp < '06,00,00':
    print('Good morning!')
elif timestamp < '12,00,00':
    print('Good afternoon!')
elif timestamp < '18,00,00':
    print('Good evening!')
else:
    print('Good night!')
