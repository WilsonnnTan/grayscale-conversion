import os
from helper import ImageLoader, GrayscaleAlgorithm

def get_input(prompt, default=None):
    if default:
        user_input = input(f"{prompt} [{default}]: ").strip()
        return user_input if user_input else default
    return input(f"{prompt}: ").strip()

def main():
    image_loader = ImageLoader()
    print("=== Grayscale Conversion CLI ===")
    
    while True:
        image_path = get_input("\nEnter the path to your image (or 'exit' to quit)")
        
        if image_path.lower() == 'exit':
            print("Goodbye!")
            break
            
        if not os.path.exists(image_path):
            print(f"Error: File '{image_path}' not found.")
            continue
            
        try:
            img_object = image_loader.load_image(image_path)
            print(f"Successfully loaded '{image_path}' ({img_object.width}x{img_object.height})")
        except Exception as e:
            print(f"Error loading image: {e}")
            continue

        algorithm_manager = GrayscaleAlgorithm(img_object)
        
        while True:
            print("\nSelect an algorithm:")
            print("1. Averaging")
            print("2. Luma")
            print("3. Desaturation")
            print("4. Decomposition (Max/Min)")
            print("5. Single Color Channel (R/G/B)")
            print("6. Custom Gray Shades (Posterization)")
            print("7. Change Image Path")
            print("8. Exit")
            
            choice = get_input("Choice")
            
            if choice == '7':
                break
            if choice == '8':
                print("Goodbye!")
                return
                
            processed_img = None
            try:
                if choice == '1':
                    processed_img = algorithm_manager.averaging()
                elif choice == '2':
                    processed_img = algorithm_manager.luma()
                elif choice == '3':
                    processed_img = algorithm_manager.desaturation()
                elif choice == '4':
                    mode = get_input("Use Max decomposition? (y/n)", "y").lower()
                    processed_img = algorithm_manager.decomposition(is_max=(mode == 'y'))
                elif choice == '5':
                    color = get_input("Choose color channel (R/G/B)", "R").upper()
                    processed_img = algorithm_manager.single_color_channel(color=color)
                elif choice == '6':
                    shades = get_input("Number of shades (2-256)", "2")
                    processed_img = algorithm_manager.custom_gray_shades(number_of_shades=int(shades))
                else:
                    print("Invalid choice. Please try again.")
                    continue
                
                if processed_img:
                    # Suggest a default save path
                    base, ext = os.path.splitext(image_path)
                    default_save = f"{base}_gray{ext}"
                    save_path = get_input("Enter save path", default_save)
                    
                    # Ensure directory exists
                    save_dir = os.path.dirname(save_path)
                    if save_dir and not os.path.exists(save_dir):
                        os.makedirs(save_dir)
                        
                    image_loader.save_image(processed_img, save_path)
                    print(f"Successfully saved processed image to '{save_path}'")
                    
            except ValueError as e:
                print(f"Error executing algorithm: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
