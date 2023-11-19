from PyQt5.QtWidgets import QWidget, QFileDialog, QListWidgetItem, QMessageBox
from PyQt5.QtCore import QDir, QFileInfo, Qt, QTimer, QUrl, QTime, QCoreApplication

from ui.pages.create_playlist_ui import Ui_Form

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QAudioOutput
import os
import shutil

from moviepy.editor import AudioFileClip

from . import playlistManager

class CreatePlaylist(QWidget):
    def __init__(self):
        super(CreatePlaylist, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        ## =======================================================================================================
        ## Get all the objects in windows
        ## =======================================================================================================
        self.load_items_btn = self.ui.pushButton
        self.add_items_btn = self.ui.pushButton_3
        self.view_list_items = self.ui.listWidget
        self.play_music_btn = self.ui.pushButton_6
        self.stop_music_btn = self.ui.pushButton_5
        self.delete_items_btn = self.ui.pushButton_4
        self.slider_music = self.ui.horizontalSlider
        self.labelTimer = self.ui.labelTimer
        self.save_playlist_btn = self.ui.pushButton_2
        
        
        
        #pygame.mixer.init()
        self.audio = QAudioOutput()
        self.media_player = QMediaPlayer(self.audio)
        
        self.folder_path = None
        self.music_playing = False

        #self.media_player.setAudioOutput(self.audio)

        self.load_items_btn.clicked.connect(self.load_items)
        self.add_items_btn.clicked.connect(self.add_items)
        self.delete_items_btn.clicked.connect(self.delete_items)
        self.play_music_btn.clicked.connect(self.play_music)
        self.stop_music_btn.clicked.connect(self.stop_music)
        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)
        self.slider_music.sliderMoved.connect(self.play_slider_changed)
        self.save_playlist_btn.clicked.connect(self.save_playlist)


    def load_items(self):
        self.folder_path, self.view_list_items = playlistManager.load_items(self.folder_path,self.view_list_items)

    def add_items(self):
        self.view_list_items = playlistManager.add_items(self.folder_path,self.view_list_items)

    def delete_items(self):
        self.view_list_items = playlistManager.delete_items(self.folder_path,self.view_list_items)

    def play_music(self):
        self.music_playing, self.media_player=playlistManager.play_music(self.folder_path, self.view_list_items, self.media_player, self.music_playing)
        

    def stop_music(self):
        self.music_playing, self.media_player = playlistManager.stop_music(self.music_playing, self.media_player)

    def position_changed(self, position):
        self.slider_music, self.labelTimer = playlistManager.position_changed(self.slider_music, position, self.labelTimer, self.media_player)

    def duration_changed(self, duration):
        self.slider_music = playlistManager.duration_changed(self.slider_music, duration)

    def play_slider_changed(self, position):
        self.media_player = playlistManager.play_slider_changed(self.media_player, position)


    def save_playlist(self):
        playlistManager.save_playlist(self.folder_path,self.view_list_items)