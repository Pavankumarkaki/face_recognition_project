import cv2

# mobile_ip="192.168.1.38"
# port="4747"
# url = f"http://{mobile_ip}:{port}/video"
# url=f"http://192.168.1.38:8080/video"
# cp=cv2.VideoCapture(url)
cp=cv2.VideoCapture(0)

if not cp.isOpened():
    print("Error: Could not connect to the mobile camera.")
    exit()

while True:
    ret,frame=cp.read()
    
    if not ret:
        break
    
    # mirror image 
    # mirror_image=cv2.flip(frame,1)
    
    cv2.imshow('camera feed',frame)
    
    if cv2.waitKey(1) == 27:#escape key
        break
    
cp.release()
cv2.destroyAllWindows()