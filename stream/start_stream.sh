#!/usr/bin/env bash
echo Shutting down mjpg_streamer
pkill mjpg_streamer
echo mjpg_streamer shut down
echo Starting ffmpeg
nohup raspivid -o - -t 0 -fps 30 -b 6000000 | ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://173.194.10.149/live2/$1 > /dev/null 2>ffpmeg_log &
echo Starting ffpmeg