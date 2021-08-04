def convert(number):
    """Convert a number into a string that contains raindrop sounds corresponding 
    to certain potential factors"""
    if number % 3 == 0:
        if number % 5 == 0:
            if number % 7 == 0:
                return "PlingPlangPlong"
            else:
                return "PlingPlang"
        if number % 7 == 0:
            return "PlingPlong"
        else:
            return "Pling"
    if number % 5 == 0:
        if number % 7 == 0:
            return "PlangPlong"
        else:
            return "Plang"
    if number % 7 == 0:
        return "Plong"
    else:
        return str(number)