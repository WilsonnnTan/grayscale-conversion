from PIL import Image
import copy

class ImageLoader:
    def __init__(self):
        pass
      
    def load_image(self, image_path):
        """
        Load an image from the specified file path.
        
        Args:
            image_path (str): The file path to the image file.
        
        Returns:
            img_object (PIL.Image): The PIL Image object.
        """
        
        img_object = Image.open(image_path)
        
        return img_object

    def save_image(self, img_object, image_save_path) -> None:
        """
        Save an image to the specified file path.
        
        Args:
            img_object (PIL.Image): The PIL Image object to save.
            image_save_path (str): The file path where the image will be saved.
        
        Returns:
            None
        """
        
        img_object.save(image_save_path)
        

class GrayscaleAlgorithm:
    def __init__(self, img_object):
        """
        Initialize the GrayscaleAlgorithm with an image object.
        
        Args:
            img_object (PIL.Image): The PIL Image object to convert.
        """
        self.img_object = img_object
        
    def _image_deep_copy(self):
        """
        Create a deep copy of the image object and extract its properties.
        
        This is a private helper method that creates an independent copy of the
        original image to avoid modifying the source image when applying filters.
        
        Returns:
            tuple: A tuple containing:
                - img_object_copy (PIL.Image): A deep copy of the image.
                - width (int): The width of the image in pixels.
                - height (int): The height of the image in pixels.
                - pixels: PIL Image pixel data object for the copied image.
        """
        img_object_copy = copy.deepcopy(self.img_object)
        width, height = img_object_copy.size
        pixels = img_object_copy.load()
        
        return (img_object_copy, width, height, pixels)
    
    def averaging(self):
        """
        Convert image to grayscale using the simple averaging method.
        
        This method creates a copy of the image and calculates the average
        of RGB values for each pixel, assigning the same gray value to all
        three channels while preserving the alpha channel.
        
        Returns:
            img_object_copy (PIL.Image): A new grayscale image object.
        """
        
        img_object_copy, width, height, pixels = self._image_deep_copy()
        
        for i in range(height):
            for j in range(width):
                r, g, b, a = pixels[j, i]
                gray = int((r + g + b) / 3)
                pixels[j, i] = (gray, gray, gray, a)
        
        return img_object_copy
    
    def luma(self):
        """
        Convert image to grayscale using the ITU-R BT.709 recommendation (luma weightings).
        
        This method creates a copy of the image and applies human perception-based
        color weights (red: 0.2126, green: 0.7152, blue: 0.0722) to produce a more
        accurate grayscale representation compared to simple averaging.
        
        Returns:
            img_object_copy (PIL.Image): A new grayscale image object.
        """
        
        img_object_copy, width, height, pixels = self._image_deep_copy()
        
        for i in range(height):
            for j in range(width):
                r, g, b, a = pixels[j, i]
                gray = int(r * 0.2126 + g * 0.7152 + b * 0.0722)
                pixels[j, i] = (gray, gray, gray, a)
        
        return img_object_copy
    
    def desaturation(self):
        """
        Convert image to grayscale using the desaturation method.
        
        This method creates a copy of the image and calculates the grayscale value
        as the average of the maximum and minimum RGB values. This method is useful
        for preserving highlights and shadows in the image.
        
        Returns:
            img_object_copy (PIL.Image): A new grayscale image object.
        """
        
        img_object_copy, width, height, pixels = self._image_deep_copy()
        
        for i in range(height):
            for j in range(width):
                r, g, b, a = pixels[j, i]
                gray = int((max(r, g, b) + min(r, g, b)) / 2)
                pixels[j, i] = (gray, gray, gray, a)
        
        return img_object_copy