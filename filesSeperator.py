import os
from pathlib import Path

"""
Download or copy and Paste this cose and save with .py extension and
run inside the folder that you want to segregate
"""
subcategory={

    'DOCUMENTS':['.pdf','.txt','.doc','rtf','.pptx','.docx',
                '.odt'],
    'AUDIO':['.mp3','.m4b','.m4a','.webvtt','.cea-608/708',
            '.dfxp', '.sami', '.scc', '.srt', '.ttml', '.3gpp'],
    'VIDEOS':['.mov','.avi','.mp4''.3gp','.ogg', '.oga', '.ogv',
                '.ogx','.wmv','.webm','.flv','.avi','.QuickTime',
                '.hdv','.mxf','.mpeg-2','.ts','.wav','.lfx',
                '.gfx''.vob'],
    'IMAGES':['.jpg','.jpeg','.raw','.png','.tiff','.gif',],
    'PROGRAMMING FILES':['.htm','.html','.cpp','.c','.py']
}
def findTheCategory (value):
    for filename,ext in subcategory.items():
        for extension in ext:
            if extension == value:
                return filename
    return 'MISC'
def organizeDir():
    for i in os.scandir():
        if i.is_dir():
            continue
        filePath=Path(i)
        fileType=filePath.suffix.lower()
        directory = findTheCategory(fileType)
        directoryPath=Path(directory)
        if directoryPath.is_dir() !=True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDir()