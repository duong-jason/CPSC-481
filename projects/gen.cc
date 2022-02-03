#include <stdio.h>
#include <time.h>
#include <map>

class Scrambler {
private:
    struct move_t {
        char s, r;
    } **mov, *prev, *back;

    std::map<char, char> neg =
        {{ 'U', 'D' },
         { 'D', 'U' },
         { 'L', 'R' },
         { 'R', 'L' },
         { 'F', 'B' },
         { 'B', 'F' }};

    int hlen, vlen;
    const char* symbol = "UDLRFB";
    const char* dir = " '2";
    char head;

public:
    Scrambler(const size_t& h, const size_t& v) : hlen(h), vlen(v) {
        srand(time(NULL));
        mov = new move_t*[hlen];
        for (int i = 0; i < hlen; ++i)
            mov[i] = new move_t[2];
    }

    ~Scrambler() {
        for (int i = 0; i < hlen; ++i)
            delete[] mov[i];
        delete[] mov;
    }

    void optimize() {
        int L = 0, R = 0;

        // hand-move-dir
        int table[2][6][3] = {
          //   R  L   F   B   U   D
            { {0}, {}, {}, {}, {}, {} }, // L
            { {}, {}, {}, {}, {}, {} }  // R
        };

    }

    void parse() {
        #define dup (prev->s == (head = symbol[rand() % 6]))
        #define trio (back->s == (neg[prev->s]) && (back->s == head))

        for (int j = 0; j < vlen; ++j) {
            for (int i = 0; i < hlen; ++i) {
                head = symbol[rand() % 6];

                while ((i > 0 && dup) || ((i > 1) && trio));

                mov[i]->s = head;
                mov[i]->r = dir[rand() % 3];

                back = prev;
                prev = mov[i];
            }

            for (int i = 0; i < hlen; ++i) {
                printf("%c%c", mov[i]->s, mov[i]->r);
                if (mov[i]->r != ' ') printf(" ");
            }
            printf("\n");
        }

    }
};

int main(int argc, char** argv) {
    Scrambler scramble(atoi(argv[1]), atoi(argv[2]));
    scramble.parse();
}
