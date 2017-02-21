# stop-action-movie-maker

## Overview

The stop action movie recorder and player are two command line python scripts for creating stop action movies.  As the name implies, *stop-action-recorder.py* is used to record the movie and *stop-action-player.py* is used to play the movie.

***stop-action-recorder.py*** uses the specified webcam to record the movie. Upon start up, the program will capture an frame and display a live view of what is visible on the webcam. When the SPACE key is pressed, the frame will be saved.  That image will be shown as a faint image behind the live image for reference as the next frame is being prepared.

These keys have the following functions:

<kbd>Space</kbd>   Saves a frame

<kbd>g</kbd> Turns the display of a grid on or off

<kbd>ESC</kbd> Exits the program.

The frames are stored as *.png* files with names in the form of *filename.nnn.png* where *filename* is the name provided to the command and *nnn* is the number of the frame.  For example: *testmovie.002.png*.

An additional file named *filename.count* containing the number of frames in the movie is also created.  For example: *testmovie.count*. This file is used by *stop-action-player.py* to play the movie.

The *frame* and *.count* files are stored in the current directory.

***stop-action-player.py*** uses the files created by *stop-action-recorder.py* to play back the movie. The movie will be played until the <kbd>ESC</kbd> key is pressed. The time between frames can be specified on the command line; the default is 0.1 seconds.

When the movie is played, the frame numbers are displayed in the upper left corner of the screen. The display of the frame numbers can be suppressed using the *-s* or *--suspressframetext* options on the command line. The frame numbers can be toggled on and off by pressing the <kbd>f</kbd> key while the movie is playing.

The stop action movie recorder and player are written for python 2.7.x.

## Usage Instructions


### Stop Action Movie Recorder

    $ stop-action-recorder.py -h

    usage: stop-action-recorder.py [-h] [-d] [-g] [-s GRIDSPACING]
                                   [-w WEBCAMNUMBER] [-r]
                                   moviename

    Stop action movie recorder

    positional arguments:
      moviename             file name of the stop action movie

    optional arguments:
      -h, --help            show this help message and exit
      -d, --debug           display debugging messages
      -g, --gridlines       display grid lines
      -s GRIDSPACING, --spacing GRIDSPACING
                            grid spacing (pixels); default is 15 pixels
      -w WEBCAMNUMBER, --webcam WEBCAMNUMBER
                            number of the webcam to use
      -r, --reverseimages   reverses the foreground and background images


### Stop Action Movie Player

    $ python stop-action-player.py -h

    usage: stop-action-player.py [-h] [-t TIMEDELAY] [-s] [-d] moviename

    Stop action movie player

    positional arguments:
      moviename             file name of the stop action movie

    optional arguments:
      -h, --help            show this help message and exit
      -t TIMEDELAY, --timebetweenframes TIMEDELAY
                            time delay between displaying frames (milliseconds)
      -s, --suppressframenumbers
                            suppress display of frame numbers
      -d, --debug           display debugging messages

    
### Usage Examples
Record a movie using webcam 0 and store the frames in files with the name *testmovie*.

    $ python stop-action-recorder.py testmovie

Record a movie using webcam 1 and store the frames in files with the name *testmovie*.

    $ python stop-action-recorder.py testmovie -w 1

Record a movie using webcam 0, display grid lines and space them 25 pixels apart. Note: display of grid lines can be turned on or off from the keyboard by pressing the <kbd>g</kbd> key.

    $ python stop-action-recorder.py testmovie -g -s 25

Record a movie using webcam 0 and store the frames in files with the name *testmovie*. When displaying the images make the live frames fainter than and the previous frame.

    $ python stop-action-recorder.py testmovie -r

Play a movie named *testmovie* using the default delay between frames of a tenth of a second.

    $ python stop-action-player.py testmovie

Play a movie named *testmovie* with a delay between frames of half a second (500 milliseconds).

    $ python stop-action-player.py testmovie -t 500

Play a movie named *testmovie* and suppress the display of the frame numbers. Note: the display of frame numbers can be toggled on and off by pressing the <kbd>f</kbd> key while the movie is playing.

    $ python stop-action-player.py testmovie -s

#### Messages
If *stop-action-recorder.py* is unable to open the webcam, it will display the message:

    cannot open webcam    

If *stop-action-recorder.py* is unable to capture the initial frame, it will display the following message and exit.

    unable to read initial webcam image

If *stop-action-recorder.py* is unable to capture a subsequent frame, it will display the following message and exit.

    unable to read webcam image in loop

If *stop-action-player.py* is unable to open the frame count file, it will display a message like the one below and exit:

    can not open frame count file testmovie.count

If *stop-action-player.py* is unable to open one of the frame files, it will display a message like the one below and exit:

    frame file testmovie.001.png does not exist

## Installation Instructions

The *stop-action-movie-maker* python programs requires the the OpenCV for Python CV2 library for Python 2 to be installed. 

After installing CV2 for your operating system, change to the directory where you want the *stop-action-movie-maker* files to be installed.

Install the *stop-action-movie-maker* files by cloning this repository with this command:

    $ git clone https://github.com/makeralchemy/stop-action-movie-maker

Make your first stop action movie with the command:

    $ python stop-action-recorder.py testmovie

## License
This project is licensed under the MIT license.
