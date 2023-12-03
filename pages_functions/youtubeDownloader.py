from PyQt5.QtWidgets import QWidget

from ui.pages.youtube_downloader_ui import Ui_Form


from . import playlistManager

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QAudioOutput


class YoutubeDownloader(QWidget):
    def __init__(self):
        super(YoutubeDownloader, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.download_btn = self.ui.pushButton
        self.view_list_items = self.ui.listWidget
        self.url_playlist = self.ui.lineEdit
        self.progressBar = self.ui.progressBar
        self.progressBar.setVisible(False)
        
        self.folder_path = None
        
        
    def download_item_mp3(self):
        self.folder_path, self.view_list_items = playlistManager.download_item_mp3(self.folder_path,self.view_list_items,self.url_playlist,self.progressBar)