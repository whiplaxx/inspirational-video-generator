from inspirational_video import InspirationalVideo

def main():

    grind_video = InspirationalVideo('grind')
    grind_video.generate_random_video('grind.mp4')
    #for index_video, video_path in enumerate(grind_video.get_videos_path()):
    #    for index_phrase, phrase in enumerate(grind_video.get_phrases()):
    #        grind_video.generate_video(f"grind_{index_video}_{index_phrase}.mp4", video_path=video_path, phrase=phrase)

if __name__ == '__main__':

    main()
