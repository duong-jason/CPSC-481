/* Push-Down-Automata for recognizing valid Rubik's Cube Notations */

#include <stdio.h>
#include <string.h>
#include <stack>
#include <map>

#define EOS '$'
#define TOS ss.top()

enum nonterminal_t { S = 'S', V = 'V' };

struct token_t {
    enum symbol_t { U = 'U', D = 'D', L = 'L', R = 'R', F = 'F', B = 'B', M = 'M', x = 'x', y = 'y' } symbol;
    enum dir_t { BLANK = 0, CCW = '\'', ROT = '2' } dir;
};

std::map<char, char> neg =
    {{ 'U', 'D' },
     { 'D', 'U' },
     { 'L', 'R' },
     { 'R', 'L' },
     { 'F', 'B' },
     { 'B', 'F' }};

std::stack<char> ss;
char* bufp;
char save;
bool ON = false;

char* append(const char* const w, const char& c) {
    size_t len = strlen(w);
    char* r = new char[len + 3];

    strcpy(r, w);

    r[len] = ' ';
    r[len+1] = c;
    r[len+2] = '\0';

    return r;
}

bool isTerminal(const char& c) {
    const char* pattern = "$/U/D/L/R/F/B/M/x/y/";
    const size_t len = strlen(pattern);

    for (size_t pos = 0; pos < len; pos += 2)
        if (c == *(pattern + pos)) return true;
    return false;
}

void error(const char* status) {
    printf("%s\n",status);
    exit(1);
}

void parser(char* input) {
    bufp = append(input, EOS);
    bufp = strtok(bufp, " ");

    ss.push('$');
    ss.push('S');

    while (!ss.empty() && bufp) {
        if (isTerminal(TOS)) {
            if (TOS == bufp[0]) {
                ss.pop();
                bufp = strtok(NULL, " ");
            }
            else error("unmatched token");
        }
        else {
            switch (TOS) {
                case 'S' : {
                    if (ON && bufp[0] == save) error("no layer change");

                    ON = false;
                    save = bufp[0];

                    ss.pop();
                    ss.push('S');
                    ss.push('V');
                    ss.push(bufp[0]);

                    break;
                }
                case 'V' : {
                    if (bufp[0] == neg[save]) {
                        ON = true;
                        ss.pop();
                        ss.push(bufp[0]);
                    }
                    else if (bufp[0] != save) {
                        ss.pop();
                        ss.push(bufp[0]);
                    }
                    else error("duplicate token");

                    break;
                }
                default : error("unexpected variable");
            }
        }
    }

    printf("ACCEPTED\n");
}

int main(int argc, char** argv) {
    if (argc == 2) parser(argv[1]);
    else fprintf(stderr, "./%s <string>", argv[0]);

    return 0;
}
