
def get_size_from_aspect_ratio(aspect_ratio, width=None, height=None):
    """ Given the aspect ratio and length of one of the sides, return the size of the rectangle
    
    If both height and width lenghts are passed, prioritizes width
    """

    if height==None:
        height = (width/aspect_ratio[0]) * aspect_ratio[1]
    elif width==None:
        width = (height/aspect_ratio[1]) * aspect_ratio[0]
    else:
        raise Exception("Either height or width must be specified.")
    return (width, height)
