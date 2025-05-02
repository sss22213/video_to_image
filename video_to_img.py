import os
import argparse
import glob
import time
import threading
import subprocess

class video_to_img:

    def __init__(self, ffmpeg_path, thread_number):
        self.dev = ffmpeg_path

        self.video_file = []

        self.thread_number = thread_number

    def __find_video(self):
        """
        Search the current directory for all video file.
        """
        self.video_list = []

        video_extensions = ['.mp4', '.avi', '.mov', '.mkv']
        for extension in video_extensions:
            for video_file in glob.glob(f'*{extension}'):
                self.video_list.append(video_file)

        return self.video_list
    
    def __convert_to_img(self, videofile, output_folder, save_fps, hardware_acc):
        """
        Convert video to image.
        """
 
        if not os.path.exists(output_folder):
            print(f"Create folder : {output_folder}.")
            try:
                os.makedirs(output_folder, exist_ok=True)
            except Exception as e:
                print(
                    f"Unable to create folder {output_folder}, raise exception {e}")
                return -1
        
        p = subprocess.Popen([self.dev, '-hwaccel', hardware_acc, '-i', videofile, '-pix_fmt', 'rgb24', '-vf', 'fps=' + str(save_fps), os.path.join(output_folder, str(time.time()) + '_out%d.png')])
        p.wait()


    def convert_to_img(self, output_folder, save_fps, hardware_acc):
        """
        Convert multiple video to image.
        """

        videolist = None

        videofile = None

        count = 0

        videolist = self.__find_video()

        video_number = len(videolist)
        if video_number == 0:
            print('video is not exist')
            return

        # Wait all file join to thread
        while len(videolist) != 0:
            if threading.active_count() <= self.thread_number:
                videofile = videolist.pop()
                t = threading.Thread(target = self.__convert_to_img, args = (os.path.join(os.getcwd(), videofile), os.path.join(output_folder, str(count) + '_' + str(videofile)), save_fps, hardware_acc))
                t.start()
                count = count + 1

        # Wait all video convert complete
        while threading.active_count() != 1:
            t.join()
    
def main():
    """
    Parse command line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Convert a video to PNG images with optional background removal.")
    parser.add_argument("-b", "--ffmpeg_path", type=str, help="Select ffmpeg elf(exe) file path")
    parser.add_argument("-o", "--output", type=str,
                        default=".\\output", help="Path to the output folder (default is a folder named output in the current folder).")
    parser.add_argument("-f", "--fps", type=int, default=1, help="Frames per second to save.")
    parser.add_argument("-j", "--thread_number", type=int, default=1, help="thread number")
    parser.add_argument("-a", "--hardware_acc", type=str, default='auto', help="hardware acc. ex: cuda")
    args = parser.parse_args()
    
    if not args.thread_number:
        args.thread_number = 1

    v_to_i = video_to_img(args.ffmpeg_path, args.thread_number)

    v_to_i.convert_to_img(args.output, args.fps, args.hardware_acc)

if __name__ == "__main__":
    main()
