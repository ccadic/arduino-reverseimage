# arduino-reverseimage
Python Script to reverse an Arduino Coded image into a JPG file.
One common encoding format for 16-bit colors is 5-6-5 RGB, where the first 5 bits represent the red value, the next 6 bits represent the green value, and the last 5 bits represent the blue value.
To convert this data into an actual image using Python, we'll use the PIL module from the Pillow library.

Here's a step-by-step Python script to accomplish this:
Parse the given data into a list.
Decode the 16-bit value into RGB values.
Create a new image using the RGB values.
Save the image in the desired format.

