#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import time
import PySimpleGUI as sg
import tkinter as tk
from skimage import io
from skimage.external.tifffile import TiffFile
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.backends.tkagg as tkagg
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from PIL import Image
from PIL.TiffTags import TAGS

# Using TiffCapture
# tiff = tc.opentiff(tiff_file)
# plt.imshow(tiff.read()[1])
# plt.show()
# tiff.release()


def draw_figure(canvas, figure, loc=(0, 0)):
    """ Draw a matplotlib figure onto a Tk canvas
    loc: location of top-left corner of figure on canvas in pixels.
    Inspired by matplotlib source: lib/matplotlib/backends/backend_tkagg.py
    """
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)
    return photo


def tiff_viewer():
    # Use a GUI to get the patient data .csv
    # TODO: Add progress bar for loading
    tiff_file = sg.PopupGetFile('Choose video file (.tif/.tiff) to open:')
    if tiff_file is None:
        quit()
    sg.Popup('Results', 'The value returned from PopupGetFile', tiff_file)

    # Using skimage aka scikit-image from SciPy
    video_file = io.imread(tiff_file)
    with TiffFile(tiff_file) as tif:
        # image_stack = tif.asarray()
        for page in tif.pages:
            for tag in page.tags.values():
                tag_name, tag_value = tag.name, tag.value
            image = page.asarray()

    video_shape = video_file.shape
    num_frames = video_file.shape[0]
    print('video shape: ', video_shape)
    print('Width x Height: ', video_file.shape[1], video_file.shape[2])
    print('# of Frames: ', num_frames)
    # show the image
    plt.figure(1)
    plt.imshow(video_file[0], cmap='gray')
    plt.axis('off')
    # plt.show()

    # define the window layout
    layout = [[sg.Text('TIFF Video Viewer', size=(15, 1), pad=((510, 0), 3), justification='center', font='Helvetica 20')],
              [sg.Canvas(size=(600, 600), key='canvas')],
              # [sg.Image(filename='', key='image')],
              [sg.Slider(range=(1, num_frames), size=(115, 10), orientation='h', key='frame_slider')],
              [sg.Button('Exit', size=(10, 2), pad=((600, 0), 3), font='Helvetica 14')]]

    # create the window
    window = sg.Window('Tiff Viewer', no_titlebar=False).Layout(layout)
    window.Layout(layout).Finalize()

    # Start main GUI window
    while True:
        event, values = window.Read(timeout=5)        # Poll every 100 ms
        if event is 'Exit' or event is None:
            exit(69)
        frame_current = int(values['frame_slider'])
        # print('Current frame #', frame_current)

        image_current = video_file[frame_current-1]
        canvas = window.FindElement('canvas').TKCanvas
        fig = plt.gcf()
        plt.imshow(image_current, cmap='gray')
        fig_photo = draw_figure(canvas, fig)

        # window.FindElement('image').Update(data=image_current)
        # window.FindElement('image').Update(data=videoFile[frame_current])


tiff_viewer()
