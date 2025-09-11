#Generate a QR code
#This is a Medium level project
#This project is created by Md Aminul islam Bhuiyan
#Date: 2025-Jan-19
import qrcode

def generate_qr_code(text, file_name):
    '''
    Generates a QR code from the given text and saves it as an image file.

    Parameters:
    text (str): The text or URL to encode in the QR code.
    file_name (str): The name of the file where the QR code image will be saved.
    '''
    try:
        qr = qrcode.QRCode(
            version = 1,
            error_correction= qrcode.constants.ERROR_CORRECT_L,
            box_size= 10,
            border=3
        )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color = "#000000", back_color = "White")
        img.save(file_name)
        print(f"QR code successfully saved as {file_name}")
    except Exception as e:
        print(f"An error occurred:{e}")

if __name__ == "__main__":
    # text = "https://github.com/aminul01-g/pythonProjects"
    text = input("Input Your URL or Text: ")
    file_name = "qr_code.png"

    generate_qr_code(text, file_name)
    print(f"QR code saved as {file_name}")