# WMA To MP3

Script used to convert multiple WMA files to MP3 format.

## Requirements

ffmpeg  library is required, to install it on Ubuntu and its derivates execute the next command
```
sudo apt-get install ffmpeg
```

## Usage
The input argument is the folder where the wma files to be converted to mp3 are located. The mp3 files will be created in the same folder.
```
python3 wma2mp3.py <folder>
```

Inside the script, LOG_LEVEL constant indicates the logging level used by the library ffmpeg. Common values are:

|Value|Description|
|---|---|
|quiet|Show nothing at all.|
|fatal|Only show fatal errors.|
|error|Show all errors, including ones which can be recovered from.|
|warning|Show all warnings and errors.|
|info|Show informative messages during processing.|

## Licensing

This project is licensed under the [MIT](https://github.com/ivan-iglesias/wma-to-mp3/LICENSE) License.
