from PyQt5.QtWidgets import QWidget, QFileDialog, QListWidgetItem, QMessageBox
from PyQt5.QtCore import QDir, QFileInfo, Qt, QTimer, QUrl, QTime, QCoreApplication

from ui.pages.edit_playlist_ui import Ui_Form

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QAudioOutput
import os
import shutil

from moviepy.editor import AudioFileClip

from . import playlistManager


class EditPlaylist(QWidget):
    def __init__(self):
        super(EditPlaylist, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        ## =======================================================================================================
        ## Get all the objects in windows
        ## =======================================================================================================
        self.load_playlist_btn = self.ui.pushButton
        self.add_items_btn = self.ui.pushButton_3
        self.view_list_items = self.ui.listWidget
        self.play_music_btn = self.ui.pushButton_6
        self.stop_music_btn = self.ui.pushButton_5
        self.delete_items_btn = self.ui.pushButton_4
        self.slider_music = self.ui.horizontalSlider
        self.labelTimer = self.ui.labelTimer
        self.update_playlist_btn = self.ui.pushButton_2

        self.audio = QAudioOutput()
        self.media_player = QMediaPlayer(self.audio)
        
        self.music_playing = False
        self.playlist_Path = None

        self.load_playlist_btn.clicked.connect(self.load_playlist)
        self.add_items_btn.clicked.connect(self.add_items)
        self.delete_items_btn.clicked.connect(self.delete_items)
        self.play_music_btn.clicked.connect(self.play_music)
        self.stop_music_btn.clicked.connect(self.stop_music)
        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)
        self.slider_music.sliderMoved.connect(self.play_slider_changed)
        self.update_playlist_btn.clicked.connect(self.update_playlist)

    def load_playlist(self):
        self.playlist_Path, self.view_list_items = playlistManager.load_playlist(self.playlist_Path,self.view_list_items)

    def add_items(self):
        if not self.playlist_Path:
            playlistManager.showError("Please load playlist before adding items.")
            return
        self.view_list_items = playlistManager.add_items(os.path.dirname(self.playlist_Path),self.view_list_items)

    def delete_items(self):
        if not self.playlist_Path:
            playlistManager.showError("Please load playlist before deleting items.")
            return
        self.view_list_items = playlistManager.delete_items(os.path.dirname(self.playlist_Path),self.view_list_items)

    def play_music(self):
        if not self.playlist_Path:
            playlistManager.showError("Please load playlist before playing music.")
            return
        self.music_playing, self.media_player=playlistManager.play_music(os.path.dirname(self.playlist_Path), self.view_list_items, self.media_player, self.music_playing)
        
    def stop_music(self):
        self.music_playing, self.media_player = playlistManager.stop_music(self.music_playing, self.media_player)

    def position_changed(self, position):
        self.slider_music, self.labelTimer = playlistManager.position_changed(self.slider_music, position, self.labelTimer, self.media_player)

    def duration_changed(self, duration):
        self.slider_music = playlistManager.duration_changed(self.slider_music, duration)

    def play_slider_changed(self, position):
        self.media_player = playlistManager.play_slider_changed(self.media_player, position)


    def update_playlist(self):
        playlistManager.update_playlist(self.playlist_Path,self.view_list_items)
