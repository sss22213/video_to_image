# Video to Image Converter

This Python script converts videos to a series of PNG images, allowing users to specify the frame rate at which images are saved. 

## Installation

To run this script, you'll need to ensure you have the required Python libraries. Install them using the `requirements.txt` file provided in this repository.


```
pip install -r requirements.txt
```

## Usage

Ensure you have Python 3.6 or newer installed on your system. Clone this repository or download the script and `requirements.txt` file. Then, install the required libraries as mentioned above.

To use the script, run it from the command line with the desired options:

```
python video_to_img.py [options]
```

## Options

- `-b`, `--b` <ffmpeg path>: Specify the ffmpeg elf(exe) path 

- `-o`, `--output` <output_folder>: Specify the path to the output folder where PNG images will be saved. If not specified, images are saved to a default `output` directory at the root of the program.

- `-f`, `--fps` <frames_per_second>: Specify the number of frames per second to save.

- `-h`, `--help`: Display help information showing all command-line options.

- `-j`, `--thread_number`: uising thread number. Recommand 1.

## Example

1. To convert all video at folder A, putting video_to_img.py to folder A.

2. Execute below the command:

```
python video_to_img.py [options]
```

3. Then, the Python script will automatically convert the videos in folder A to the output folder.

## Note:
ffmpeg download: https://www.ffmpeg.org/download.html

ffmpeg with nvidia: https://github.com/m-ab-s/media-autobuild_suite?tab=readme-ov-file


