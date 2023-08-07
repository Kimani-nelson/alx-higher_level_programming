#!/usr/bin/python3
#!/bin/bash

# Check if $PYFILE is set
if [ -z "$PYFILE" ]; then
    echo "Error: Environment variable \$PYFILE is not set."
    exit 1
fi

# Check if the file exists
if [ ! -f "$PYFILE" ]; then
    echo "Error: Python file \"$PYFILE\" not found."
    exit 1
fi

# Run the Python script
python "$PYFILE"

