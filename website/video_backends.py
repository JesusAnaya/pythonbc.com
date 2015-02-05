
from embed_video.backends import YoutubeBackend


class YoutubeBackendHttps(YoutubeBackend):
    @property
    def protocol(self):
        return 'https'
