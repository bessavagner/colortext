# The colortext package

The colortext package is a single class named ```ColorText``` with a constructor and two methods:

~~~python
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
def cprint(self, *objects, color=None, bold=False, endcolor=True, **kwargs):
    """Output colored text directly to terminal. Works like


    Args:
        color (str, optional): ANSI escape color code. Defaults to None.
        bold (bool, optional): whether to put text in bold fashion. Defaults to False.
        endcolor (bool, optional): whether to close ANSI escape code. Defaults to True.

    Returns:
        ColorText object: a ColorTexto object for reuse
    """
~~~

The following works on most plataforms, if it don't work on yours, please let me know: bessavagner@gmail.com

```colorstring``` wraps a string with ANSI escape code and ```cprint``` Works like an override of built-in's print.
