## Ubuntu installation
Install through "sudo ./install.sh" command or do it manually:

Install **ANTLR4** :
```
$ cd /usr/local/lib
$ wget http://www.antlr.org/download/antlr-4.6-complete.jar
$ export CLASSPATH=".:/usr/local/lib/antlr-4.6-complete.jar:$CLASSPATH"
$ alias antlr4='java -jar /usr/local/lib/antlr-4.6-complete.jar'
$ alias grun='java org.antlr.v4.gui.TestRig'
```

Install python requirements (for your python3):
```
pip3 install -r requirements.txt
```

## Building lexer
it will produce `L.py`:
```
antlr4 -Dlanguage=Python3 L.g4
```

## Running the lexer
run.py will read L-program file and produce lexems as output
Example:
```
python3 run.py ./test/correct/minus_mult.l


0) COMMENT('// next line is SUB token', [0,0] .. [0,24])
1) ID('x', [1,0] .. [1,0])      SUB('-', [1,2] .. [3,0])        ID('y', [1,4] .. [5,0])
2) COMMENT('// next line is MUL token', [2,0] .. [2,24])
3) ID('x', [3,0] .. [3,0])      MUL('*', [3,2] .. [5,0])        ID('y', [3,4] .. [7,0])
```

## Tests
 - */correct* contains test programs to test all key words and some corner cases
 - */incorrect* test programs test that invalid syntax cause syntax error
 (attention! some syntax may look like invalid but be valid in real: "12ab" == FLOATING(12)  ID(ab))
