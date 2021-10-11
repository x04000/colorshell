# ──────────────────────────────────────────────────────────────────────────────

import sys

# ──────────────────────────────────────────────────────────────────────────────

prompt1 = '\x1b[38;2;76;86;106m\x1b[360m[ '
prompt2 = ' \x1b[38;2;76;86;106m\x1b[360m] \x1b[0m\x1b[0m'

# ──────────────────────────────────────────────────────────────────────────────

def makergb(a:str):

    return tuple(int(a.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

def makex1b(a:tuple):

    return f'\\x1b[38;2;{a[0]};{a[1]};{a[2]}m\\x1b[360m'

# ──────────────────────────────────────────────────────────────────────────────

def inp(a:str):

    return input(
            prompt1 + '\x1b[38;2;235;203;139m\x1b[360m' + a + prompt2
            )

def main(*arg):

    if not arg:

        print('\x1b[38;2;235;203;139m\x1b[360m\n─  Input a hex color code or rgb\n   (rgb color must be separated)\n   example: "0 0 0"\n')
        inp1 = inp('inp1')

    else:

        inp1 = arg

    if len(inp1.split()) == 3:

        inp1 = inp1.split()
        inp1 = (inp1[0], inp1[1], inp1[2])

    if inp1:

        if len(inp1) in (6, 7):

            if len(inp1) == 7:

                inp1 = inp1.lstrip('#')

            result = '\x1b[38;2;208;135;112m\x1b[360m' + makex1b(makergb(inp1))

            if not arg:
                
                print('\n-  ' + result + '\n')

            return result

        elif isinstance(inp1, tuple):

            result = '\x1b[38;2;208;135;112m\x1b[360m' + makex1b(inp1)

            if not arg:

                print('\n-  ' + result + '\n')

            return result
        
        else:

            return main()
        
    else:
        return main()

if __name__ == '__main__':

    try:

        try:

            main()

        except KeyboardInterrupt:

            print('\x1b[38;2;191;97;106m\x1b[360m\nKeyboardInterrupt')

    except:

        print('\x1b[38;2;191;97;106m\x1b[360mUnknow error')

