import cv2

f = cv2.imread("flag.png")
l = cv2.imread("lemur.png")

res = cv2.bitwise_xor(f, l)

cv2.imshow("res", res)
cv2.waitKey()
cv2.destroyAllWindows()
