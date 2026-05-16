# Buttons, Entry, and Setting Component Options

## What I Learned

This lesson helped me understand how Tkinter widgets can:
- change properties,
- respond to button clicks,
- and interact with user input.

---

# Widgets

Tkinter GUI components are called widgets.

Examples:
- Label
- Button
- Entry

Each widget is an object with:
- properties/settings
- methods/actions

---

# Changing Widget Properties

Widgets can be updated after creation using `.config()`.

Example:

```python
my_label.config(text="New Text")
```

This changes the label text after the label has already been created.

---

# Important Reminder

When reading code like:

```python
my_label.config(...)
```

always ask:

> Which object is performing the action?

In this case:
- `my_label` is the object
- `.config()` changes the label settings

---

# Buttons

Buttons can trigger functions when clicked.

Example:

```python
button = Button(command=button_clicked)
```

When the button is clicked, Tkinter runs:

```python
button_clicked
```

---

# Important Thing I Learned

This:

```python
command=button_clicked
```

is NOT the same as:

```python
command=button_clicked()
```

## Why?

Using parentheses `()` runs the function immediately.

Without parentheses:
Tkinter stores the function and runs it later when the button is clicked.

---

# Entry Widget

The `Entry` widget creates an input box.

Example:

```python
input = Entry()
```

To get text from the input:

```python
input.get()
```

`.get()` returns the current text inside the entry box.

---

# Challenge I Completed

Goal:
- Type text into the entry box
- Click the button
- Update the label with the typed text

Example logic:

```python
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
```

---

# Program Flow

1. User types text into the entry widget
2. User clicks the button
3. The button triggers a function
4. The function gets text from the entry
5. The label text updates

This is called interactivity.

---

# Mental Drill

Question:

```python
my_label.config(text="Clicked")
```

Which widget changes?

Answer:
- the label changes because `my_label` is calling `.config()`

---

# Personal Reminder

Tkinter programming is mostly:
- widgets
- events
- functions
- updating properties
- and tracking program flow