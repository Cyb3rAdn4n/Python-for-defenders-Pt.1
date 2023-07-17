class Indicator:
    """
    Atomic Indicators of Compromise.
    
    Parameters
    ----------
    
    value: str
        Value of indicator
    """
    
    def __init__(self, value):
        self.value: str = value
        
    def defang(self) -> str:
        """
        Defangs the indicator
        
        Implemented in subclasses
        """
        pass
    
# Notice the parens? Parens for Parents!
class IPv4Indicator(Indicator):
    
    def __init__(self, value):
        # Instantiate parent properties/methods
        super().__init__(value)
        
    # Overwrite the `defang()` method for our purposes
    def defang(self) -> str:
        """
        Defangs the indicator
        
        Brackets the dots
        """
        return self.value.replace(".", "[.]")
    
# Notice the parens? Parens for Parents!
class DomainIndicator(Indicator):
    
    def __init__(self, value):
        # Instantiate parent properties/methods
        super().__init__(value)
        
    # Overwrite the `defang()` method for our purposes
    def defang(self) -> str:
        """
        Defangs the indicator
        
        Brackets the dots
        """
        return self.value.replace(".", "[.]")
    


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
