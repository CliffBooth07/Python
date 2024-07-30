import turtle
import pandas

screen = turtle.Screen()
pic = "blank_states_img.gif"
screen.title("State Guess")
screen.addshape(pic)
turtle.shape(pic)
data = pandas.read_csv("50_states.csv")
# screen.tracer(0)

state_gussed = []
while len(state_gussed) < 50:
    screen.update()
    user_input = screen.textinput(f"{len(state_gussed)}/50 Guess States", "Enter states names?").title()
    list_state = data.state.to_list()

    if user_input == "Exit":
        state_remaining = [s for s in list_state if s not in state_gussed]
        # for s in list_state:
        #     if s in state_gussed:
        #         pass
        #     else:
        #         state_remaining.append(s)
        remain = {
            "state": state_remaining
        }
        data = pandas.DataFrame(remain)
        data.to_csv("Unguessed_State.csv")
        break

    if user_input in list_state:
        state_gussed.append(user_input)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        us_state = data[data.state == user_input]
        t.goto(int(us_state.x), int(us_state.y))
        t.write(us_state.state.item(), font=('Arial', 6, 'normal'))
    else:
        pass
