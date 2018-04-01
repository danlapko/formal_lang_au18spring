#!/usr/bin/env bash
cd /usr/local/lib
wget http://www.antlr.org/download/antlr-4.6-complete.jar
export CLASSPATH=".:/usr/local/lib/antlr-4.6-complete.jar:$CLASSPATH"
alias antlr4='java -jar /usr/local/lib/antlr-4.6-complete.jar'
alias grun='java org.antlr.v4.gui.TestRig'
cd -
pip3 install -r requirements.txt