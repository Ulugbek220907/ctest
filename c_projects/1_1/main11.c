#include <stdio.h>
//it was team project that has given us in school 21 .
void render(int ball_x, int ball_y, int p1_y, int p2_y, int score1, int score2) {
    /* Clears the terminal using ANSI escape codes instead of system() */
    printf("\033[2J\033[H");
    
    for (int y = 0; y < 25; y++) {
        for (int x = 0; x < 80; x++) {
            if (y == 0 || y == 24) {
                printf("-");
            } else if (x == ball_x && y == ball_y) {
                printf("O");
            } else if (x == 4 && (y == p1_y || y == p1_y - 1 || y == p1_y + 1)) {
                printf("|");
            } else if (x == 75 && (y == p2_y || y == p2_y - 1 || y == p2_y + 1)) {
                printf("|");
            } else if (x == 40) {
                printf(".");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }
    printf("Score: Player 1: %d | Player 2: %d\n", score1, score2);
}

int main(void) {
    int ball_x = 40, ball_y = 12;
    int p1_y = 12, p2_y = 12;
    int dir_x = -1, dir_y = 1;
    int score1 = 0, score2 = 0;

    render(ball_x, ball_y, p1_y, p2_y, score1, score2);

    while (score1 < 21 && score2 < 21) {
        int action = getchar();
        
        /* Ignore newlines so the game doesn't jump twice when pressing Enter */
        if (action == '\n') continue;

        /* Input routing and paddle movement */
        if ((action == 'a' || action == 'A') && p1_y > 2) {
            p1_y--;
        } else if ((action == 'z' || action == 'Z') && p1_y < 22) {
            p1_y++;
        } else if ((action == 'k' || action == 'K') && p2_y > 2) {
            p2_y--;
        } else if ((action == 'm' || action == 'M') && p2_y < 22) {
            p2_y++;
        } else if (action == ' ') {
            /* Skip turn, just let the ball move */
        } else {
            /* Invalid input, wait for correct input without advancing game state */
            continue; 
        }

        /* Calculate next ball coordinates */
        int next_x = ball_x + dir_x;
        int next_y = ball_y + dir_y;

        /* Wall collisions (Top/Bottom) */
        if (next_y <= 0 || next_y >= 24) {
            dir_y = -dir_y;
            next_y = ball_y + dir_y;
        }

        /* Paddle collisions */
        if (next_x == 4 && (next_y == p1_y || next_y == p1_y - 1 || next_y == p1_y + 1)) {
            dir_x = -dir_x;
            next_x = ball_x + dir_x;
        } else if (next_x == 75 && (next_y == p2_y || next_y == p2_y - 1 || next_y == p2_y + 1)) {
            dir_x = -dir_x;
            next_x = ball_x + dir_x;
        }

        /* Scoring */
        if (next_x <= 0) {
            score2++;
            ball_x = 40; ball_y = 12;
            dir_x = 1;
        } else if (next_x >= 79) {
            score1++;
            ball_x = 40; ball_y = 12;
            dir_x = -1;
        } else {
            ball_x = next_x;
            ball_y = next_y;
        }

        render(ball_x, ball_y, p1_y, p2_y, score1, score2);
    }

    if (score1 >= 21) {
        printf("\nCongratulations Player 1! You won!\n");
    } else {
        printf("\nCongratulations Player 2! You won!\n");
    }

    return 0;
}
