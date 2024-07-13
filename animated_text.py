import curses
import time

def main(stdscr):
    # Initialize the curses
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Sample text to display
    text = "Awesome Text Animation!"
    text_length = len(text)
    
    # Get the screen dimensions
    sh, sw = stdscr.getmaxyx()
    
    # Initial position for the text (bottom of the screen)
    x = sw//2 - text_length//2
    y = sh - 1

    # Loop to animate the text
    while True:
        stdscr.clear()
        if y < 0:
            y = sh - 1  # Reset position to bottom of the screen
        stdscr.addstr(y, x, text, curses.A_BOLD)
        stdscr.refresh()
        y -= 1
        time.sleep(0.1)

        # Exit on user input
        if stdscr.getch() != -1:
            break

# Initialize curses
curses.wrapper(main)
