import matplotlib.pyplot as plt
import numpy as np
import cv2

# Load the image
img = '10'
file = '/N1kor4/TIPE_PC/pictures/' + str(img) + '.jpg'
Original = cv2.imread(file)

# Grayscale and Contrast Adjustment Function
def NoirBlanc(Image, teinte):
    """Convert an image to grayscale with binary thresholding based on a specified shade.

    Parameters:
    Image : array
        The input color image as an array.
    teinte : int
        The grayscale threshold. Pixels darker than this value are set to black.

    Returns:
    array
        The transformed grayscale image.
    """
    Image_gray = []
    for row in Image:
        new_row = []
        for pixel in row:
            grayscale_value = pixel[0] * 0.2125 + pixel[1] * 0.7174 + pixel[2] * 0.0721
            if grayscale_value < teinte:
                grayscale_value = 0
            new_row.append(grayscale_value)
        Image_gray.append(new_row)
    return np.array(Image_gray, dtype=np.uint8)


# Edge Detection Function
def Contour(Image):
    """Detect edges by scanning the image columns for transitions from black to non-black.

    Parameters:
    Image : array
        The input grayscale image.

    Returns:
    array
        The image with detected edges.
    """
    edges = np.full_like(Image, 255)
    for i in range(3, len(Image[0])):  # Avoid out-of-bounds with offset of 3
        for j in range(len(Image)):
            if Image[j - 3][i] == 0 and Image[j][i] > 0:
                edges[j][i] = 0
    return edges


# Extract Curve Coordinates
def Courbe(Image):
    """Extract the coordinates of the first black pixel in each column, simulating the shape of the curve.

    Parameters:
    Image : array
        The input edge-detected image.

    Returns:
    list, list
        X and Y coordinates of the curve.
    """
    Image_rotated = np.flipud(Image.T)  # Rotate matrix 90 degrees
    X, Y = [], []
    for col_idx, col in enumerate(Image_rotated):
        black_pixels = [row_idx for row_idx, value in enumerate(col) if value == 0]
        if black_pixels:
            X.append(col_idx)
            Y.append(black_pixels[0])
    return X, Y


# Calculate Angle of Intersection Between Two Linear Fits
def coeff_angle1(X, Y):
    """Find the intersection point and angles of two linear segments on the curve.

    Parameters:
    X : list
        X coordinates of the curve.
    Y : list
        Y coordinates of the curve.

    Returns:
    list, list, float, float
        Linear fits (Y values) and intersection coordinates (x0, y0).
    """
    nb = 90
    [a1, b1] = np.polyfit(X[:nb], Y[:nb], 1)
    Y_reg1 = a1 * np.array(X) + b1

    nb2 = nb
    nb3 = nb2 + 10
    [a2, b2] = np.polyfit(X[nb2:nb3], Y[nb2:nb3], 1)
    Y_reg2 = a2 * np.array(X) + b2

    x0 = (b2 - b1) / (a1 - a2)
    y0 = a1 * x0 + b1
    return Y_reg1, Y_reg2, x0, y0


# Display Curve and Regression Lines
def courbe(Image):
    """Plot the curve with linear regressions and intersection point.

    Parameters:
    Image : array
        Input image for curve plotting.
    """
    X, Y = Courbe(Contour(NoirBlanc(Image, teinte)))
    Y_reg1, Y_reg2, x0, y0 = coeff_angle1(X, Y)
    plt.figure()
    plt.grid()
    plt.plot(X, Y, label='Curve')
    plt.plot(X, Y_reg1, 'k', label='Fit 1')
    plt.plot(X, Y_reg2, 'r', label='Fit 2')
    plt.scatter(x0, y0, color='g', label='Intersection')
    plt.ylim([400, 0])
    plt.legend()
    plt.show()


# Calculate Intersection Angle
def Angle(Image):
    """Calculate the angle at the intersection point of the two regression lines.

    Parameters:
    Image : array
        The input image.

    Returns:
    float
        The intersection angle in degrees.
    """
    position = 100
    X, Y = Courbe(Contour(NoirBlanc(Image, teinte)))
    Y_reg1, Y_reg2, x0, y0 = coeff_angle1(X, Y)
    num = Y_reg1[position] - x0
    den = np.sqrt((Y_reg1[position] - x0)**2 + (Y_reg2[position] - y0)**2)
    theta = np.arccos(num / den)
    if Y_reg2[position] - y0 < 0:
        theta = 2 * np.pi - theta
    theta = abs(np.degrees(theta) - 180)
    return theta


# Display Original and Resized Image
plt.imshow(Original)

# Resize Parameters
Taille = 400
CoordX, CoordY = 1860, 1200
Original_resized = Original[CoordY:CoordY + Taille // 2, CoordX:CoordX + Taille]
plt.imshow(Original_resized)

# Define Teinte Threshold and Process Image
teinte = 50
plt.imshow(NoirBlanc(Original_resized, teinte), cmap='gray', vmin=0, vmax=255)
plt.imshow(Contour(NoirBlanc(Original_resized, teinte)), cmap="gray")

X, Y = Courbe(Contour(NoirBlanc(Original_resized, teinte)))
plt.figure()
plt.grid()
plt.plot(X, Y)
courbe(Original_resized)

# Calculate and Print Angle
angle = Angle(Original_resized)
print("L'angle est de", round(angle, 0), '°')
