#!/bin/bash
# This is in support of the chatgpt speech system.
DEBUG=1
debug() {
    [[ -z "$DEBUG" ]] | echo "$@"
}
speechrun(){
    debug "cd chat speech environment"
    cd /home/dee/chatgptspeech
    debug "sourcing activate"
    source bin/activate
    debug "cd git chatgptspeech" 
    cd /home/dee/git/chatgptspeech
    debug "running the chatgptspeech script" 
    python3 speech.py 
    debug "deactivating the environment"
    deactivate
    debug "done, returning"
}
LOG=/tmp/chatgptspeechrun
echo "Chatgpt speech run " >$LOG 2>&1
speechrun >> $LOG 2>&1

