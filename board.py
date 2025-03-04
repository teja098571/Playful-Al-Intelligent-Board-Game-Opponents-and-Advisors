import tkinter as tk
import random
import time

# Function to handle the dice roll
def roll_dice():
    dice_value = random.randint(1, 6)  # Generate a random number between 1 and 6
    dice_label.config(text=f"Dice Roll: {dice_value}")
    move_player(dice_value)

# Function to move the player based on dice roll
def move_player(dice_value):
    global player_positions, current_player
    initial_position = player_positions[current_player]
    player_positions[current_player] += dice_value  # Move the player according to the dice roll

    # Check if player lands on a snake or ladder
    if player_positions[current_player] in snakes:
        player_positions[current_player] = snakes[player_positions[current_player]]
        message = f"{player_names[current_player]} got bitten by a snake!"
    elif player_positions[current_player] in ladders:
        player_positions[current_player] = ladders[player_positions[current_player]]
        message = f"{player_names[current_player]} climbed a ladder!"
    else:
        message = ""
    
    # Check if player has won the game
    if player_positions[current_player] >= 100:
        player_positions[current_player] = 100
        message = f"Congratulations! {player_names[current_player]} won!"
        # Display win message box
        tk.messagebox.showinfo("Game Over", f"{player_names[current_player]} won the game!")

    # Update the player's position and board
    update_board(initial_position, player_positions[current_player])
    player_pos_label.config(text=f"{player_names[current_player]} Position: {player_positions[current_player]}")
    status_label.config(text=message)

    # Move to the next player
    current_player = (current_player + 1) % len(player_positions)
    turn_label.config(text=f"{player_names[current_player]}'s Turn")

# Function to update the board (smooth transition of the player's position)
def update_board(initial_position, final_position):
    for i in range(initial_position, final_position):
        cell = board_cells[i]
        root.update()  # Update the screen to show smooth movement
        time.sleep(0.05)  # Add a small delay to simulate smooth movement
        cell.config(bg="white")  # Reset previous position to normal

    # Highlight the new position
    new_cell = board_cells[final_position - 1]
    new_cell.config(bg=player_colors[current_player], fg="red", font=("Arial", 12, "bold"))

# Initialize the main game window
root = tk.Tk()
root.title("Snake and Ladder Game")
root.geometry("700x750")
root.resizable(False, False)

# Initialize the player's starting position
player_positions = [1, 1]  # Start both players at position 1
current_player = 0  # Player 1 starts

# Define the positions of snakes and ladders on the board
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Player Names and Colors
player_names = ["Player 1", "Player 2"]
player_colors = ["skyblue", "pink"]  # Player 1 color and Player 2 color

# Set up the UI components
frame = tk.Frame(root)
frame.pack(pady=20)

# Create the "Roll Dice" button with fun design
roll_button = tk.Button(frame, text="Roll Dice", command=roll_dice, font=("Arial", 16), bg="green", fg="black", relief="raised", width=15, height=2)
roll_button.grid(row=0, column=0, padx=10, pady=10)

# Create a label to display the dice roll result
dice_label = tk.Label(frame, text="Dice Roll: ", font=("Arial", 14), fg="blue")
dice_label.grid(row=0, column=1, padx=10, pady=10)

# Create a label to display the player's current position
player_pos_label = tk.Label(frame, text=f"{player_names[current_player]} Position: {player_positions[current_player]}", font=("Arial", 14), fg="blue")
player_pos_label.grid(row=1, column=0, columnspan=2)

# Create a label to display status messages (e.g., "Congratulations", "Oh no!")
status_label = tk.Label(frame, text="", font=("Arial", 12), fg="navy blue")
status_label.grid(row=2, column=0, columnspan=2)

# Create a label to display whose turn it is
turn_label = tk.Label(frame, text=f"{player_names[current_player]}'s Turn", font=("Arial", 14), fg="navy blue")
turn_label.grid(row=3, column=0, columnspan=2)

# Create the board UI (10x10 grid)
board_frame = tk.Frame(root)
board_frame.pack()

# Create the board cells (100 cells for 10x10 grid)
board_cells = []
for i in range(10):
    row = []
    for j in range(10):
        cell = tk.Button(board_frame, text=str(i*10 + j + 1), width=5, height=3, font=("Arial", 10), relief="solid", bg="lightgreen")
        cell.grid(row=i, column=j)
        row.append(cell)
    board_cells.extend(row)

# Update the board to show the player's initial position
update_board(1, player_positions[current_player])

# Run the Tkinter event loop
root.mainloop()
