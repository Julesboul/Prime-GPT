class EmptyFileException(Exception):
    """
        Raise this exception if the file is empty (no word in it)
    """
    pass

class NoExtensionException(Exception):
    """
        Raise if there is no extension in the file name
    """
    pass

class NotAllowedExtensionException(Exception):
    """
        Raise if the extension is not support by the app
    """
    pass

class FormatNotAcceptedException(Exception):
    """
        Raise if the format asked does not exist
    """
    pass

class NoFileException(Exception):
    """
        Raise when there is no file in the request
    """
    pass