class Tape:
    BLANC_SYMBOL = " "

    def __init__(self, tape_string=""):
        self.__tape = dict((enumerate(tape_string)))

    def __str__(self):
        s = ""
        for key, value in self.__tape.items():
            s += value
        return s

    def __getitem__(self, index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.BLANC_SYMBOL

    def __setitem__(self, pos, char):
        self.__tape[pos] = char


class TuringMachine:
    def __init__(
        self, tape="", initial_state="", final_states=None, transition_functions=None
    ):
        self.__tape = Tape(tape)
        self.__head_position = 0
        self.__current_state = initial_state
        self.state_accepted = False
        if transition_functions is None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_functions
        if final_states is None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)

    def get_tape(self):
        return str(self.__tape)

    def make_step(self):
        current_symbol = self.__tape[self.__head_position]
        state = (self.__current_state, current_symbol)
        print(
            f"{str(self.__tape)[:self.__head_position]}"
            f"{state[0]}{str(self.__tape)[self.__head_position:]}"
        )
        if state in self.__transition_function:
            next_state = self.__transition_function[state]
            self.__tape[self.__head_position] = next_state[1]
            if next_state[2] == "R":
                self.__head_position += 1
            elif next_state[2] == "L":
                if self.__head_position == 0:
                    self.__head_position = 0
                else:
                    self.__head_position -= 1
            self.__current_state = next_state[0]
        else:
            raise KeyError(self.__transition_function[state])

    def final(self):
        if self.__current_state in self.__final_states:
            print(self.__current_state)
            if self.__current_state == "qa":
                self.state_accepted = True
            return True
        else:
            return False

    def accepted(self):
        return self.state_accepted
