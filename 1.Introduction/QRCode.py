import qrcode

def generate_QRCode(f_name, l_name, phone_number):
    qr = qrcode.QRCode(
        version = 2,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    data = f"f_name: {f_name}\nl_name: {l_name}\nphone_number: {phone_number}"

    qr.add_data(data)
    qr.make(fit= True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save("qrcode.png")

if __name__ == "__main__":
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")
    phone_number = int(input("Enter phone number: "))

    generate_QRCode(f_name, l_name, phone_number )

    print("QR Code generated successfully!")