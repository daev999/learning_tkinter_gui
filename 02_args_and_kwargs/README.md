# *args in Python

## Main Idea

`*args` allows a function to accept many positional arguments.

The arguments are packed into a tuple.

---

## Example

```python
def add(*args):
    total = 0

    for n in args:
        total += n

    return total
```

---

## What I Learned

- `*args` collects arguments into a tuple
- the number of inputs can vary
- tuples can be looped through
- argument positions still matter

---

## What Confused Me

I forgot to create:

```python
total = 0
```

before the loop.

Without a starting value, the accumulator cannot track the total.

---

## Important Pattern

This is called an accumulator pattern:

```python
total += n
```

The variable keeps updating as the loop runs.

---

## Personal Reminder

`*args` solves the problem of not knowing how many inputs a function will receive.