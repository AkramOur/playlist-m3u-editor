from PyQt5.QtWidgets import QWidget, QFileDialog, QListWidgetItem, QMessageBox
from PyQt5.QtCore import QDir, QFileInfo, Qt, QTimer, QUrl, QTime, QCoreApplication, QThread, pyqtSignal

from ui.pages.create_playlist_ui import Ui_Form

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QAudioOutput
import os
import shutil

from moviepy.editor import AudioFileClip

from . import download


class DownloadThread(QThread):
    finished = pyqtSignal()

    def __init__(self, url, folder_path):
        super().__init__()
        self.url = url
        self.folder_path = folder_path

    def run(self):
        download.download_playlist_youtube(self.url, self.folder_path)
        self.finished.emit()


def load_items(folder_path,view_list_items):
    # Open a file dialog to allow the user to select a folder
    folder_dialog = QFileDialog()
    folder_dialog.setFileMode(QFileDialog.Directory)
    folder_dialog.setOption(QFileDialog.ShowDirsOnly)

    if folder_dialog.exec_():
        # Get the selected folder
        folder_path = folder_dialog.selectedFiles()[0]
        # Clear the current items in the view list
        view_list_items.clear()

        # Add the elements of the selected folder to the view list
        for file_name in os.listdir(folder_path):
            # Create a QListWidgetItem and add it to the QListView
            list_item = QListWidgetItem(file_name)
            view_list_items.addItem(list_item)
    
    return folder_path, view_list_items


def add_items(folder_path,view_list_items):
    if folder_path is None:
        # Show an error message if folder_path is not set
        showError("Please load items before adding items.")
        return view_list_items

    # Open a file dialog to allow the user to select MP3 files
    file_dialog = QFileDialog()
    file_dialog.setNameFilter("MP3 files (*.mp3 *.flac)")
    file_dialog.setFileMode(QFileDialog.ExistingFiles)

    if file_dialog.exec_():
        # Get the list of selected files
        selected_files = file_dialog.selectedFiles()
        # Copy the selected MP3 files to the folder_path
        for selected_file in selected_files:
            destination_path = os.path.join(folder_path, os.path.basename(selected_file))
            #if the file already exists in the directory
            if folder_path != os.path.dirname(selected_file):
                shutil.copyfile(selected_file, destination_path)

            # Create a QListWidgetItem and add it to the QListView
            list_item = QListWidgetItem(os.path.basename(destination_path))
            view_list_items.addItem(list_item)
            
    return view_list_items

def delete_items(folder_path,view_list_items):
    # Check if there is any selected item in the list
    selected_items = view_list_items.selectedItems()

    if not selected_items:
        showError("No item selected. Please select a music file.")
        return view_list_items
    
    result = showConfirmation("Are you sure you want to delete the selected item(s)?")

    if result == QMessageBox.Yes:
        # Delete selected items from the list and the folder
        for item in selected_items:
            item_text = item.text()
            item_path = os.path.join(folder_path, item_text)

            # Remove the item from the list
            row = view_list_items.row(item)
            view_list_items.takeItem(row)

            # Remove the item from the folder
            os.remove(item_path)
    return view_list_items
            
            
def showError(message):
    error_dialog = QMessageBox()
    error_dialog.setIcon(QMessageBox.Critical)
    error_dialog.setWindowTitle("Error")
    error_dialog.setText(message)
    error_dialog.exec_()
    
def showConfirmation(message):
    confirm_dialog = QMessageBox()
    confirm_dialog.setIcon(QMessageBox.Question)
    confirm_dialog.setWindowTitle("Confirmation")
    confirm_dialog.setText(message)
    confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    return confirm_dialog.exec_()

def showSuccess(message):
    success_dialog = QMessageBox()
    success_dialog.setIcon(QMessageBox.Information)
    success_dialog.setWindowTitle("Success")
    success_dialog.setText(message)
    success_dialog.exec_()

def showWarning(message):
    success_dialog = QMessageBox()
    success_dialog.setIcon(QMessageBox.Warning)
    success_dialog.setWindowTitle("Warning")
    success_dialog.setText(message)
    success_dialog.exec_()



def play_music(folder_path,view_list_items,media_player,music_playing):
    # Check if there is any selected item in the list
    if view_list_items.currentItem() is not None:
        # Get the selected item text (file name)
        selected_item_text = view_list_items.currentItem().text()

        # Construct the full path to the selected MP3 file
        selected_file_path = os.path.join(folder_path, selected_item_text)
        print('selected_file_path' ,selected_file_path)
        # Stop any currently playing music
        stop_music(music_playing,media_player)

        # Load and play the selected music file using QMediaPlayer
        media_content = QMediaContent(QUrl.fromLocalFile(selected_file_path))
        media_player.setMedia(media_content)
        media_player.play()

        return True, media_player
    else:
        showError("No item selected. Please select a music file.")
        return False, media_player

def stop_music(music_playing,media_player):
    # Check if music is currently playing
    if music_playing:
        # Stop the currently playing music
        media_player.stop()

    return False,media_player

def position_changed(slider_music, position, labelTimer, media_player):
    if slider_music.maximum() != media_player.duration():
        slider_music.setMaximum(media_player.duration())
    slider_music.setValue(position)

    seconds = int((position / 1000) % 60)
    minutes = int((position / 60000) % 60)
    hours = int((position / 2600000) % 24)

    time = QTime(hours, minutes, seconds)
    labelTimer.setText(time.toString())
    
    return slider_music,labelTimer


