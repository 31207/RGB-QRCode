import utils


def example_usage():
    # Example usage:
    # Encode a file into images
    utils.encode_file(pics_path="output_images/",
                      input_file="input_file.jpg", read_size=1000)

    # Decode images back into a file
    utils.decode_pics(pics_path="output_images/",
                      output_file="reconstructed_file.jpg")


if __name__ == "__main__":
    example_usage()
