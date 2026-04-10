from PIL import Image

class ImageLoader:
    def __init__(self):
        pass
      
    def load_image(self, image_path) -> tuple:
        """
        Load an image from the specified path and extract its dimensions and pixel data.
        
        Args:
            image_path (str): The file path to the image file.
        
        Returns:
            tuple: A tuple containing:
                - img_object (PIL.Image): The PIL Image object.
                - width (int): The width of the image in pixels.
                - height (int): The height of the image in pixels.
                - pixels: PIL Image pixel data object for accessing individual pixels.
        """
        
        img_object = Image.open(image_path)
        width, height = img_object.size
        pixels = img_object.load()
        
        return (img_object, width, height, pixels)

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