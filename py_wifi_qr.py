"""Wifi QR Code."""
# JDD 01/2024

import qrcode

def generate_wifi_qr(ssid, encryption_type, password):
    """function to generate qr code."""
    wifi_info = f"WIFI:S:{ssid};T:{encryption_type};P:{password};;"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_info)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("wifi_qr.png")

def main():
    """main is the Main."""
    ssid = input("Enter the SSID (WiFi name): ")
    encryption_type = input("Enter the encryption type (e.g., WPA, WEP): ")
    password = input("Enter the WiFi password: ")

    generate_wifi_qr(ssid, encryption_type, password)
    print("QR code generated and saved as wifi_qr.png")

if __name__ == "__main__":
    main()
