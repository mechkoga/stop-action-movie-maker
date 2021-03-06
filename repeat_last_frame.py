#!/usr/bin/env python
# repeat_last_frame.py
"""
creates a new set of frame files and .count file with the last frame repeated
the specified number of times
"""

# disable pylint too many locals messages
#pylint: disable=R0914

import argparse
import os
from shutil import copyfile

FILE_TYPE = '.png'     # images will be saved as .png files
COUNT_TYPE = '.count'  # file type for the file containing the image count
LAST_FRAME_REPEAT = 1  # number of times to repeat the first frame on playback
READ_ONLY = 'r'        # read only parameter for opening files
WRITE_ONLY = 'w'       # write only parameter for creating and overwriting files
FIRST_FRAME = 1        # frame number of first file in the sequence
SUCCESS_CODE = 0       # successful processing
CMD_ERROR_CODE = 1     # error with command parameters
CNF_ERROR_CODE = 2     # error occurred in create_new_frameset

def debug(program_name, print_debug_messages, display_text):
    """
    print debugging messages prefixed by the name of the program
    """
    if print_debug_messages:
        print program_name + ':', display_text
    return

def create_new_frameset(input_movie_name, output_movie_name,
                        last_frame_repeat, prog_name, print_dm):
    """
    create a new frameset with the last frame repeat the specified
    number of times
    """

    if last_frame_repeat < 1:
        return CNF_ERROR_CODE, 'last frame repeat must be greater than zero'

    # construct the file name for input file containing the count of images
    # in the movie
    input_count_file_name = input_movie_name + COUNT_TYPE
    debug(prog_name, print_dm, 'input count file name is ' + \
          input_count_file_name)

    # verify the frame count file exists before trying to open it
    if os.path.isfile(input_count_file_name):
        icf = open(input_count_file_name, READ_ONLY)

        # read the number of frames in the moview
        icf_count = int(icf.read())
        debug(prog_name, print_dm, 'frame count is ' + str(icf_count))

        # close the frame count file
        icf.close()

        # loop through the input files and create new output files with the
        # first frame repeat the number of time specified

        input_frame_play_sequence = range(1, icf_count + 1, 1)
        output_frame_sequence_count = 0

        # loop through all the image files
        for i in input_frame_play_sequence:
            # construct the image number used in the file name
            input_frame_sequence_num = str(i).zfill(3)
            # construct the file name
            input_file_name = input_movie_name + "." + \
                              input_frame_sequence_num + FILE_TYPE

            # verify the frame image file exists before trying to copying it
            if os.path.isfile(input_file_name):

                # if this is the last frame, add new frames
                if i == input_frame_play_sequence[-1]:
                    for rep in range(i, i + last_frame_repeat  + 1):
                        output_frame_sequence_count = rep
                        output_frame_sequence_num = str(output_frame_sequence_count).zfill(3)
                        output_file_name = output_movie_name  + "." + \
                                           output_frame_sequence_num + FILE_TYPE
                        debug(prog_name, print_dm, 'copying ' + \
                              input_file_name + ' to ' + output_file_name)
                        copyfile(input_file_name, output_file_name)
                else:
                    # display the frame
                    output_frame_sequence_count += 1
                    output_frame_sequence_num = str(output_frame_sequence_count).zfill(3)
                    output_file_name = output_movie_name  + "." + \
                                       output_frame_sequence_num + FILE_TYPE
                    debug(prog_name, print_dm, 'copying ' + input_file_name + \
                          ' to ' + output_file_name)
                    copyfile(input_file_name, output_file_name)

            # the frame file does not exist: print an error and exit
            else:
                error_message = 'input frame file ' + input_file_name + \
                                ' does not exist: processing stopping'
                return CNF_ERROR_CODE, error_message

    # the frame count file does not exist: print an error message
    else:
        error_message = 'can not open input frame count file ' + \
                        input_count_file_name
        return CNF_ERROR_CODE, error_message

    # write the output count file

    output_count_file_name = output_movie_name  + COUNT_TYPE
    debug(prog_name, print_dm, 'output count file name is ' + \
          output_count_file_name)

    ocf = open(output_count_file_name, WRITE_ONLY)
    ocf.write(str(output_frame_sequence_count))
    ocf.close()

    debug(prog_name, print_dm, "input .count = " + str(icf_count))
    debug(prog_name, print_dm, "output .count = " + \
          str(output_frame_sequence_count))

    success_message = 'new frame set ' + output_movie_name  + \
                      ' with last frame repeated ' + str(last_frame_repeat) + \
                      ' times successfully created'
    return SUCCESS_CODE, success_message

def main():
    """
    main program execution starts here
    """
    # extract the parameters specified on the command line
    parser = argparse.ArgumentParser(description='Create frame set with the last frame repeated')
    parser.add_argument('input_movie_name',
                        help='file name of the input stop action movie')
    parser.add_argument('output_movie_name',
                        help='file name of the output stop action movie')
    parser.add_argument('-r', '--lastframerepeat', dest='last_frame_repeat',
                        default=LAST_FRAME_REPEAT, type=int,
                        help='number of times to repeat the last frame')
    parser.add_argument('-d', '--debug', dest='debug_switch',
                        action='store_true', help='display debugging messages')
    args = parser.parse_args()

    # save the values from the command parser
    prog_name = parser.prog.rsplit(".", 1)[0]        # remove the .py from the program name
    print_dm = args.debug_switch

    # display the command parameters if debug is turned on
    debug(prog_name, print_dm, 'input movie name is ' + args.input_movie_name)
    debug(prog_name, print_dm, 'output movie name is ' + args.output_movie_name)
    debug(prog_name, print_dm, 'number of times to repeat the last frame is ' + \
          str(args.last_frame_repeat))
    debug(prog_name, print_dm, 'debug is set to ' + str(print_dm))

    # create the new frame set with the last frame repeated
    _, return_message = create_new_frameset(args.input_movie_name,
                                            args.output_movie_name,
                                            args.last_frame_repeat,
                                            prog_name,
                                            print_dm)
    print return_message

# command line execution starts here
if __name__ == "__main__":
    main()
