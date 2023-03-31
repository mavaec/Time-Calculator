def time_calculator(time, duration, day=None) :
	

	result_extra_day = ''
	result_day = ''
	result_time = ''

	

	time = time.strip()
	time_components = time.split()
	time_digits = time_components[0].split(':')
	time_components[1] = time_components[1].lower()
	time_hours = int(time_digits[0])
	time_minutes = int(time_digits[1])
	
	if time_components[1] == 'am' :
		if time_hours == 12 :
			time_hours = 0
	else :
		if time_hours < 12 :
			time_hours += 12

	#print(time_hours, time_minutes)


	duration = duration.strip()
	duration_components = duration.split()
	duration_digits = duration_components[0].split(':')
	duration_hours = int(duration_digits[0])
	duration_minutes = int(duration_digits[1])

	new_time_hours = time_hours + duration_hours
	new_time_minutes = time_minutes + duration_minutes

	#print(new_time_hours, new_time_minutes)

	extra_hours = new_time_minutes // 60
	new_time_minutes = new_time_minutes % 60
	new_time_hours += extra_hours
	extra_days = new_time_hours // 24
	new_time_hours = new_time_hours % 24

	if extra_days == 1 :
		result_extra_day = '(next day)'
	elif extra_days > 1 :
		result_extra_day = '(' + str(extra_days) + ' days after)'


	if day != None :
		week_day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
		day = (day.strip()).lower()
		i = week_day.index(day)
		result_day = ', ' + week_day[(i+extra_days) % len(week_day)].capitalize()

	if new_time_hours > 12 :
		result_time = str(new_time_hours - 12)
	elif new_time_hours == 0 :
		result_time = '12'
	else :
		result_time = str(new_time_hours)

	result_time += ':' + str(new_time_minutes)
	result_time += ' ' + time_components[1].upper()


	print(result_time + result_day, result_extra_day)

	return 0