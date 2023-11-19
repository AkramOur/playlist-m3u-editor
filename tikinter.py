from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidget, QPushButton, QVBoxLayout, QWidget

class PlaylistEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Modern Playlist Editor")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.interfaces = {}

        self.create_menu()
        self.create_interface("Interface 1")
        self.create_interface("Interface 2")

        self.show_interface("Interface 1")

    def create_menu(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")
        file_menu.addAction("Open", self.open_file)
        file_menu.addAction("Exit", self.close)

        interface_menu = menubar.addMenu("Interface")

        for interface_name in self.interfaces:
            interface_menu.addAction(interface_name, lambda i=interface_name: self.show_interface(i))

    def create_interface(self, interface_name):
        interface_widget = QWidget(self.central_widget)
        self.central_layout = QVBoxLayout(interface_widget)

        playlist = QListWidget()
        self.central_layout.addWidget(playlist)

        add_button = QPushButton("Add Track", interface_widget)
        add_button.clicked.connect(lambda: self.add_track(playlist))
        self.central_layout.addWidget(add_button)

        remove_button = QPushButton("Remove Track", interface_widget)
        remove_button.clicked.connect(lambda: self.remove_track(playlist))
        self.central_layout.addWidget(remove_button)

        save_button = QPushButton("Save Playlist", interface_widget)
        save_button.clicked.connect(lambda: self.save_playlist(playlist))
        self.central_layout.addWidget(save_button)

        load_button = QPushButton("Load Playlist", interface_widget)
        load_button.clicked.connect(lambda: self.load_playlist(playlist))
        self.central_layout.addWidget(load_button)

        self.interfaces[interface_name] = {"widget": interface_widget, "playlist": playlist}

    def show_interface(self, interface_name):
        self.setCentralWidget(self.interfaces[interface_name]["widget"])

    def add_track(self, playlist):
        track_path, _ = QFileDialog.getOpenFileName(self, "Select a track", "", "MP3 files (*.mp3);;All Files (*)")
        if track_path:
            playlist.addItem(track_path)

    def remove_track(self, playlist):
        selected_item = playlist.currentItem()
        if selected_item:
            playlist.takeItem(playlist.row(selected_item))

    def save_playlist(self, playlist):
        playlist_path, _ = QFileDialog.getSaveFileName(self, "Save Playlist", "", "M3U files (*.m3u);;All Files (*)")
        if playlist_path:
            with open(playlist_path, "w", encoding="utf-8") as file:
                for row in range(playlist.count()):
                    file.write(playlist.item(row).text() + "\n")

    def load_playlist(self, playlist):
        playlist_path, _ = QFileDialog.getOpenFileName(self, "Select a playlist", "", "M3U files (*.m3u);;All Files (*)")
        if playlist_path:
            playlist.clear()
            with open(playlist_path, "r") as file:
                for line in file:
                    playlist.addItem(line.strip())

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if file_path:
            print(f"Opening file: {file_path}")


if __name__ == "__main__":
    app = QApplication([])
    window = PlaylistEditor()
    window.show()
    app.exec_()
