/* Push-Down-Automata for recognizing valid Rubik's Cube Notations */

#include <stdio.h>
#include <string.h>
#include <stack>
#include <map>

#define TOS ss.top()

enum state {
	Q0, Q1
};

enum symbol {
	EOS = '$',
	  U = 'U',
	  D = 'D',
	  L = 'L',
	  R = 'R',
	  F = 'F',
	  B = 'B',
	  M = 'M',
	  x = 'x',
	  y = 'y'
};

enum dir : char {
	BLANK = NULL,
	CCW = '\'',
	ROT = '2'
};

std::map<symbol, symbol> neg =
    {{ U, D },
     { D, U },
     { L, R },
     { R, L },
     { F, B },
     { B, F }};

std::stack<char> ss;
char *tape, *arm1, *arm2;
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
    tape = append(input, EOS);
    tape = strtok(tape, " ");

	arm1 = arm2 = tape;
	printf("%s = %s = %s\n", arm2, arm1, tape);

    ss.push(EOS);
    ss.push(Q0);

	int i = 0;

	/* problem: accepts U (D D) and <odd offset> R R */
    while (tape) {
        if (isterm(TOS)) {
            if (TOS == tape[0]) {
                ss.pop();

				arm2 = arm1;
				arm1 = tape;
                tape = strtok(NULL, " ");
				printf("%s = %s = %s\n", arm2, arm1, tape);

				if (i > 2) ON = true;
				else ++i;
            }
            else error("unmatched token");
        }
        else {
            switch (TOS) {
                case Q0 : {
                    if (ON && tape[0] == *arm2) error("error -> no layer change");

                    ss.pop();
                    ss.push(Q0);
                    ss.push(Q1);
                    ss.push(tape[0]);
                    break;
                }
                case Q1 : {
					printf("---%s and %s\n", tape, arm1);
                    if (tape != arm1) {
                        ss.pop();
                        ss.push(tape[0]);
                    }
                    else if (tape[0] == neg[(symbol)(*arm2)]) {
                        ss.pop();
                        ss.push(tape[0]);
                    }
                    else error("error -> duplicate token");
                    break;
                }
                default : error("error -> unexpected variable");
            }
        }
    }

    printf("ACCEPTED -> %s\n", input);
}

int main(int argc, char** argv) {
    if (argc == 2) parser(argv[1]);
    else fprintf(stderr, "./%s <string>\n", argv[0]);

    return 0;
}
