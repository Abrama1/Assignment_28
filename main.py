from abc import ABC, abstractmethod


class MediaPlayer(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def rewind(self, seconds):
        pass

    @abstractmethod
    def fast_forward(self, seconds):
        pass


class AudioPlayer(MediaPlayer):
    def play(self):
        print("AudioPlayer: Playing audio")

    def pause(self):
        print("AudioPlayer: Pausing audio")

    def stop(self):
        print("AudioPlayer: Stopping audio")

    def rewind(self, seconds):
        print(f"AudioPlayer: Rewinding audio by {seconds} seconds")

    def fast_forward(self, seconds):
        print(f"AudioPlayer: Fast forwarding audio by {seconds} seconds")


class VideoPlayer(MediaPlayer):
    def play(self):
        print("VideoPlayer: Playing video")

    def pause(self):
        print("VideoPlayer: Pausing video")

    def stop(self):
        print("VideoPlayer: Stopping video")

    def rewind(self, seconds):
        print(f"VideoPlayer: Rewinding video by {seconds} seconds")

    def fast_forward(self, seconds):
        print(f"VideoPlayer: Fast forwarding video by {seconds} seconds")


class StreamingPlayer(MediaPlayer):
    def play(self):
        print("StreamingPlayer: Playing streaming media")

    def pause(self):
        print("StreamingPlayer: Pausing streaming media")

    def stop(self):
        print("StreamingPlayer: Stopping streaming media")

    def rewind(self, seconds):
        print(f"StreamingPlayer: Rewinding streaming media by {seconds} seconds")

    def fast_forward(self, seconds):
        print(f"StreamingPlayer: Fast forwarding streaming media by {seconds} seconds")


# Example usage
audio_player = AudioPlayer()
audio_player.play()
audio_player.pause()
audio_player.rewind(10)
audio_player.fast_forward(5)

video_player = VideoPlayer()
video_player.play()
video_player.stop()
video_player.fast_forward(20)

streaming_player = StreamingPlayer()
streaming_player.play()
streaming_player.pause()
streaming_player.rewind(30)
