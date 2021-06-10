# Usage

This script will set up a handler for every signal type that it can, and then
it simply prints what it receives.

You must use SIGKILL to stop this script.

Simply launch it:

    python3 sig.py

# In Docker

Build the image and then run it:

    docker build -t sig .
    docker run --rm --name sig -it sig

Remember, you'll need to send the process a SIGKILL to exit:

    docker kill sig
