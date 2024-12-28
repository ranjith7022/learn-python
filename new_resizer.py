def new_resizer(max_width, max_height):
    mw,mh = max_width,max_height
    def min_resize(min_width = 0, min_height = 0):
        miw,mih = min_width,min_height
        if(min_width>mw or min_height > mh):
            raise Exception("minimum size cannot exceed maximum size")
        def final_size(x,y):
            return min(mw,max(x,miw)),min(mh,max(y,mih))
        return final_size
    return min_resize