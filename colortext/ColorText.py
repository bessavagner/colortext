import sys
import os

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
    def __init__(self, defaultcolor=OKGREEN, std_id=1):
        """ColorText constructor

        Args:
            defaultcolor (str, optional): color in ANSI escape code. Defaults to OKGREEN.
        """
        self.defaultcolor = defaultcolor
        if os.name == 'nt':
            self._windows_enable_ANSI(std_id)
    
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

    def _windows_enable_ANSI(self, std_id):
        """Enable Windows 10 cmd.exe ANSI VT Virtual Terminal Processing."""
        from ctypes import byref, POINTER, windll, WINFUNCTYPE
        from ctypes.wintypes import BOOL, DWORD, HANDLE

        GetStdHandle = WINFUNCTYPE(
            HANDLE,
            DWORD)(('GetStdHandle', windll.kernel32))

        GetFileType = WINFUNCTYPE(
            DWORD,
            HANDLE)(('GetFileType', windll.kernel32))

        GetConsoleMode = WINFUNCTYPE(
            BOOL,
            HANDLE,
            POINTER(DWORD))(('GetConsoleMode', windll.kernel32))

        SetConsoleMode = WINFUNCTYPE(
            BOOL,
            HANDLE,
            DWORD)(('SetConsoleMode', windll.kernel32))

        if std_id == 1:       # stdout
            h = GetStdHandle(-11)
        elif std_id == 2:     # stderr
            h = GetStdHandle(-12)
        else:
            return False

        if h is None or h == HANDLE(-1):
            return False

        FILE_TYPE_CHAR = 0x0002
        if (GetFileType(h) & 3) != FILE_TYPE_CHAR:
            return False

        mode = DWORD()
        if not GetConsoleMode(h, byref(mode)):
            return False

        ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
        if (mode.value & ENABLE_VIRTUAL_TERMINAL_PROCESSING) == 0:
            SetConsoleMode(h, mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING)
        return True
