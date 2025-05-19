import cv2 
image_path = "sample.jpg" 
image = cv2.imread(image_path) if image is None: print("Image not found or path is incorrect.") exit()
hog = cv2.HOGDescriptor() hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
weights (rects, weights) = hog.detectMultiScale(image,winStride=(4, 4), padding=(8, 8), scale=1.05)s 
for i, (x, y, w, h) in enumerate(rects): 
  cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2) label = f"Person {i+1}"
  cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
   count = len(rects) cv2.putText(image, f"Total People Detected: {count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
image cv2.imwrite("crowd_detected.jpg", image)
