# Other Tkinter Widgets

## What I Learned

This lesson introduced more Tkinter widgets and helped me understand how GUI programs handle different types of user interaction.

Instead of memorising every widget, I focused on understanding:
- what each widget is used for
- how widgets interact with functions
- and how Tkinter responds to user actions

---

# Widgets I Learned

## Text Widget

```python
Text()
```

A multi-line text input box.

Useful for:
- notes
- messages
- larger text input

---

## Spinbox

```python
Spinbox()
```

A number selector with up and down controls.

Useful for:
- counters
- selecting small ranges of numbers

---

## Scale

```python
Scale()
```

A slider widget.

Useful for:
- volume controls
- brightness sliders
- choosing values within a range

---

## Checkbutton

```python
Checkbutton()
```

A checkbox that can be:
- on (`1`)
- off (`0`)

Usually connected to:

```python
IntVar()
```

which helps Tkinter track the checkbox state.

---

## Radiobutton

```python
Radiobutton()
```

Used when the user should only choose ONE option from multiple choices.

Example:
- small
- medium
- large

Only one option can be selected at a time.

---

## Listbox

```python
Listbox()
```

Displays a list of selectable items.

Useful for:
- menus
- song lists
- selectable options

---

# Important Tkinter Pattern

A lot of Tkinter widgets use the same ideas repeatedly:

- `.get()` → retrieve current value
- `command=` → run a function when an event happens
- `.pack()` → place widget on screen

---

# Important Mental Model

Tkinter programming is mostly:

1. User interacts with widget
2. Event happens
3. Function runs
4. Program updates something

This is called event-driven programming.

---

# About IntVar()

```python
IntVar()
```

is a special Tkinter variable that tracks integer values automatically.

Example:
- checkbox checked → `1`
- checkbox unchecked → `0`

---

# Important Reminder

I do NOT need to memorise every Tkinter widget.

The important thing is understanding:
- widget purpose
- event flow
- user interaction
- and how widgets connect to functions

Most syntax can always be checked in the documentation later.

---

# Personal Reflection

This lesson made Tkinter feel more advanced because widgets are now interacting with each other and responding to user actions.

I’m starting to understand how GUI applications actually work behind the scenes.