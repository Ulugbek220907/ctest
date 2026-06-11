#include <ncurses.h>
#include <unistd.h>

void render_interactive(int ball_x, int ball_y, int p1_y, int p2_y, int score1, int score2) {
    clear();
    
    /* Draw Top and Bottom Borders */
    for (int x = 0; x < 80; x++) {
        mvprintw(0, x, "-");
        mvprintw(24, x, "-");
    }
    
    /* Draw Middle Net */
    for (int y = 1; y < 24; y++) {
        mvprintw(y, 40, ".");
    }
    
    /* Draw Paddle 1 */
    mvprintw(p1_y - 1, 4, "|");
    mvprintw(p1_y, 4, "|");
    mvprintw(p1_y + 1, 4, "|");
    
    /* Draw Paddle 2 */
    mvprintw(p2_y - 1, 75, "|");
    mvprintw(p2_y, 75, "|");
    mvprintw(p2_y + 1, 75, "|");
    
    /* Draw Ball */
    mvprintw(ball_y, ball_x, "O");

    /* Draw Score */
    mvprintw(25, 28, "Score: Player 1: %d | Player 2: %d", score1, score2);
    
    refresh();
}

int main(void) {
    int ball_x = 40, ball_y = 12;
    int p1_y = 12, p2_y = 12;
    int dir_x = -1, dir_y = 1;
    int score1 = 0, score2 = 0;

    /* Initialize ncurses environment */
    initscr();
    cbreak();
    noecho();
    keypad(stdscr, TRUE);
    nodelay(stdscr, TRUE);
    curs_set(0);

    while (score1 < 21 && score2 < 21) {
        int action = getch();

        if (action != ERR) {
            if ((action == 'a' || action == 'A') && p1_y > 2) {
                p1_y--;
            } else if ((action == 'z' || action == 'Z') && p1_y < 22) {
                p1_y++;
            } else if ((action == 'k' || action == 'K') && p2_y > 2) {
                p2_y--;
            } else if ((action == 'm' || action == 'M') && p2_y < 22) {
                p2_y++;
            }
        }

        /* Calculate next ball coordinates */
        int next_x = ball_x + dir_x;
        int next_y = ball_y + dir_y;

        /* Wall collisions */
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

        render_interactive(ball_x, ball_y, p1_y, p2_y, score1, score2);
        
        /* 50ms delay for a playable game speed */
        usleep(50000); 
    }

    /* End game state */
    clear();
    if (score1 >= 21) {
        mvprintw(12, 32, "Player 1 Wins!");
    } else {
        mvprintw(12, 32, "Player 2 Wins!");
    }
    refresh();
    
    /* Keep the win screen up for 3 seconds before closing */
    usleep(3000000); 

    endwin();
    return 0;
}