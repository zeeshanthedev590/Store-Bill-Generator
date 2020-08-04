import time
sum = 0
while True:
    user = input('Enter The Price :')
    if user!='q':
        sum = sum + int(user)

    if user=='q':
        print('Thanks For Coming To Zk Store')
        print(f'Your Bill Is : {sum}')
        time.sleep(5)
        exit()