from turing import TuringMachine

initial_state = "q0"
transition_function = {
    ("q0", "a"): ("q1", "â", "R"),
    ("q0", " "): ("qr", " ", "L"),
    ("q1", " "): ("qa", " ", "L"),
    ("q1", "b"): ("q1", "b", "R"),
    ("q1", "a"): ("q2", "a", "L"),
    ("q2", "b"): ("q2", "b", "L"),
    ("q2", "â"): ("q3", "â", "L"),
    ("q3", "b"): ("q4", "b", "R"),
    ("q3", "a"): ("q4", "a", "R"),
    ("q3", "â"): ("q4", "â", "R"),
    ("q3", " "): ("q6", " ", "L"),
    ("q4", " "): ("qr", " ", "L"),
    ("q4", "b"): ("q4", "b", "R"),
    ("q4", "a"): ("q5", "b", "R"),
    ("q5", "b"): ("q5", "b", "R"),
    ("q5", " "): ("qr", " ", "L"),
    ("q5", "a"): ("q3", "b", "R"),
    ("q6", "a"): ("q6", "a", "L"),
    ("q6", "b"): ("q6", "b", "L"),
    ("q6", "â"): ("q1", "â", "R"),
}

final_states = {"qr", "qa"}

t = TuringMachine(
    "aaaaaa",
    initial_state=initial_state,
    final_states=final_states,
    transition_functions=transition_function,
)

print("Input on Tape:\n" + t.get_tape())

while not t.final():
    t.make_step()

print("Result of the Turing machine calculation:")
print(t.get_tape())
print(t.accepted())
