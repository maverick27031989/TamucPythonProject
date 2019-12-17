from Car import Car

f = open("FuelEffic.txt", "r")
log_file = open("LogFuel.txt", "w")
line1 = f.readline()
line2 = f.readline()
f.close()
if line1.__contains__(':') & line2.__contains__(':'):
    car_efficiency = int(line1.split(':')[1].strip())
    tank_size = int(line2.split(':')[1].strip())
    car = Car(car_efficiency)
    print('\n'+line1+line2)
    while 1:
        print('\nWhat would you like to do: \n\n'
                '1. See Current Fuel Level\n'
                '2. Drive\n'
                '3. Add Gas\n'
                '4. Exit\n')
        user_input = int(input('Please make a selection: '))
        if user_input == 1:
            log_file.write('User Input: 1 - See Current Fuel Level\n')
            fuel_level = str(car.get_gas_level())
            print('Current Fuel Level (in gallon) '+fuel_level)
            log_file.write('Fuel level shown: '+fuel_level+' gallons\n')
        elif user_input == 2:
            log_file.write('User Input: 2 - Drive\n')
            miles_to_drive = int(input('How many miles to drive: '))
            is_car_drove = car.drive(miles_to_drive)
            if is_car_drove:
                print('You drove '+str(miles_to_drive)+' miles.You can drive another '+str(car.max_miles)+' miles on this gas')
                log_file.write('Miles to drive: '+str(miles_to_drive)+'\n')
            else:
                print('You can drive only '+str(car.max_miles)+' miles. Please add gas first.')
                log_file.write('Fuel not sufficient to drive'+str(miles_to_drive)+' miles\n')
        elif user_input == 3:
            log_file.write('User Input: 3 - Add Gas\n')
            gas_to_add = int(input('How much gas to add: '))
            log_file.write('Gas to add - ' + str(gas_to_add) + ' gallons\n')
            max_gas_can_be_added = tank_size - car.get_gas_level()
            if max_gas_can_be_added == 0:
                log_file.write('Tank already full. No more gas added\n')
                print('Tank already full. Gas can not be added')
            elif gas_to_add < max_gas_can_be_added:
                car.add_gas(gas_to_add)
                log_file.write('Total gas added - '+str(gas_to_add)+' gallons\n')
                print('Total gas added (in gallon): '+str(gas_to_add))
            else:
                car.add_gas(max_gas_can_be_added)
                log_file.write('Tank full. Total gas added - ' + str(max_gas_can_be_added) + ' gallons\n')
                print('Tank full. Total gas added (in gallon): '+str(max_gas_can_be_added))
        elif user_input == 4:
            log_file.write('User Input: 4 - Exit\n')
            print('Thank you. Have a good day')
            exit()
        else:
            print('Invalid selection made.')






