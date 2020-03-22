# -*- coding: utf-8 -*-
import argparse, re
from os import path
from codecs import open

here = path.abspath(path.dirname(__file__))

def install(args):
    if args:
        from deepnlpf.core.plugin_manager import PluginManager
        PluginManager().install(args)
    else:
        print("Wrong command!")
        print("Try the command: deepnlpf --install <name_plugin>")

def uninstall(args):
    if args:
        from deepnlpf.core.plugin_manager import PluginManager
        PluginManager().uninstall(args)
    else:
        print("Wrong command!")
        print("Try the command: deepnlpf --uninstall <name_plugin>")

def api(args):
    if args:
        from deepnlpf.core.api import app, socketio
        if(args == 'start'):
            socketio.run(app, host='127.0.0.1', port=5000)
    else:
        print("Wrong command!")
        print("Try the command: deepnlpf --api start")

def main():
    my_parser = argparse.ArgumentParser(
        prog="deepnlpf",
        description="DeepNLPF Command Line Interface - CLI",
        epilog='🐙 Enjoy the program! :)'
    )

    version_file_contents = open(path.join(here, '_version.py'), encoding='utf-8').read()
    VERSION = re.compile('__version__ = \"(.*)\"').search(version_file_contents).group(1)
    my_parser.version = '🐙 DeepNLPF v' + VERSION

    my_parser.add_argument('-v', '--version',
                           help='show version.',
                           action='version')

    my_parser.add_argument('-install', '--install',
                        help="Command for install plugin.",
                        type=install,
                        action='store')

    my_parser.add_argument('-uninstall', '--uninstall',
                    help="Command for uninstall plugin.",
                    type=install,
                    action='store')

    my_parser.add_argument('-api', '--api',
                        help="Command run api.",
                        type=api,
                        action='store')

    args = my_parser.parse_args()

if __name__ == '__main__':
    main()
