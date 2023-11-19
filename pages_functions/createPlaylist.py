from PyQt5.QtWidgets import QWidget, QFileDialog, QListWidgetItem, QMessageBox
from PyQt5.QtCore import QDir, QFileInfo, Qt, QTimer, QUrl, QTime, QCoreApplication

from ui.pages.create_playlist_ui import Ui_Form

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QAudioOutput
import os
import shutil

from moviepy.editor import AudioFileClip

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
        # Open a file dialog to allow the user to select a folder
        folder_dialog = QFileDialog()
        folder_dialog.setFileMode(QFileDialog.Directory)
        folder_dialog.setOption(QFileDialog.ShowDirsOnly)

        if folder_dialog.exec_():
            # Get the selected folder
            selected_folder = folder_dialog.selectedFiles()[0]
            self.folder_path = selected_folder
            # Clear the current items in the view list
            self.view_list_items.clear()

            # Add the elements of the selected folder to the view list
            for file_name in os.listdir(selected_folder):
                # Create a QListWidgetItem and add it to the QListView
                list_item = QListWidgetItem(file_name)
                self.view_list_items.addItem(list_item)

    def add_items(self):
        if self.folder_path is None:
            # Show an error message if folder_path is not set
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Critical)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("Please load items before adding items.")
            error_dialog.exec_()
            return

        # Open a file dialog to allow the user to select MP3 files
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("MP3 files (*.mp3)")
        file_dialog.setFileMode(QFileDialog.ExistingFiles)

        if file_dialog.exec_():
            # Get the list of selected files
            selected_files = file_dialog.selectedFiles()

            # Copy the selected MP3 files to the folder_path
            for selected_file in selected_files:
                destination_path = os.path.join(self.folder_path, os.path.basename(selected_file))
                shutil.copyfile(selected_file, destination_path)

                # Create a QListWidgetItem and add it to the QListView
                list_item = QListWidgetItem(os.path.basename(destination_path))
                self.view_list_items.addItem(list_item)

    def delete_items(self):
        # Check if there is any selected item in the list
        selected_items = self.view_list_items.selectedItems()

        if not selected_items:
            print("No item selected. Please select a music file.")
            return

        confirm_dialog = QMessageBox()
        confirm_dialog.setIcon(QMessageBox.Question)
        confirm_dialog.setWindowTitle("Confirmation")
        confirm_dialog.setText("Are you sure you want to delete the selected item(s)?")

        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = confirm_dialog.exec_()

        if result == QMessageBox.Yes:
            # Delete selected items from the list and the folder
            for item in selected_items:
                item_text = item.text()
                item_path = os.path.join(self.folder_path, item_text)

                # Remove the item from the list
                row = self.view_list_items.row(item)
                self.view_list_items.takeItem(row)

                # Remove the item from the folder
                os.remove(item_path)

    def play_music(self):
        # Check if there is any selected item in the list
        if self.view_list_items.currentItem() is not None:
            # Get the selected item text (file name)
            selected_item_text = self.view_list_items.currentItem().text()

            # Construct the full path to the selected MP3 file
            selected_file_path = os.path.join(self.folder_path, selected_item_text)

            # Stop any currently playing music
            self.stop_music()

            # Load and play the selected music file using QMediaPlayer
            media_content = QMediaContent(QUrl.fromLocalFile(selected_file_path))
            self.media_player.setMedia(media_content)
            self.media_player.play()

            self.music_playing = True
        else:
            print("No item selected. Please select a music file.")

    def stop_music(self):
        # Check if music is currently playing
        if self.music_playing:
            # Stop the currently playing music
            self.media_player.stop()

            # Reset the flag to indicate that music is not playing
            self.music_playing = False

    def position_changed(self, position):
        if self.slider_music.maximum() != self.media_player.duration():
            self.slider_music.setMaximum(self.media_player.duration())
        self.slider_music.setValue(position)

        seconds = int((position / 1000) % 60)
        minutes = int((position / 60000) % 60)
        hours = int((position / 2600000) % 24)

        time = QTime(hours, minutes, seconds)
        self.labelTimer.setText(time.toString())

    def duration_changed(self, duration):
        self.slider_music.setRange(0,duration)

    def play_slider_changed(self, position):
        self.media_player.setPosition(position)


    def save_playlist(self):
        if not self.folder_path:
            # Show an error message if folder_path is not set
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Critical)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("Please load items before saving the playlist.")
            error_dialog.exec_()
            return

        # Open a file dialog to get the file name and location for the playlist
        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("M3U Playlist (*.m3u)")

        if file_dialog.exec_():
            # Get the selected file path for saving the playlist
            playlist_file_path = file_dialog.selectedFiles()[0]

            # Open the playlist file in write mode
            with open(playlist_file_path, 'w', encoding='utf-8') as playlist_file:
                # Write the header information to the playlist file
                playlist_file.write("#EXTM3U\n")

                # Iterate through the items in the view list and write each path and duration to the playlist file
                for row in range(self.view_list_items.count()):
                    item = self.view_list_items.item(row)
                    item_text = item.text()
                    print('self.folder_path ',self.folder_path)
                    item_path = self.folder_path+"/"+item_text

                    # Get the duration of the media item
                    duration = self.get_media_duration(item_path)

                    # Write the path and duration to the playlist file
                    playlist_file.write(f"#EXTINF:{duration},{item_text}\n")
                    playlist_file.write(f"{item_text}\n")

            # Show a success message
            success_dialog = QMessageBox()
            success_dialog.setIcon(QMessageBox.Information)
            success_dialog.setWindowTitle("Success")
            success_dialog.setText("Playlist saved successfully.")
            success_dialog.exec_()

    def get_media_duration(self, file_path):
        # Load the audio file
        audio_clip = AudioFileClip(file_path)

        # Get the duration in seconds
        duration_in_seconds = audio_clip.duration

        return int(duration_in_seconds)
