import sys

class ColorText:
    """ColorText
    class members with mains ANSI escape color code:
    HEADER = '\\033[95m'
    OKBLUE = '\\033[94m'
    OKGREEN = '\\033[92m'
    WARNING = '\\033[93m'
    FAIL = '\\033[91m'
    ENDC = '\\033[0m'
    BOLD = '\\033[1m'
    UNDERLINE = '\\033[4m' 
    Returns:
        class: Color text to be printed on terminal
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    def __init__(self, defaultcolor=OKGREEN):
        """ColorText constructor

        Args:
            defaultcolor (str, optional): color in ANSI escape code. Defaults to OKGREEN.
        """
        self.defaultcolor = defaultcolor
    
    def colorstring(self, string='', color=None, bold=False, endcolor=True):
        """Wraps string with ANSI escape code

        Args:
            string (str, optional): text. Defaults to ''.
            color ([type], optional): color in ANSI escape code. Defaults to None.
            bold (bool, optional): whether to put text in bold fashion. Defaults to False.
            endcolor (bool, optional): whether to close ANSI escape code. Defaults to True.

        Returns:
            str: colored text
        """
        end = self.ENDC
        if color is None:
            color = self.defaultcolor
        if bold:
            color += self.BOLD
        if not endcolor:
            end = ''
        return f'{color}{string}{end}'
    
    def cprint(self, *objects, color=None, bold=False, endcolor=True, **kwargs):
        """Output colored text directly to terminal. Works like
        an override of built-in's print.
    

        Args:
            color (str, optional): ANSI escape color code. Defaults to None.
            bold (bool, optional): whether to put text in bold fashion. Defaults to False.
            endcolor (bool, optional): whether to close ANSI escape code. Defaults to True.

        Returns:
           ColorText object: a ColorTexto object for reuse
        """
        end = self.ENDC
        if color is None:
            color = self.defaultcolor
        if bold:
            color += self.BOLD
        if not endcolor:
            end = ''
        print(color, *objects, end, **kwargs)
        return self
