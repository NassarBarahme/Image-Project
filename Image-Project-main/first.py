import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
from tkinter import Tk, simpledialog

def reduce_image_size(img, scale):
    width = int(img.shape[1] * scale / 100)
    height = int(img.shape[0] * scale / 100)
    return cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

def show_histogram_with_image(image, title):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(image if len(image.shape) == 2 else cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap='gray')
    plt.title(title)
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.hist(image.ravel(), bins=256, range=[0, 256], color='gray')
    plt.title(f"Histogram: {title}")
    plt.xlabel("Intensity")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

path_to_image = r"C:\\Users\\s1221\\OneDrive\\Desktop\\nassar\\New folder\\nassar.jpg"
input_image = cv2.imread(path_to_image)
if input_image is None:
    print(" تعذر العثور على الصورة.")
    exit()

resized_image = reduce_image_size(input_image, 50)
cv2.imshow("Original Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

show_histogram_with_image(gray_image, "Grayscale Image")

equalized_image = cv2.equalizeHist(gray_image)
show_histogram_with_image(equalized_image, "Equalized Image")

c = np.random.uniform(0, 2)
print(f"Value of c: {c}")

scaled = c * gray_image
modified_image = np.clip(scaled, 0, 255).astype(np.uint8)

saturated = (scaled > 255)

s = cv2.cvtColor(modified_image, cv2.COLOR_GRAY2BGR)
s[saturated] = [0, 0, 255]

cv2.imshow("Brightened Image with Saturation Highlight", s)
cv2.waitKey(0)
cv2.destroyAllWindows()

student_id = "12218619"
kernel_vals = [int(num) for num in student_id] + [int(student_id[-1])]
kernel_matrix = np.array(kernel_vals[:9]).reshape((3, 3))
filtered_image = cv2.filter2D(gray_image, -1, kernel_matrix)
cv2.imshow("Filtered Image", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

height, width = gray_image.shape
x_start = random.randint(0, width - 500)
y_start = random.randint(0, height - 500)
mask = np.zeros_like(gray_image, dtype=np.uint8)
mask[y_start:y_start + 500, x_start:x_start + 500] = 255
masked_image = cv2.bitwise_and(gray_image, mask)
cv2.imshow("Masked Image", masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

edges_detected = cv2.Canny(gray_image, 100, 200)
cv2.imshow("Edges Detected", edges_detected)
cv2.waitKey(0)
cv2.destroyAllWindows()

def region_grow(image, seed, threshold):
    visited = np.zeros_like(image, dtype=bool)
    result = np.zeros_like(image, dtype=np.uint8)
    stack = [seed]
    seed_value = image[seed[1], seed[0]]

    while stack:
        x, y = stack.pop()
        if visited[y, x]:
            continue
        visited[y, x] = True

        if abs(int(image[y, x]) - int(seed_value)) <= threshold:
            result[y, x] = 255
            neighbors = [(x + dx, y + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]
                         if 0 <= x + dx < image.shape[1] and 0 <= y + dy < image.shape[0]]
            stack.extend(neighbors)
    return result

def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"نقطة البداية: ({x}, {y})")
        try:
            root = Tk()
            root.withdraw()
            threshold = simpledialog.askinteger("Threshold Input", "أدخل قيمة العتبة:", minvalue=0, maxvalue=255)
            root.destroy()

            if threshold is not None:
                grown_area = region_grow(gray_image, (x, y), threshold)
                cv2.imshow("Region Growing", grown_area)
        except Exception as e:
            print(f"خطأ: {e}")

cv2.imshow("Select Seed Point", gray_image)
cv2.setMouseCallback("Select Seed Point", mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
