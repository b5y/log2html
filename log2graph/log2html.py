# -*- coding: utf-8 -*-
import os
import re
import plotly
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go


def get_files(path=basestring):
    if not os.path.isdir(path):
        raise IOError('Object {0} is not a folder'.format(path))
    for dirpath, dirnames, filenames in os.walk(path):
        for file_ in filenames:
            if file_.endswith('.log'):
                yield os.path.join(dirpath, file_)


def read_log_file(filename=basestring):
    if not os.path.isfile(filename):
        raise IOError('Object {0} is not a file'.format(filename))
    if not filename.endswith('.log'):
        raise TypeError('File {0} has inappropriate extension'.format(filename))
    numbers = []
    with open(filename, 'rb') as fd:
        for line in fd:
            if line.startswith('val_loss'):
                numbers.extend(re.findall(r'[-+]?\d*\.\d+|\d+', line))
    return numbers


def get_graph(val_loss=list):
    n = len(val_loss)
    random_x = np.linspace(0, 1, n)
    random_y = val_loss
    trace = go.Scatter(
        x=random_x,
        y=random_y,
        mode='lines+markers',
        name='lines+markers'
    )
    return trace


def draw_graph(filename_or_folder=basestring, off=None, auto_open=False, sharing=basestring):
    if os.path.isfile(filename_or_folder):
        data = [get_graph(read_log_file(filename=filename_or_folder))]
        if not off:
            py.plot(data, filename=filename_or_folder[:-4], auto_open=auto_open, sharing=sharing)
        else:
            plotly.offline.plot(data, filename=filename_or_folder[:-4] + '.html', auto_open=auto_open)
    elif os.path.isdir(filename_or_folder):
        for file_ in get_files(filename_or_folder):
            data = [get_graph(read_log_file(filename=file_))]
            if not off:
                py.plot(data, filename=file_[:-4], auto_open=auto_open, sharing=sharing)
            else:
                plotly.offline.plot(data, filename=file_[:-4] + '.html', auto_open=auto_open)
    else:
        raise IOError('Cannot get access to {0} object'.format(filename_or_folder))
