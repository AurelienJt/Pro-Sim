import math


def calculate_parameters(initial_speed=None, launch_angle=None, initial_vertical_speed=None, time_of_flight=None, max_height=None, range_distance=None, initial_horizontal_speed=None, ):
    g = 9.81 # acceleration due to gravity (m/s^2)
    print(initial_speed, launch_angle, initial_vertical_speed, time_of_flight, max_height, range_distance, initial_horizontal_speed)
    if initial_speed is not None and launch_angle is not None:
        # Given: Initial Speed and Launch Angle
        initial_horizontal_speed = initial_speed * math.cos(math.radians(launch_angle))
        initial_vertical_speed = initial_speed * math.sin(math.radians(launch_angle))
        time_of_flight = (2 * initial_speed * math.sin(math.radians(launch_angle))) / g
        max_height = (initial_vertical_speed**2) / (2 * g)
        range_distance = initial_horizontal_speed * time_of_flight
        
    elif initial_speed is not None and initial_vertical_speed is not None:
        # Given: Initial Speed and Initial Vertical Speed
        launch_angle = math.degrees(math.asin(initial_vertical_speed / initial_speed))
        initial_horizontal_speed = initial_speed * math.cos(math.radians(launch_angle))
        time_of_flight = (2 * initial_vertical_speed) / g
        max_height = (initial_vertical_speed**2) / (2 * g)
        range_distance = initial_horizontal_speed * time_of_flight

    elif initial_speed is not None and time_of_flight is not None:
        # Given: Initial Speed and Time of Flight
        launch_angle = math.degrees(math.asin((g * time_of_flight) / (2 * initial_speed)))
        initial_horizontal_speed = initial_speed * math.cos(math.radians(launch_angle))
        initial_vertical_speed = initial_speed * math.sin(math.radians(launch_angle))
        max_height = (initial_vertical_speed**2) / (2 * g)
        range_distance = initial_horizontal_speed * time_of_flight
        
    elif initial_speed is not None and max_height is not None:
        # Given: Initial Speed and Maximum Height
        initial_vertical_speed = math.sqrt(2 * g * max_height)
        launch_angle = math.degrees(math.asin(initial_vertical_speed / initial_speed))
        initial_horizontal_speed = initial_speed * math.cos(math.radians(launch_angle))
        time_of_flight = (2 * initial_vertical_speed) / g
        range_distance = initial_horizontal_speed * time_of_flight
        
    elif initial_speed is not None and range_distance is not None:
        # Given: Initial Speed and Range
        launch_angle = math.degrees(math.asin((range_distance * g) / (initial_speed ** 2)) / 2)
        initial_horizontal_speed = initial_speed * math.cos(math.radians(launch_angle))
        initial_vertical_speed = initial_speed * math.sin(math.radians(launch_angle))

        time_of_flight = (2 * initial_speed * math.sin(math.radians(launch_angle))) / g
        max_height = (initial_vertical_speed**2) / (2 * g)
    
    elif initial_speed is not None and initial_horizontal_speed is not None:
        # Calculate the launch angle (in degrees)
        launch_angle = math.degrees(math.acos(initial_horizontal_speed / initial_speed))

        # Calculate the initial vertical speed
        initial_vertical_speed = initial_speed * math.sin(math.radians(launch_angle))

        # Calculate time of flight
        g = 9.81  # Acceleration due to gravity (replace with your desired value)
        time_of_flight = (2 * initial_vertical_speed) / g

        # Calculate maximum height
        max_height = (initial_vertical_speed ** 2) / (2 * g)

        # Calculate range distance
        range_distance = initial_horizontal_speed * time_of_flight

    elif launch_angle is not None and initial_vertical_speed is not None:
        # Given: Launch Angle and Initial Vertical Speed
        initial_speed = initial_vertical_speed / math.sin(math.radians(launch_angle))
        initial_horizontal_speed = initial_speed * math.cos(math.radians(launch_angle))
        time_of_flight = (2 * initial_vertical_speed) / g
        max_height = (initial_vertical_speed**2) / (2 * g)
        range_distance = initial_horizontal_speed * time_of_flight
        
    elif launch_angle is not None and time_of_flight is not None:
        # Given: Launch Angle and Time of Flight
        initial_speed = (g * time_of_flight) / (2 * math.sin(math.radians(launch_angle)))
        initial_horizontal_speed = initial_speed * math.cos(math.radians(launch_angle))
        initial_vertical_speed = initial_speed * math.sin(math.radians(launch_angle))
        max_height = (initial_vertical_speed**2) / (2 * g)
        range_distance = initial_horizontal_speed * time_of_flight
        
    elif launch_angle is not None and max_height is not None:
        # Given: Launch Angle and Maximum Height
        initial_vertical_speed = math.sqrt(2 * g * max_height)
        initial_speed = initial_vertical_speed / math.sin(math.radians(launch_angle))
        initial_horizontal_speed = initial_speed * math.cos(math.radians(launch_angle))
        time_of_flight = (2 * initial_vertical_speed) / g
        range_distance = initial_horizontal_speed * time_of_flight
    
    elif launch_angle is not None and range_distance is not None:
        launch_angle_rad = math.radians(launch_angle)
        initial_speed = math.sqrt((range_distance * g) / (2 * math.sin(launch_angle_rad) * math.cos(launch_angle_rad)))
        initial_horizontal_speed = initial_speed*math.cos(math.radians(launch_angle))
        initial_vertical_speed = initial_speed*math.sin(math.radians(launch_angle))
        time_of_flight = (2 * initial_vertical_speed) / g
        range_distance = initial_horizontal_speed * time_of_flight
        max_height = (initial_vertical_speed**2) / (2 * g)
       
    elif launch_angle is not None and initial_horizontal_speed is not None:
        # Convert launch angle from degrees to radians
        launch_angle_radians = math.radians(launch_angle)

        # Calculate the initial vertical speed
        initial_vertical_speed = initial_horizontal_speed * math.tan(launch_angle_radians)

        # Calculate time of flight
        g = 9.81  # Acceleration due to gravity (replace with your desired value)
        time_of_flight = (2 * initial_vertical_speed) / g

        # Calculate maximum height
        max_height = (initial_vertical_speed ** 2) / (2 * g)

        # Calculate range distance
        range_distance = initial_horizontal_speed * time_of_flight
        initial_speed = initial_horizontal_speed/math.cos(math.radians(launch_angle))

    elif max_height is not None and range_distance is not None:
        initial_vertical_speed = math.sqrt(2 * g * max_height)

        # Calculate time of flight
        time_of_flight = (2 * initial_vertical_speed) / g

        # Calculate initial horizontal speed
        initial_horizontal_speed = range_distance / time_of_flight

        # Calculate the launch angle (in degrees)
        launch_angle = math.degrees(math.atan(initial_vertical_speed / initial_horizontal_speed))
        initial_speed = initial_horizontal_speed/math.cos(math.radians(launch_angle))

    elif time_of_flight is not None and range_distance is not None:
        initial_horizontal_speed = range_distance / time_of_flight
        initial_vertical_speed = (g * time_of_flight) / 2
        max_height = (initial_vertical_speed**2) / (2 * g)
        launch_angle = math.degrees(math.atan(initial_vertical_speed / initial_horizontal_speed))
        initial_speed = initial_horizontal_speed/math.cos(math.radians(launch_angle))

    elif initial_horizontal_speed is not None and range_distance is not None:
        time_of_flight = range_distance / initial_horizontal_speed
        initial_vertical_speed = (g * time_of_flight) / 2
        max_height = (initial_vertical_speed**2) / (2 * g)
        launch_angle = math.degrees(math.atan(initial_vertical_speed / initial_horizontal_speed))
        initial_speed = initial_horizontal_speed/math.cos(math.radians(launch_angle))
    
    elif initial_vertical_speed is not None and range_distance is not None:
        time_of_flight = (2 * initial_vertical_speed) / g
        max_height = (initial_vertical_speed ** 2) / (2 * g)
        initial_horizontal_speed = range_distance / time_of_flight
        launch_angle = math.degrees(math.atan(initial_vertical_speed / initial_horizontal_speed))
        initial_speed = initial_horizontal_speed/math.cos(math.radians(launch_angle))

    elif initial_horizontal_speed is not None and initial_vertical_speed is not None:
        launch_angle = math.degrees(math.atan(initial_vertical_speed / initial_horizontal_speed))
        initial_speed = initial_vertical_speed / math.sin(math.radians(launch_angle))
        time_of_flight = (2 * initial_speed * math.sin(math.radians(launch_angle))) / g
        max_height = (initial_vertical_speed**2) / (2 * g)
        range_distance = initial_horizontal_speed * time_of_flight

    return initial_speed, launch_angle, initial_horizontal_speed, initial_vertical_speed, time_of_flight, max_height, range_distance
    print("Launch Angle:", launch_angle, "degrees")
    print("Initial Speed:", initial_speed, "m/s")
    print("Initial Horizontal Speed:", initial_horizontal_speed, "m/s")
    print("Initial Vertical Speed:", initial_vertical_speed, "m/s")
    print("Time of Flight:", time_of_flight, "seconds")
    print("Maximum Height:", max_height, "meters")
    print("Range:", range_distance, "meters")
