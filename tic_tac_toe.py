from enum import Enum
from kivy.lang import Builder
from kivymd.app import MDApp


class Characters(str, Enum):
    X = str("X")
    O = str("O")


class TicTacToe(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Pink"
        return Builder.load_file("tic_tac_toe.kv")

    # Who's Turn
    current_turn = Characters.X
    game_over = False
    winner = None
    board_state = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]

    def presser(self, btn):
        btn.text = self.current_turn
        btn.disabled = True
        if self.current_turn == Characters.X:
            self.current_turn = Characters.O
        else:
            self.current_turn = Characters.X
        self.root.ids.score.text = f"{self.current_turn}'s Turn!"
        self.update_board(
            x_coordinate=btn.x_coordinate,
            y_coordinate=btn.y_coordinate,
            character=btn.text
        )
        self.evaluate_board()

    def update_board(self, x_coordinate, y_coordinate, character):
        self.board_state[int(y_coordinate)][int(x_coordinate)] = character


    def evaluate_board(self):
        print(self.board_state)
        for horiz_row_index in range(3):
            if (self.board_state[horiz_row_index][0] and self.board_state[horiz_row_index][1] and self.board_state[horiz_row_index][2] in [Characters.X, Characters.O]) and (self.board_state[horiz_row_index][0] == self.board_state[horiz_row_index][1] == self.board_state[horiz_row_index][2]):
                print("Horizontal Victory")
                self.game_over = True
                self.winner = self.board_state[horiz_row_index][0]
        for vertical_column_index in range(3):
            if (self.board_state[0][vertical_column_index] and self.board_state[1][vertical_column_index] and self.board_state[2][vertical_column_index] in [Characters.X, Characters.O]) and (self.board_state[0][vertical_column_index] == self.board_state[1][vertical_column_index] == self.board_state[2][vertical_column_index]):
                print("Vertical Victory")
                self.game_over = True
                self.winner = self.board_state[0][vertical_column_index]
        # Top-Left to Btm-Right diagonal
        if (self.board_state[0][0] and self.board_state[1][1] and self.board_state[2][2] in [Characters.X, Characters.O]) and (self.board_state[0][0] == self.board_state[1][1] == self.board_state[2][2]):
            print("TL-BR Victory")
            self.game_over = True
            self.winner = self.board_state[0][0]
        # Btm-Left to Top-Right diagonal
        if (self.board_state[2][0] and self.board_state[1][1] and self.board_state[0][2] in [Characters.X, Characters.O]) and (self.board_state[2][0] == self.board_state[1][1] == self.board_state[0][2]):
            print("BL-TR Victory")
            self.game_over = True
            self.winner = self.board_state[0][0]


        if self.game_over:
            self.root.ids.btn1.disabled = True
            self.root.ids.btn2.disabled = True
            self.root.ids.btn3.disabled = True
            self.root.ids.btn4.disabled = True
            self.root.ids.btn5.disabled = True
            self.root.ids.btn6.disabled = True
            self.root.ids.btn7.disabled = True
            self.root.ids.btn8.disabled = True
            self.root.ids.btn9.disabled = True
            self.root.ids.score.text = f"{self.winner} Has Won!"
        elif not self.game_over and self.root.ids.btn1.disabled and self.root.ids.btn2.disabled and self.root.ids.btn3.disabled and self.root.ids.btn4.disabled and self.root.ids.btn5.disabled and self.root.ids.btn6.disabled and self.root.ids.btn7.disabled and self.root.ids.btn8.disabled and self.root.ids.btn9.disabled:
            self.root.ids.score.text = f"It's A Tie!"

    def restart(self):
        print("Restarting Game!")
        self.current_turn = Characters.X

        self.root.ids.btn1.disabled = False
        self.root.ids.btn2.disabled = False
        self.root.ids.btn3.disabled = False
        self.root.ids.btn4.disabled = False
        self.root.ids.btn5.disabled = False
        self.root.ids.btn6.disabled = False
        self.root.ids.btn7.disabled = False
        self.root.ids.btn8.disabled = False
        self.root.ids.btn9.disabled = False

        self.root.ids.btn1.text = ""
        self.root.ids.btn2.text = ""
        self.root.ids.btn3.text = ""
        self.root.ids.btn4.text = ""
        self.root.ids.btn5.text = ""
        self.root.ids.btn6.text = ""
        self.root.ids.btn7.text = ""
        self.root.ids.btn8.text = ""
        self.root.ids.btn9.text = ""
        self.root.ids.score.text = "X Goes First!"

        self.game_over = False

        for i in range(3):
            for j in range(3):
                self.board_state[i][j] = ""
        print(self.board_state)
        print(self.root.ids)



TicTacToe().run()
