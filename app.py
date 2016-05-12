import os

from flask import Flask
from pygments.lexers import *
import config

__author__ = 'ohaz'

app = Flask(__name__)

lexers = {'python': Python3Lexer, 'nasm': NasmLexer, 'autoit': AutoItLexer,
          'blitzbasic': BlitzBasicLexer, 'blitzmax': BlitzMaxLexer, 'monkey': MonkeyLexer,
          'cpp': CppLexer, 'c': CLexer, 'ini': IniLexer,
          'nginx': NginxConfLexer, 'pacman': PacmanConfLexer, 'css': CssLexer,
          'less': LessCssLexer, 'sass': SassLexer, 'd': DLexer,
          'json': JsonLexer, 'yaml': YamlLexer, 'diff': DiffLexer,
          'c#': CSharpLexer, 'f#': FSharpLexer, 'vbnet': VbNetLexer,
          'erlang': ErlangLexer, 'brainfuck': BrainfuckLexer, 'fortran': FortranLexer,
          'go': GoLexer, 'bnf': BnfLexer, 'glshader': GLShaderLexer,
          'gnuplot': GnuplotLexer, 'postscript': PostScriptLexer, 'haskell': HaskellLexer,
          'vhdl': VhdlLexer, 'hexdump': HexdumpLexer, 'html': HtmlLexer,
          'xml': XmlLexer, 'coffee': CoffeeScriptLexer, 'dart': DartLexer,
          'Javascript': JavascriptLexer, 'typescript': TypeScriptLexer,
          'scala': ScalaLexer, 'commonlisp': CommonLispLexer, 'makefile': MakefileLexer,
          'bbcode': BBCodeLexer, 'tex': TexLexer, 'matlab': MatlabLexer,
          'objectivec': ObjectiveCLexer, 'objectivecpp': ObjectiveCppLexer,
          'swift': SwiftLexer, 'ada': AdaLexer, 'delphi': DelphiLexer,
          'perl': PerlLexer, 'php': PhpLexer, 'prolog': PrologLexer,
          'cython': CythonLexer, 'numpy': NumPyLexer, 'python2': PythonLexer,
          'ruby': RubyLexer, 'rust': RustLexer, 'lua': LuaLexer,
          'bash': BashLexer, 'ps': PowerShellLexer, 'mysql': MySqlLexer,
          'postgres': PostgresLexer, 'sql': SqlLexer, 'tcl': TclLexer,
          'vim': VimLexer, 'http': HttpLexer, 'irc': IrcLogsLexer, 'java': JavaLexer
          }

auth_key = config.auth_key
basepath = os.path.dirname(os.path.realpath(__file__))
app.secret_key = config.secret_key

debug = config.debug
host = config.host
port = config.port
