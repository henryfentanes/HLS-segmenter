import os.path
from collections import OrderedDict

# SEGMENTS DURATION (seconds)
SEGMENT_SIZE = 1

# FFMPEG PRESET [ultrafast,superfast, veryfast, faster, fast, medium, slow, slower, veryslow]
FFMPEG_PRESET = 'slow'

# PRESETS FOR ADAPTATIVE QUALITY
PROFILES = OrderedDict()
PROFILES['1-low'] = {
    'resolutions':  { '4/3': '640x480', '16/9': '640x360' },
    'audiobitrate': '96k',
    'videobitrate': '600k',
    'buffersize':   '1200k',
    'profile':      'baseline',
    'level':        '3.0',
    'fps':          24
}
PROFILES['2-medium'] = {
    'resolutions':  { '4/3': '640x480', '16/9': '640x360' },
    'audiobitrate': '96k',
    'videobitrate': '1200k',
    'buffersize':   '2400k',
    'profile':      'baseline',
    'level':        '3.1',
    'fps':          24
}
PROFILES['3-high'] = {
    'resolutions':  { '4/3': '960x720', '16/9': '960x540' },
    'audiobitrate': '128k',
    'videobitrate': '3500k',
    'buffersize':   '7000k',
    'profile':      'main',
    'level':        '3.1',
    'fps':          24
}
PROFILES['4-hd'] = {
    'resolutions':  { '4/3': '1280x960', '16/9': '1280x720' },
    'audiobitrate': '128k',
    'videobitrate': '5000k',
    'buffersize':   '10000k',
    'profile':      'main',
    'level':        '3.1',
    'fps':          24
}


def build(inputfile, ratio='16/9', segmentsize=False, ffmpegmode=False):
    presets = PROFILES.copy()
    for quality, profile in presets.items():
        try:
            presets[quality]['resolution'] = profile['resolutions'][ratio]
            presets[quality]['gop'] = presets[quality]['fps'] * SEGMENT_SIZE
            presets[quality]['inputfile'] = inputfile
            presets[quality]['outputname'] = quality
            presets[quality]['segmentsize'] = segmentsize if segmentsize else SEGMENT_SIZE
            presets[quality]['ffmpegmode'] = ffmpegmode if ffmpegmode else FFMPEG_PRESET
        except Exception as e:
            print('Error while building {0} Profile with ratio {1}.. Ignoring'.format(quality, ratio))
            del presets[quality]

    return presets.items()
