import qrcode

image = qrcode.make("https://127.0.0.1:8000")
image.save("C:/Users/satvi/OneDrive/Desktop/python_projects/project-restaurant/qr.png")