for key in tuple(globals().keys()):
     if (not key.startswith("__")) and (key != "key"):
         globals().pop(key) 
         del key