def duration_changed(slider_music, duration):
    slider_music.setRange(0,duration)
    return slider_music

def play_slider_changed(media_player, position):
    media_player.setPosition(position)
    return media_player

def save_playlist(folder_path,view_list_items):
    if not folder_path:
        # Show an error message if folder_path is not set
        showError("Please load items before saving the playlist.")
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
            for row in range(view_list_items.count()):
                item = view_list_items.item(row)
                item_text = item.text()
                item_path = folder_path+"/"+item_text

                # Get the duration of the media item
                duration = get_media_duration(item_path)

                # Write the path and duration to the playlist file
                playlist_file.write(f"#EXTINF:{duration},{item_text}\n")
                playlist_file.write(f"{item_text}\n")

        # Show a success message
        showSuccess("Playlist saved successfully.")

def get_media_duration(file_path):
    
    # Load the audio file
    audio_clip = AudioFileClip(file_path)

    # Get the duration in seconds
    duration_in_seconds = audio_clip.duration

    return int(duration_in_seconds)


def load_items_youtube(folder_path,view_list_items,url_playlist,progressBar):
    url = url_playlist.text()
    if url is None or not url.startswith("https://www.youtube.com/watch?"):
        showError("Please enter a valid URL playlist")
        return folder_path, view_list_items
    progressBar.setVisible(True)
    # Open a file dialog to allow the user to select a folder
    folder_dialog = QFileDialog()
    folder_dialog.setFileMode(QFileDialog.Directory)
    folder_dialog.setOption(QFileDialog.ShowDirsOnly)

    if folder_dialog.exec_():
        # Get the selected folder
        folder_path = folder_dialog.selectedFiles()[0]
        # Clear the current items in the view list
        view_list_items.clear()

        # Create and start the download thread
        download_thread = DownloadThread(url, folder_path)
        download_thread.finished.connect(progressBar.hide)
        download_thread.start()

        # Update the progress bar while the thread is running
        while download_thread.isRunning():
            QCoreApplication.processEvents()

        # Add the elements of the selected folder to the view list
        for file_name in os.listdir(folder_path):
            # Create a QListWidgetItem and add it to the QListView
            list_item = QListWidgetItem(file_name)
            view_list_items.addItem(list_item)

    return folder_path, view_list_items


def download_item_mp3(folder_path,view_list_items,url_playlist,progressBar):
    url = url_playlist.text()
    if url is None or not url.startswith("https://www.youtube.com/watch?"):
        showError("Please enter a valid URL video")
        return folder_path, view_list_items
    progressBar.setVisible(True)
    # Open a file dialog to allow the user to select a folder
    folder_dialog = QFileDialog()
    folder_dialog.setFileMode(QFileDialog.Directory)
    folder_dialog.setOption(QFileDialog.ShowDirsOnly)

    if folder_dialog.exec_():
        # Get the selected folder
        folder_path = folder_dialog.selectedFiles()[0]
        # Clear the current items in the view list
        view_list_items.clear()

        # Create and start the download thread
        download_thread = DownloadThread(url, folder_path)
        download_thread.finished.connect(progressBar.hide)
        download_thread.start()

        # Update the progress bar while the thread is running
        while download_thread.isRunning():
            QCoreApplication.processEvents()

        # Add the elements of the selected folder to the view list
        for file_name in os.listdir(folder_path):
            # Create a QListWidgetItem and add it to the QListView
            list_item = QListWidgetItem(file_name+' Downloaded !')
            view_list_items.addItem(list_item)

    return folder_path, view_list_items

def load_playlist(playlist_Path,view_list_items):

    # Open a file dialog to get the file name and location for the playlist
    file_dialog = QFileDialog()
    file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
    file_dialog.setNameFilter("M3U Playlist (*.m3u)")

    if file_dialog.exec_():
        # Get the selected folder
        playlist_Path = file_dialog.selectedFiles()[0]
        # Clear the current items in the view list
        view_list_items.clear()

        with open(playlist_Path, 'r', encoding='utf-8') as playlist_file:
            for line in playlist_file:
                # Skip lines that start with '#', as they contain metadata
                if not line.startswith("#"):
                    file = os.path.basename(line.strip())
                    if not os.path.exists(os.path.dirname(playlist_Path) + "/" + file):
                        showWarning("The file " + file + " not exist!")
                        continue
                    # Strip any extra whitespace/newlines and add the path to the list
                    # Create a QListWidgetItem and add it to the QListView
                    list_item = QListWidgetItem(file)
                    view_list_items.addItem(list_item)
    
    return playlist_Path, view_list_items

def update_playlist(playlist_Path, view_list_items):
    if not playlist_Path:
        # Show an error message if folder_path is not set
        showError("Please load the playlist before updating.")
        return

    # Open the playlist file in write mode
    with open(playlist_Path, 'w', encoding='utf-8') as playlist_file:
        # Write the header information to the playlist file
        playlist_file.write("#EXTM3U\n")
        # Iterate through the items in the view list and write each path and duration to the playlist file
        for row in range(view_list_items.count()):
            item = view_list_items.item(row)
            item_text = item.text()
            item_path = os.path.dirname(playlist_Path) + "/" + item_text
            # verify if th file exist
            if not os.path.exists(item_path):
                continue
            # Get the duration of the media item
            duration = get_media_duration(item_path)
            # Write the path and duration to the playlist file
            playlist_file.write(f"#EXTINF:{duration},{item_text}\n")
            playlist_file.write(f"{item_text}\n")

    # Show a success message
    showSuccess("Playlist saved successfully.")