import pygame
import time
from djitellopy import Tello

# Initialize pygame
pygame.init()

# Set up the controller
controller = pygame.joystick.Joystick(0)
controller.init()

# Set up the Tello drone
tello = Tello()

# Connect to the Tello drone
tello.connect()

# Enable video streaming
tello.streamon()

# Function to map controller inputs to Tello commands
def map_controller_inputs():
    pygame.event.pump()

    # Get controller axes values
    left_stick_x = controller.get_axis(0)
    left_stick_y = controller.get_axis(1)
    right_stick_x = controller.get_axis(2)
    right_stick_y = controller.get_axis(3)

    # Get controller button states
    x_button = controller.get_button(0)  # X button
    triangle_button = controller.get_button(2)  # Triangle button
    circle_button = controller.get_button(1)  # Circle button
    square_button = controller.get_button(3)  # Square button

    # Map controller inputs to Tello commands
    forward_backward = int(left_stick_y * 100)
    left_right = int(left_stick_x * 100)
    up_down = int(right_stick_y * 100)
    yaw = int(right_stick_x * 100)

    # Adjust the speed of the Tello drone
    speed = 30

    # Check controller button states and send the corresponding Tello commands
    if x_button == 1:
        tello.takeoff()
    elif triangle_button == 1:
        tello.land()
    elif circle_button == 1:
        tello.emergency()
    elif square_button == 1:
        tello.flip_back()

    # Send the mapped commands to the Tello drone
    tello.send_rc_control(left_right, forward_backward, up_down, yaw)
    time.sleep(0.05)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Map controller inputs to Tello commands
    map_controller_inputs()

# Disconnect from the Tello drone
tello.streamoff()
tello.disconnect()

# Quit pygame
pygame.quit()