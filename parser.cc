/* Push-Down-Automata for recognizing valid Rubik's Cube Notations */

#include <stdio.h>
#include <string.h>
#include <stack>
#include <map>

#define TOS ss.top()

enum state : char { Q0, Q1 };
enum symbol : char { EOS = '$', U = 'U', D = 'D', L = 'L', R = 'R', F = 'F', B = 'B', M = 'M', x = 'x', y = 'y' };
enum dir : char { BLANK = NULL, CCW = '\'', ROT = '2' };

std::map<symbol, symbol> neg =
    {{ U, D },
     { D, U },
     { L, R },
     { R, L },
     { F, B },
     { B, F }};

std::stack<char> ss;
char *bufp;
char save;
bool ON = false;

char* append(const char* const out, const char& c) {
    const size_t len = strlen(out);
    char* const in = new char[len + 3];

    strcpy(in, out);

    in[len] = ' ';
    in[len+1] = c;
    in[len+2] = '\0';

    return in;
}

bool isterm(const char& c) {
    const char *pattern = "$UDLRFBMxy", *ptr = pattern;
    size_t len = strlen(pattern);

    while (len-- > 0) {
        if (*ptr++ == c) return true;
    }
    return false;
}

void error(const char* status) {
    printf("%s\n",status);
    exit(1);
}

void parser(const char* const input) {
    bufp = append(input, EOS);
    bufp = strtok(bufp, " ");

    ss.push(EOS);
    ss.push(Q0);

    while (!ss.empty() && bufp) {
        if (isterm(TOS)) {
            if (TOS == bufp[0]) {
                ss.pop();
                bufp = strtok(NULL, " ");
            }
            else error("unmatched token");
        }
        else {
            switch (TOS) {
                case Q0 : {
                    if (ON && bufp[0] == save) error("no layer change");

                    ON = false;
                    save = bufp[0];

                    ss.pop();
                    ss.push(Q0);
                    ss.push(Q1);
                    ss.push(bufp[0]);
                    break;
                }
                case Q1 : {
                    if (bufp[0] == neg[(symbol)save]) {
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

    printf("ACCEPTED -> %s\n", input);
}

int main(int argc, char** argv) {
    if (argc == 2) parser(argv[1]);
    else fprintf(stderr, "./%s <string>", argv[0]);

    return 0;
}
