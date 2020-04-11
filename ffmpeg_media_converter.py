import ffmpeg
from sys import argv

# Name input and output file format
def main():
    # File to convert
    file_in = argv[1]
    # File format & name to convert to
    file_out = argv[2]

    # C lib to convert media files
    (
        ffmpeg
        .input(file_in)
        .output(file_out)
        .run()
    )

if __name__ == '__main__':
    if len(argv) < 3:
        print("Usage: <filename> <input_file> <output_file>")
    else:
        main()

