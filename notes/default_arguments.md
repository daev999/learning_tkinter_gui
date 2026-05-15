# Default Arguments in Python

## Main Idea

Functions can have default values for parameters.

This makes some arguments optional when calling the function.

---

## Basic Example

```python
def greet(name="David"):
    print(f"Hello {name}")
```

If no value is passed in, `"David"` becomes the default value.

---

## Why This Matters

Default values make functions easier to use because you don't always need to provide every argument.

---

## Tkinter Connection

```python
my_label.pack(side="left")
```

The `pack()` method can accept optional keyword arguments like `side`.

Some parameters already have default values behind the scenes.

---

## What Confused Me

I thought every function parameter had to be manually provided.

I was confused because `pack()` accepted arguments that were not immediately visible.

---

## What Finally Clicked

Functions can already contain built-in default behaviour.

Only required arguments must always be provided.

---

## Important Difference

### Required Argument

```python
def greet(name):
```

`name` must be provided.

### Optional Argument

```python
def greet(name="David"):
```

`name` already has a default value.

---

## Personal Reminder

When reading documentation:
- arguments with `=` usually already have default values
- arguments without defaults are usually required