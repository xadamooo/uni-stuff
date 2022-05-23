from turing import TuringMachine
import json

file = json.load(open("states.json"))

initial_state = file["init"]
transition_function = file["states"]
transition_function = {tuple(k.split("|")): v for k, v in transition_function.items()}

final_states = file["final_states"]

alph = {"a", "b", "c", "â", " "}
nums = {x for x in range(100)}
all_keys = []
for key, value in transition_function.items():
    all_keys.append(key[1])

assert len(set(all_keys) - alph - nums) == 0

input_value = input("INPUT: ")
assert len(set(input_value) - set(all_keys)) == 0

t = TuringMachine(
    input_value,
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
