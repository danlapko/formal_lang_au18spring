from antlr4 import *
import sys
import argparse

from L import L as Lexer


def end_of_token_position(start_line, start_column, text):
    lines = text.splitlines()

    end_line = start_line + len(lines) - 1
    end_column = len(lines[-1]) - 1

    if end_line == start_line:
        end_line += start_column

    return end_line, end_column


def output(lexer):
    tokens = lexer.getAllTokens()
    token_names = lexer.ruleNames

    last_line = -1
    for token in tokens:

        token_name = token_names[token.type - 1]
        text = token.text
        tok_start_line = token.line - 1
        tok_start_column = token.column

        tok_end_line, tok_end_column = end_of_token_position(tok_start_line, tok_start_column, text)

        if token_name == "FLOATING":
            text = float(text)

        if last_line != tok_start_line:
            last_line = tok_start_line
            print("\n" + str(last_line) + ") ", end="")

        print('{name}({text}, [{st_line},{st_col}] .. [{end_line},{end_col}])'.format(
            name=token_name,
            text="'"+text+"'" if token_name!= "FLOATING" else text,
            st_line=tok_start_line,
            st_col=tok_start_column,
            end_line=tok_end_line,
            end_col=tok_end_column), end="\t")
    print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='L-program file name')
    args = parser.parse_args()

    file_stream = FileStream(args.file)
    lexer = Lexer(file_stream)


    class MyErrorListener:
        def syntaxError(self, recognizer, offendingSymbol, line, charPositionInLine, msg, exc):
            print('Syntax error at ({line}:{char}): {msg}'.format(line=line - 1,
                                                                  char=charPositionInLine,
                                                                  msg=msg))
            sys.exit(1)


    lexer.removeErrorListeners()
    lexer.addErrorListener(MyErrorListener())

    output(lexer)
