#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import time
import PySimpleGUI as sg
from skimage import io
from skimage.external.tifffile import TiffFile
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.backends.tkagg as tkagg
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import cv2
from PIL import Image
from PIL.TiffTags import TAGS

# Using TiffCapture
# tiff = tc.opentiff(tiff_file)
# plt.imshow(tiff.read()[1])
# plt.show()
# tiff.release()


def draw_figure(canvas, figure, image, loc=(0, 0)):
    """ Draw a matplotlib figure onto a Tk canvas
    loc: location of top-left corner of figure on canvas in pixels.
    Inspired by matplotlib source: lib/matplotlib/backends/backend_tkagg.py
    """
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    # photo = Tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=image)
    tkagg.blit(image, figure_canvas_agg.get_renderer()._renderer, colormode=2)
    return image


def tiff_viewer():
    # Use a GUI to get the patient data .csv
    # TODO: Add progress bar for loading
    tiff_file = sg.PopupGetFile('Choose video file (.tif/.tiff) to open:')
    if tiff_file is None:
        quit()
    sg.Popup('Results', 'The value returned from PopupGetFile', tiff_file)

    # Using skimage aka scikit-image from SciPy
    videoFile = io.imread(tiff_file)
    with TiffFile(tiff_file) as tif:
        image_stack = tif.asarray()
        for page in tif.pages:
            for tag in page.tags.values():
                tag_name, tag_value = tag.name, tag.value
            image = page.asarray()

    video_shape = image_stack.shape
    num_frames = image_stack.shape[0]
    print('video shape: ', video_shape)
    print('Width x Height: ', image_stack.shape[2], image_stack.shape[1])
    print('# of Frames: ', num_frames)
    # show the image
    plt.imshow(image_stack[0], cmap='gray')
    plt.axis('off')
    plt.show()

    # define the window layout
    layout = [[sg.Text('TIFF Video Viewer', size=(15, 1), pad=((510, 0), 3), justification='center', font='Helvetica 20')],
              # [sg.Canvas(size=(600, 600), key='canvas')],
              [sg.Image(filename='', key='image')],
              [sg.Slider(range=(0, num_frames-1), size=(115, 10), orientation='h', key='frame_slider')],
              [sg.Button('Exit', size=(10, 2), pad=((600, 0), 3), font='Helvetica 14')]]

    # create the window and show it without the plot
    window = sg.Window('Demo Application - OpenCV Integration', no_titlebar=False, location=(0,0)).Layout(layout)
    # window.Layout(layout).Finalize()

    # ---===--- LOOP through video file by frame --- #
    i = 0
    while True:
        event, values = window.Read(timeout=500)        # Poll every 100 ms
        if event is 'Exit' or event is None:
            exit(69)
        frame_current = int(values['frame_slider'])
        print('Current frame #', frame_current)

        # TODO: Display current frame
        imgbytes = cv2.imencode('.tiff', image_stack[frame_current])[1].tobytes()  # ditto
        window.FindElement('image').Update(data=image_stack[frame_current])
        # canvas = window.FindElement('canvas').TKCanvas
        # fig = plt.gcf()
        # draw_figure(canvas, fig, image_stack[frame_current])
        # window.FindElement('image').Update(data=videoFile[frame_current])


tiff_viewer()
