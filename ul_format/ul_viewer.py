#!/usr/bin/env python3
"""
my own png viewer, but for the custom ".ul" image format defined in ul_format.py
ul_viewer.py
============

A Qt (PySide6) desktop application for viewing ".ul" image files
(the custom format defined in ul_format.py).

Features:
- File > Open... to browse for a .ul file
- Drag-and-drop a .ul file onto the window
- File > Open Recent
- Zoom in / out / actual size / fit to window
- File > Import PNG... converts a PNG (or other image) into .ul and opens it
- File > Export as PNG... saves the currently open .ul image as a PNG

Run with:
    pip install PySide6 Pillow
    python ul_viewer.py [optional_path_to_file.ul]
"""

import os
import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QImage, QPixmap, QAction, QKeySequence, QIcon
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QScrollArea, QFileDialog,
    QMessageBox, QToolBar, QStatusBar, QSizePolicy
)

from ul_format import read_ul_file, write_ul_file, UlFormatError

APP_TITLE = "UL Image Viewer"
ZOOM_STEP = 1.25
MIN_ZOOM = 0.05
MAX_ZOOM = 20.0


def ul_image_to_qimage(ul_img) -> QImage:
    """Convert a UlImage (from ul_format) into a QImage, copying the pixel buffer."""
    fmt = QImage.Format_RGBA8888 if ul_img.channels == 4 else QImage.Format_RGB888
    bytes_per_line = ul_img.width * ul_img.channels
    qimg = QImage(ul_img.pixels, ul_img.width, ul_img.height, bytes_per_line, fmt)
    # .copy() forces Qt to own its own buffer, decoupling it from the Python bytes object
    return qimg.copy()


class UlViewerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_TITLE)
        self.resize(1000, 720)
        self.setAcceptDrops(True)

        self.current_path = None
        self.current_qimage = None
        self.zoom_factor = 1.0
        self.fit_to_window = True

        # --- Central image display ---
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setBackgroundRole(QLabel().backgroundRole())
        self.image_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.image_label.setScaledContents(False)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.image_label)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.scroll_area)

        self._build_menu_and_toolbar()

        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage("Open a .ul file to get started (File > Open, or drag & drop)")

    # ---------------------------------------------------------- UI setup
    def _build_menu_and_toolbar(self):
        open_action = QAction("&Open...", self)
        open_action.setShortcut(QKeySequence.Open)
        open_action.triggered.connect(self.open_file_dialog)

        import_action = QAction("&Import PNG/Image...", self)
        import_action.triggered.connect(self.import_image_dialog)

        export_action = QAction("&Export as PNG...", self)
        export_action.triggered.connect(self.export_png_dialog)

        quit_action = QAction("E&xit", self)
        quit_action.setShortcut(QKeySequence.Quit)
        quit_action.triggered.connect(self.close)

        zoom_in_action = QAction("Zoom &In", self)
        zoom_in_action.setShortcut(QKeySequence.ZoomIn)
        zoom_in_action.triggered.connect(self.zoom_in)

        zoom_out_action = QAction("Zoom &Out", self)
        zoom_out_action.setShortcut(QKeySequence.ZoomOut)
        zoom_out_action.triggered.connect(self.zoom_out)

        actual_size_action = QAction("&Actual Size", self)
        actual_size_action.setShortcut("Ctrl+0")
        actual_size_action.triggered.connect(self.zoom_actual_size)

        fit_action = QAction("&Fit to Window", self)
        fit_action.setShortcut("Ctrl+9")
        fit_action.triggered.connect(self.zoom_fit_to_window)

        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(open_action)
        file_menu.addAction(import_action)
        file_menu.addAction(export_action)
        file_menu.addSeparator()
        file_menu.addAction(quit_action)

        view_menu = menu.addMenu("&View")
        view_menu.addAction(zoom_in_action)
        view_menu.addAction(zoom_out_action)
        view_menu.addAction(actual_size_action)
        view_menu.addAction(fit_action)

        toolbar = QToolBar("Main")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        for action in (open_action, import_action, export_action, None,
                       zoom_out_action, zoom_in_action, actual_size_action, fit_action):
            if action is None:
                toolbar.addSeparator()
            else:
                toolbar.addAction(action)

    # ---------------------------------------------------------- Drag & drop
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            path = url.toLocalFile()
            if path.lower().endswith(".ul"):
                self.load_ul_file(path)
                return
        QMessageBox.warning(self, APP_TITLE, "Please drop a .ul file.")

    # ---------------------------------------------------------- File actions
    def open_file_dialog(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Open .ul file", "", "UL Images (*.ul);;All Files (*)"
        )
        if path:
            self.load_ul_file(path)

    def load_ul_file(self, path: str):
        try:
            ul_img = read_ul_file(path)
        except (UlFormatError, OSError) as e:
            QMessageBox.critical(self, APP_TITLE, f"Could not open file:\n{e}")
            return

        self.current_qimage = ul_image_to_qimage(ul_img)
        self.current_path = path
        self.fit_to_window = True
        self._refresh_display()

        self.setWindowTitle(f"{APP_TITLE} - {os.path.basename(path)}")
        size_kb = os.path.getsize(path) / 1024
        self.status.showMessage(
            f"{os.path.basename(path)}  |  {ul_img.width}x{ul_img.height}  |  "
            f"{'RGBA' if ul_img.channels == 4 else 'RGB'}  |  {size_kb:.1f} KB"
        )

    def import_image_dialog(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Import image to convert to .ul", "",
            "Images (*.png *.jpg *.jpeg *.bmp *.gif *.webp *.tif *.tiff);;All Files (*)"
        )
        if not path:
            return

        try:
            from PIL import Image
            img = Image.open(path)
            if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
                img = img.convert("RGBA")
                channels = 4
            else:
                img = img.convert("RGB")
                channels = 3
            width, height = img.size
            pixels = img.tobytes()
        except Exception as e:
            QMessageBox.critical(self, APP_TITLE, f"Could not read image:\n{e}")
            return

        default_out = os.path.splitext(path)[0] + ".ul"
        out_path, _ = QFileDialog.getSaveFileName(
            self, "Save as .ul", default_out, "UL Images (*.ul)"
        )
        if not out_path:
            return
        if not out_path.lower().endswith(".ul"):
            out_path += ".ul"

        try:
            write_ul_file(out_path, width, height, channels, pixels, compress=True)
        except (UlFormatError, OSError) as e:
            QMessageBox.critical(self, APP_TITLE, f"Could not write .ul file:\n{e}")
            return

        self.load_ul_file(out_path)

    def export_png_dialog(self):
        if self.current_qimage is None:
            QMessageBox.information(self, APP_TITLE, "Open a .ul file first.")
            return

        default_out = os.path.splitext(self.current_path or "image")[0] + ".png"
        out_path, _ = QFileDialog.getSaveFileName(
            self, "Export as PNG", default_out, "PNG Images (*.png)"
        )
        if not out_path:
            return
        if not out_path.lower().endswith(".png"):
            out_path += ".png"

        if not self.current_qimage.save(out_path, "PNG"):
            QMessageBox.critical(self, APP_TITLE, "Failed to save PNG file.")
        else:
            self.status.showMessage(f"Exported to {out_path}")

    # ---------------------------------------------------------- Zoom / display
    def _refresh_display(self):
        if self.current_qimage is None:
            return

        if self.fit_to_window:
            viewport_size = self.scroll_area.viewport().size()
            scaled = self.current_qimage.scaled(
                viewport_size, Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
        else:
            target_size = QSize(
                int(self.current_qimage.width() * self.zoom_factor),
                int(self.current_qimage.height() * self.zoom_factor),
            )
            scaled = self.current_qimage.scaled(
                target_size, Qt.KeepAspectRatio, Qt.SmoothTransformation
            )

        self.image_label.setPixmap(QPixmap.fromImage(scaled))
        self.image_label.resize(scaled.size())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.fit_to_window:
            self._refresh_display()

    def zoom_in(self):
        self.fit_to_window = False
        self.zoom_factor = min(self.zoom_factor * ZOOM_STEP, MAX_ZOOM)
        self._refresh_display()

    def zoom_out(self):
        self.fit_to_window = False
        self.zoom_factor = max(self.zoom_factor / ZOOM_STEP, MIN_ZOOM)
        self._refresh_display()

    def zoom_actual_size(self):
        self.fit_to_window = False
        self.zoom_factor = 1.0
        self._refresh_display()

    def zoom_fit_to_window(self):
        self.fit_to_window = True
        self._refresh_display()


def main():
    app = QApplication(sys.argv)
    window = UlViewerWindow()
    window.show()

    if len(sys.argv) > 1:
        candidate = sys.argv[1]
        if os.path.isfile(candidate):
            window.load_ul_file(candidate)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
