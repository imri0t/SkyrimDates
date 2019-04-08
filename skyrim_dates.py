'''
    script for showing current dates as a lore based dates in Skyrim
    including lore-friendly holiday dates
    more to come later (possibly a lore library)
'''
#source by im.ri0t

from datetime import date, datetime
import os

from termcolor import colored, cprint
try:
    import colorama
    colorama.init()
except ImportError:
    pass

def main():
    '''dates and holidays'''

    days = [
        'placeholder', #this one takes the 0 spot which is never accessed
        'Mondas',
        'Tirdas',
        'Middas',
        'Turdas',
        'Fredas',
        'Loredas',
        'Sundas'
        ]

    months = [
        'placeholder', #this one takes the 0 spot which is never accessed
        'Morning Star',
        'Sun\'s Dawn',
        'First Seed',
        'Rain\'s Hand',
        'Second Seed',
        'Midyear',
        'Sun\'s Height',
        'Last Seed',
        'Hearthfire',
        'Frostfall',
        'Sun\'s Dusk',
        'Evening Star'
        ]

    today = datetime.now()
    weekday = date.weekday(today)
    day = today.day
    month = today.month
    print('the date is', day, 'of', months[month])
    print('of the week it is', days[weekday])

    if day == '1' and month == 'Morning Star':
        print('today is the New Life Festival!')
    elif day == '15' and month == 'Morning Star':
        print('today is South Wind\'s Prayer!')
    elif day == '16'and month == 'Morning Star':
        print('today is the Festival of Lights!')
    elif day == '13' and month == 'Sun\'s Dawn':
        print('today is the Feast of the Dead!')
    elif day == '16' and month == 'Sun\'s Dawn':
        print('today is Hearts Day!')
    elif day == ' 7' and month == 'Second Seed':
        print('today is the First Planting!')
    elif day == '28' and month == 'Rain\'s Hand':
        print('today is Jester\'s Day!')
    elif day == '2' and month == 'Second Seed':
        print('today is the Second Planting!')
    elif day == '16' and month == 'Midyear':
        print('todat is the Mid Year Celebration!')
    elif day == '10' and month == 'Sun\'s Height':
        print('today is the Merchant\'s Festival')
    elif day == '20' and month == 'Sun\'s Height':
        print('today is  Sun\'s Rest!')
    elif day == '27' and month == 'Last Seed':
        print('today is Harvest\'s End!')
    elif day == '3' and month == 'Hearthfire':
        print('today is Tales and Tallows!')
    elif day == '13' and month == 'Frostfall':
        print('today is the Witches Festival!')
    elif day == '20' and month == 'Sun\'s Dusk':
        print('today is the Warriors\' Festival!')
    elif day == '15' and month == 'Evening Star':
        print('today is North Wind\'s Prayer!')
    elif day == '25' and month == 'Evening Star':
        print('today is Saturalia!')
    elif day == '31' and month == 'Evening Star':
        print('today is the Old Life Festival!')
    else:
        print('no holidays today')


    sstone = 'it is the month of'

    if months[month] == 'Morning Star':
        print(sstone, 'The Ritual')
    if months[month] == 'Sun\'s Dawn':
        print(sstone, 'The Lover')
    elif months[month] == 'First Seed':
        print(sstone, 'The Lord')
    elif months[month] == 'Rain\'s Hand':
        print(sstone, 'The Mage')
    elif months[month] == 'Second Seed':
        print(sstone, 'The Shadow')
    elif months[month] == 'Midyear':
        print(sstone, 'The Steed Ritual')
    elif months[month] == 'Sun\'s Height':
        print(sstone, 'The Apprentice')
    elif months[month] == 'Last Seed':
        print(sstone, 'The Warrior')
    elif months[month] == 'Hearthfire':
        print(sstone, 'The Lady')
    elif months[month] == 'Frostfall':
        print(sstone, 'The Tower')
    elif months[month] == 'Sun\'s Dusk':
        print(sstone, 'The Atronach')
    elif months[month] == 'Evening Star':
        print(sstone, 'The Thief')
    else:
        print('there\'s been an error')

    input()
    exit(0)

if __name__ == '__main__':
    main()
