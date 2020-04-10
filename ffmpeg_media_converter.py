import ffmpeg
from sys import argv

# Name input and output file format
def main():
    file_in = argv[1]
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
        print("Usage: %s <filename> <input_file> <output_file>",)
    else:
        main()

