import colortext.ColorText as ColorText

if __name__ == '__main__':
    ctext = ColorText()

    text = ctext.colorstring("ColorText Python", color=ctext.HEADER)
    text += ctext.colorstring(" class", color=ctext.OKBLUE)

    print(text, '\n')

    print('https://github.com/bessavagner', '\n')

    ctext.cprint("This is a default usage of cprint function")

    print('\n')

    text = ctext.colorstring('affect', color=ctext.WARNING)

    ctext.cprint(f"Of course you can {text} the behavior"
                 f" of {ctext.colorstring('cprint', color=ctext.UNDERLINE)}"
                 f" and override it's color." )

    ctext.cprint("But you can avoid it by passing", endcolor=False, end='')
    ctext.cprint("endcolor=False", color=ctext.OKBLUE, end='')
    ctext.cprint("as parameter.")
