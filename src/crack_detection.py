import cv2
import requests
import numpy as np
from ultralytics import YOLO

print("Loading YOLO model...")
model = YOLO("best.pt")

url = "http://10.229.209.175" 

print(f"Manually pulling stream from: {url}")

stream = requests.get(url, stream=True, timeout=5)

if stream.status_code != 200:
    print(f"❌ ERROR: Server returned status {stream.status_code}")
    exit()

print("✅ Connection established. Processing bytes...")

bytes_data = bytes()
for chunk in stream.iter_content(chunk_size=1024):
    bytes_data += chunk
    
    # Look for the start (0xff 0xd8) and end (0xff 0xd9) of a JPEG frame
    a = bytes_data.find(b'\xff\xd8')
    b = bytes_data.find(b'\xff\xd9')
    
    if a != -1 and b != -1:
        jpg = bytes_data[a:b+2]
        bytes_data = bytes_data[b+2:]
        
        frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)

        if frame is not None:
            results = model(frame, conf=0.5, verbose=False)
            annotated_frame = results[0].plot()

            cv2.imshow("Drone Crack Detection - Manual Stream", annotated_frame)

        if cv2.waitKey(1) == ord('q'):
            break

cv2.destroyAllWindows()