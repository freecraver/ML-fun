# size of bigger image axis (height or width) - used for auto scaling mode, default=200
TARGET_SIZE = 100
# use the provided resize and crop functionality instead of auto scaling, default=True
USE_CROPPING_CAR = True
# use the provided resize and crop functionality instead of auto scaling, default=False
USE_CROPPING_FRUIT = False

# fixed height for car images, if None auto scaling mode is used, default=40
TARGET_HEIGHT_CAR = 40
# fixed width for car images, if None auto scaling mode is used, default=100
TARGET_WIDTH_CAR = 100
# fixed height for fruit images, if None auto scaling mode is used, default=None
TARGET_HEIGHT_FRUIT = None
# fixed width for fruit images, if None auto scaling mode is used, default=None
TARGET_WIDTH_FRUIT = None

# used kernel for convolution layers, default=5
KERNEL_SIZE_CAR = 5
# used kernel for convolution layers, default=5
KERNEL_SIZE_FRUIT = 5

# number of epochs used for training, default=15
EPOCHS_CAR = 15
EPOCHS_FRUIT = 15

# use grayscale images instead of rgb images, default=False
FRUIT_USE_GRAYSCALE=False