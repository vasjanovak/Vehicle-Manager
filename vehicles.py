class Vehicle:
	def __init__(self, make, model, mileage, service):
		self.make = make
		self.model = model
		self.mileage = mileage
		self.service = service


def list_of_vehicles(vehicles):
	if not vehicles:
		print('')
		print("You don't have any vehicles on your list")
		print('')
	else:
		for index, vehicle in enumerate(vehicles):
			print('')
			print('Id: {}'.format(index))
			print('Make: {}'.format(vehicle.make))
			print('Model: {}'.format(vehicle.model))
			print('Mileage: {}'.format(vehicle.mileage))
			print('Last service: {}'.format(vehicle.service))
			print('')


def edit_mileage(vehicles):
	for index, vehicle in enumerate(vehicles):
		print('')
		print('Id: {}'.format(index))
		print('Make: {}'.format(vehicle.make))
		print('Model: {}'.format(vehicle.model))
		print('Mileage: {}'.format(vehicle.mileage))
		print('')

	selected_id = input('Please select vehicle Id:')
	selected_vehicle = vehicles[selected_id]
	new_milage = input('Enter new mileage for {}:'.format(selected_vehicle.make + ' ' + selected_vehicle.model))
	selected_vehicle.mileage = new_milage
	print('Mileage for {} {} was secesfully changed.'.format(selected_vehicle.make, selected_vehicle.model))
	print('')


def edit_date_of_service(vehicles):
	for index, vehicle in enumerate(vehicles):
		print('')
		print('Id: {}'.format(index))
		print('Make: {}'.format(vehicle.make))
		print('Model: {}'.format(vehicle.model))
		print('Last service: {}'.format(vehicle.service))
		print('')

	selected_id = input('Please select vehicle Id:')
	selected_vehicle = vehicles[selected_id]
	new_service_date = input('Enter new date of service for {}:'.format(selected_vehicle.make + ' ' + selected_vehicle.model))
	selected_vehicle.service = new_service_date
	print('Date of service for {} {} was secesfully changed.'.format(selected_vehicle.make, selected_vehicle.model))
	print('')


def add_vehicle(vehicles):
	print('Please enter information about new vehicle')
	new_make = input('Enter make of car: ')
	new_model = input('Enter a model of {}: '.format(new_make))
	new_mileage = input('Enter current mileage of {} {}: '.format(new_make, new_model))
	new_service = input('Enter date of service for {} {}'.format(new_make, new_model))

	new_car = Vehicle(make=new_make, model=new_model, mileage=new_mileage, service=new_service)
	vehicles.append(new_car)

	print('You succesfully entered {} {} on your list.'.format(new_make, new_model))
	print('')


def delete_vehicle(vehicles):
	for index, vehicle in enumerate(vehicles):
		print('')
		print('Id: {}'.format(index))
		print('Make: {}'.format(vehicle.make))
		print('Model: {}'.format(vehicle.model))
		print('')

	selected_id = int(input('Please select vehicle Id:'))
	selected_vehicle = vehicles[selected_id]
	vehicles.remove(selected_vehicle)

	print('')
	print('{} {} was successfully removed'.format(selected_vehicle.make, selected_vehicle.model))


def save_to_file(vehicles):
	with open('vehicles.txt', 'w+') as vehicle_file:
		for index, vehicle in enumerate(vehicles):
			vehicle_file.write('Id: {}\n'.format(index))
			vehicle_file.write('Make: {}\n'.format(vehicle.make))
			vehicle_file.write('Model: {}\n'.format(vehicle.model))
			vehicle_file.write('Mileage: {}\n'.format(vehicle.mileage))
			vehicle_file.write('Service: {}\n'.format(vehicle.service))
			vehicle_file.write('\n')


def main():

	vehicles = []

	while True:
		print('What would you like to do?')
		print('1. List of all vehicles.')
		print('2. Edit mileage for vehicle.')
		print('3. Edit date of last service.')
		print('4. Add new vehicle.')
		print('5. Delete vehicle.')
		print('6. Save and quit.')
		selected = int(input('Pick a number of the task:'))

		if selected == 1:
			list_of_vehicles(vehicles)
		elif selected == 2:
			edit_mileage(vehicles)
		elif selected == 3:
			edit_date_of_service(vehicles)
		elif selected == 4:
			add_vehicle(vehicles)
		elif selected == 5:
			delete_vehicle(vehicles)
		elif selected == 6:
			save_to_file(vehicles)
			print('')
			print('Thank you for using out program.')
			print('Hvae a nice day.')
			print('Bye')
			break
		else:
			print('Please enter number of task you want to make!')


if __name__ == '__main__':
	main()
