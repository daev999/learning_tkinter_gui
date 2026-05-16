# *args and **kwargs in Python

## What I Learned

This lesson helped me understand the difference between positional arguments and keyword arguments in Python.

---

# Positional Arguments

Positional arguments depend on order.

```python
def greet(name, age):
    print(name, age)

greet("David", 20)
```

Python matches:
- first value → first parameter
- second value → second parameter

## Important Reminder

Function argument matching is NOT the same as list or tuple indexing.

Python simply matches values from left to right.

This:

```python
greet("David", 20)
```

does NOT mean:
- index `0`
- index `1`

It simply means:
- first argument
- second argument

---

# Keyword Arguments

Keyword arguments use names instead of positions.

```python
greet(name="David", age=20)
```

Order does not matter because Python matches using keywords.

---

# *args

`*args` allows a function to accept many positional arguments.

Python packs them into a tuple.

Example:

```python
def add(*args):
    total = 0

    for n in args:
        total += n

    return total
```

Calling:

```python
add(1, 2, 3)
```

turns `args` into:

```python
(1, 2, 3)
```

## Important Things I Learned

- `*args` creates a tuple
- tuples can be looped through
- positions still matter
- accumulator variables need a starting value

---

# Accumulator Pattern

```python
total = 0

for n in args:
    total += n
```

The variable keeps updating as the loop runs.

This pattern is used a lot in programming.

---

# **kwargs

`**kwargs` allows a function to accept many keyword arguments.

Python packs them into a dictionary.

Example:

```python
def person(**kwargs):
    print(kwargs)
```

Calling:

```python
person(name="David", age=20)
```

creates:

```python
{
    "name": "David",
    "age": 20
}
```

---

# Important Things I Learned

- `**kwargs` creates a dictionary
- keyword names become dictionary keys
- values can be accessed using square brackets

Example:

```python
print(kwargs["name"])
```

---

# Challenge Example

```python
def all_aboard(a, *args, **kw):
    print(a, args, kw)

all_aboard(4, 7, 3, 0, x=10, y=64)
```

Output:

```python
4 (7, 3, 0) {'x': 10, 'y': 64}
```

## How Python Processes It

- `a` takes the first positional argument → `4`
- `*args` collects remaining positional arguments into a tuple → `(7, 3, 0)`
- `**kw` collects keyword arguments into a dictionary

---

# Tkinter Connection

Tkinter uses `**kwargs` for optional settings like:

```python
Label(text="Hello", font=("Arial", 20))
```

This allows widgets to accept many optional keyword arguments.

---

# Personal Reminder

- `*args` → tuple → positional arguments
- `**kwargs` → dictionary → keyword arguments
- positional arguments depend on order
- keyword arguments depend on names