import base64

def encode_base64(data):
    """Encode data to Base64 format."""
    return base64.b64encode(data.encode()).decode()

def decode_base64(encoded_data):
    """Decode Base64 format back to original data."""
    return base64.b64decode(encoded_data).decode()

def main():
    original_message = "Hello, World!"
    print(f"Original Message: {original_message}")

    # Encode the message
    encoded_message = encode_base64(original_message)
    print(f"Encoded Message (Base64): {encoded_message}")

    # Decode the message
    decoded_message = decode_base64(encoded_message)
    print(f"Decoded Message: {decoded_message}")

if __name__ == "__main__":
    main()
