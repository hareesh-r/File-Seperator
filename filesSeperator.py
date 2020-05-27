import os
from pathlib import Path
subcategory={
    'DOCUMENTS':['.pdf','.txt','.doc'.'rtf','.pptx','.docx'],
    'AUDIO':['.mp3','.m4b','.m4a'],
    'VIDEOS':['.mov','.avi','.mp4'],
    'IMAGES':['.jpg','.jpeg','.raw','.png']
}
def pickCategory (value):
    for name,ext in subcategory.items():
        for exte in ext:
            if exte == value:
                return name
    return 'MISC'
def organizeDir():
    for i in os.scandir():
        if i.is_dir():
            continue
        filepath=Path(i)
        filetype=filepath.suffix.lower()
        diectory = pickCategory(filetype)
        dirpath=Path(diectory)
        if dirpath.is_dir() !=True:
            dirpath.mkdir()
        filepath.rename(dirpath.joinpath(filepath))

organizeDir()