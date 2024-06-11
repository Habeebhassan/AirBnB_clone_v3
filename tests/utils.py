import io
import sys

def clear_stream(stream):
    """
    Clears the contents of the given StringIO stream.
    
    Args:
        stream (StringIO): The stream to clear.
    """
    stream.seek(0)
    stream.truncate(0)

def reset_stream(stream_name='stdout'):
    """
    Resets the specified stream (stdout or stderr) to a new StringIO object.
    
    Args:
        stream_name (str): The name of the stream to reset ('stdout' or 'stderr').
    """
    if stream_name == 'stdout':
        sys.stdout = io.StringIO()
    elif stream_name == 'stderr':
        sys.stderr = io.StringIO()
    else:
        raise ValueError("Invalid stream name. Use 'stdout' or 'stderr'.")
