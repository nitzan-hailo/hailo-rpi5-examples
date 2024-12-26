import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib
import os
import numpy as np
import cv2
import hailo
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt


from hailo_apps_infra.hailo_rpi_common import (
    get_caps_from_pad,
    get_numpy_from_buffer,
    app_callback_class,
)
from hailo_apps_infra.depth_estimation_pipeline import GStreamerDepthEstimationApp


def generate_topographic_map(depth_data):
    """
    Maps depth data to a color topographic map.
    """
    # Convert to grayscale if needed
    if depth_data.shape[-1] == 3:
        depth_data = cv2.cvtColor(depth_data, cv2.COLOR_BGR2GRAY)

    print(depth_data.shape)

    # Normalize depth data
    normalized_depth = cv2.normalize(depth_data, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
 
    # Updated color bands
    color_bands = [0, 51, 102, 153, 204, 256]
    colors = [
        (128, 0, 0),      # Dark red
        (255, 165, 0),    # Orange
        (0, 128, 255),    # Light blue
        (0, 255, 0),      # Green
        (255, 255, 0)     # Yellow
    ]
 
    # Initialize the color map
    color_map = np.zeros((depth_data.shape[0], depth_data.shape[1], 3), dtype=np.uint8)
 
    # Apply colors based on depth ranges
    for i in range(len(color_bands) - 1):
        mask = (normalized_depth >= color_bands[i]) & (normalized_depth < color_bands[i + 1])
        color_map[mask] = np.array(colors[i], dtype=np.uint8)
    return color_map

 
def draw_contours(depth_data, map_image):
    """
    Draws contour lines on the topographic map.
    """
    # Ensure depth_data is grayscale
    if depth_data.shape[-1] == 3:
        depth_data = cv2.cvtColor(depth_data, cv2.COLOR_BGR2GRAY)
 
    # Normalize depth_data to the range [0, 255] if not already
    normalized_depth = cv2.normalize(depth_data, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
 
    # Define the color bands (ensure these are accessible in the function)
    color_bands = [0, 51, 102, 153, 204, 256]
 
    # Draw contours for each threshold
    for threshold in color_bands:
        _, binary_mask = cv2.threshold(normalized_depth, threshold, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(map_image, contours, -1, (0, 0, 0), 1)  # Black contour lines
 
    return map_image

# -----------------------------------------------------------------------------------------------
# User-defined class to be used in the callback function
# -----------------------------------------------------------------------------------------------
# Inheritance from the app_callback_class
class user_app_callback_class(app_callback_class):
    def __init__(self):
        super().__init__()
        self.use_frame = True  

    def new_function(self):  # New function example
        return "The meaning of life is: "

# -----------------------------------------------------------------------------------------------
# User-defined callback function
# -----------------------------------------------------------------------------------------------

# This is the callback function that will be called when data is available from the pipeline
def app_callback(pad, info, user_data):
    # Get the GstBuffer from the probe info
    buffer = info.get_buffer()
    # Check if the buffer is valid
    if buffer is None:
        return Gst.PadProbeReturn.OK
    # Using the user_data to count the number of frames
    user_data.increment()

    # Get the caps from the pad
    format, width, height = get_caps_from_pad(pad)

    # If the user_data.use_frame is set to True, we can get the video frame from the buffer
        # Get video frame
 #   import ipdb
 #   ipdb.set_trace()
    frame = get_numpy_from_buffer(buffer, format, width, height)
#    print(frame)
    user_data.set_frame( generate_topographic_map(frame*10))
 #   user_data.set_frame(generate_topographic_map(frame*10))
    
    return Gst.PadProbeReturn.OK

if __name__ == "__main__":
    # Create an instance of the user app callback class
    user_data = user_app_callback_class()
    app = GStreamerDepthEstimationApp(app_callback, user_data)
    app.run()

