from guizero import App, Box, PushButton, Picture
import gpio_controller

BACKGROUND_COLOR = "#c0cfb2"
TEXT_COLOR = "#333333"
SELECTED_COLOR = "#8ba888"
BUTTON_WIDTH = 8
BUTTON_HEIGHT = 4
BUTTON_TEXT_SIZE = 20

intensity = None
size = None

def close(event):
  if (event.key == "q"):
    app.destroy()

def create_button(parent, command, text):
  button = PushButton(parent, command=command, text=text, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
  button.text_color = TEXT_COLOR
  button.text_size = BUTTON_TEXT_SIZE
  button.tk.config(borderwidth=0, highlightthickness=0)
  return button

def select_intensity(selected_intensity):
  global intensity
  if intensity:
    intensity.bg = BACKGROUND_COLOR
  intensity = selected_intensity
  selected_intensity.bg = SELECTED_COLOR

def select_size(selected_size):
  global size
  if size:
    size.bg = BACKGROUND_COLOR
  size = selected_size
  selected_size.bg = SELECTED_COLOR

def start():
  left.hide()
  right.hide()
  making.show()
  gpio_controller.make_matcha(intensity.text, size.text)

gpio_controller.setup()

app = App("My-Cha", layout="grid", height=500, width=500, bg=BACKGROUND_COLOR)

app.tk.columnconfigure(0, weight=1)
app.tk.columnconfigure(1, weight=1)
app.tk.columnconfigure(2, weight=1)

left = Box(app, grid=[0,0], layout="auto")
middle = Box(app, grid=[1,0], layout="auto")
right = Box(app, grid=[2,0], layout="auto")
making = Box(app, grid=[0,0,3,1], layout="auto", visible=False)

start_button = PushButton(middle, command=start, image="assets/matcha.png", width=300, height=300)
start_button.tk.config(borderwidth=0, highlightthickness=0)
start_button.tk.pack(pady=150)

intensity_1_button = create_button(left, command=lambda: select_intensity(intensity_1_button), text="Mild")
intensity_2_button = create_button(left, command=lambda: select_intensity(intensity_2_button), text="Regular")
intensity_3_button = create_button(left, command=lambda: select_intensity(intensity_3_button), text="Strong")

size_1_button = create_button(right, command=lambda: select_size(size_1_button), text="Small")
size_2_button = create_button(right, command=lambda: select_size(size_2_button), text="Medium")
size_3_button = create_button(right, command=lambda: select_size(size_3_button), text="Large")

making_matcha_image = Picture(making, image="assets/making_matcha.png")

select_intensity(intensity_2_button)
select_size(size_2_button)

app.when_key_pressed = close
app.set_full_screen()
app.display()
