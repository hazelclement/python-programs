import tkinter
import cv2-plt-imshow as cv2
import PIL.Image, PIL.ImageTk

window = tkinter.Tk()

# Load an image using OpenCV
cv_img = cv2.imread("background.jpg")

# Get the image dimensions (OpenCV stores image data as NumPy ndarray)
height, width, no_channels = cv_img.shape

# Run the window loop
window.mainloop()