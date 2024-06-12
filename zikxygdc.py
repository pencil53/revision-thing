import cv2

image1 = cv2.imread("input2.png")
font = cv2.FONT_HERSHEY_DUPLEX
origin = (90,50)
fontscale = 1
color = (64, 52, 235)
thickness = 4

image1 = cv2.putText(image1 , "Congratulations", origin, font, fontscale, color, thickness)

startpoint = (90,60)
endpoint = (350,60)
color1 = (235, 52, 52)
thickness1 = 3

image1 = cv2.line(image1, startpoint, endpoint, color1, thickness1)

startpoint1 = (85,25)
endpoint1 = (350,80)
color2 = (59, 237, 119)
thickness2 = 3




image1 = cv2.rectangle(image1, startpoint1, endpoint1, color2, thickness2)

cv2.imshow("greetings", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()