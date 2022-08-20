from os.path import join
from os import listdir
from random import choice
#from moviepy.editor import *
#from moviepy import *
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.all import crop

INSPIRATION_TYPES = [ 'grind', 'religious' ]
ASSETS_PATH = 'assets'
ASSETS_TYPE_PATH = {
    'grind': join(ASSETS_PATH, 'grind'),
    'religious': join(ASSETS_PATH, 'grind'),
}

class InspirationalVideo:

    def __init__(self, type):
        if type in INSPIRATION_TYPES:
            self.type = type
        else:
            raise Exception(f"""Type must be one of these: '{"', '".join(INSPIRATION_TYPES)}'.""")
    
    def generate_video(self, output_path, video_path, phrase):
        
        video_path = self.get_random_video_path()
        phrase = self.get_random_phrase()

        video = VideoFileClip(video_path)
        text = TextClip(phrase, method='caption', fontsize=40, color='yellow', stroke_width=1, stroke_color='white') \
                    .set_position(('center', 'bottom')) \
                    .set_duration(video.duration)
        video = CompositeVideoClip([video, text])
        video.write_videofile(output_path)

    def generate_random_video(self, output_path):

        video_path = self.get_random_video_path()
        phrase = self.get_random_phrase()
        self.generate_video( output_path, video_path, phrase)

    def get_random_video_path(self):
        return choice(self.get_videos_path())

    def get_videos_path(self):
        videos_folder_path = join( ASSETS_TYPE_PATH[self.type], 'videos')
        videos_names = listdir(videos_folder_path)
        videos_paths = [join(videos_folder_path, video_name) for video_name in videos_names]
        return videos_paths

    def get_random_phrase(self):
        return choice(self.get_phrases())
    
    def get_phrases(self):
        
        phrases_file_path = join( ASSETS_TYPE_PATH[self.type], 'phrases.txt' )
        with open(phrases_file_path, 'r', encoding='utf-8') as phrases_file:
            phrases = phrases_file.readlines()
        return phrases
    