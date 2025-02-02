def create_char_mapping():
    # Create mapping for uppercase A-Z (0-25)
    char_map = {chr(65 + i): i for i in range(26)}
    # Add space (27) and apostrophe (28)
    char_map[' '] = 26
    char_map["'"] = 27
    return char_map

def degrees_from_char(char, char_map):
    # Convert character position to degrees (1/18 * 360 = 20 degrees per character)
    return char_map[char] * (360/28)

def encode_string(input_string):
    # Create character to position mapping
    char_map = create_char_mapping()
    # Convert string to uppercase
    input_string = input_string.upper()
    # Convert each character to its degree value
    wedge_angles = []
    for char in input_string:
        if char in char_map:
            angle = degrees_from_char(char, char_map)
            wedge_angles.append(angle)
    return wedge_angles

import math

n = int(input())
for _ in range(n):
    message = input()
    angles = encode_string(message)
    #print(angles)
    distance = 0
    for i in range(len(angles)):
        # Use modulo to wrap around to first angle for the last element
        next_i = (i + 1) % len(angles)
        # calc the minimum arc to next letter
        clockwise = (angles[next_i] - angles[i]) % 360
        counterclockwise = (angles[i] - angles[next_i]) % 360
        min_arc = min(clockwise, counterclockwise)
        #print(f"Angle 1: {angles[i]}, Angle 2: {angles[next_i]}, Min Arc: {min_arc}")
        distance += (min_arc * 2 * math.pi * 30) / 360
        
    time = distance/15 + len(angles)
    print(time)