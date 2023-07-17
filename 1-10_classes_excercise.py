# Don't delete this!
from testme import *
import re

# Create a URLIndicator subclass of Indicator
class URLIndicator(Indicator):
    
    def __init__(self, value):
        super().__init__(value)
        
            
    # Modify the defang() method to not just bracket dots, but replace http with hxxp in the URL scheme.
    def defang(self) -> str:
        """
        Modify the defang() method to not just bracket dots, but replace http with hxxp in the URL scheme.
        """
        return self.value.replace(".","[.]").replace("http","hxxp").replace("https","hxxps")
    


evil_url = URLIndicator("https://www.evil.com/yourehacked/")
print(evil_url.defang())


# Send the evil_url to testme(). Leave the other args alone.
testme(evil_url, Indicator, URLIndicator)
