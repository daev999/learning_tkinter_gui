# Python Notes: Exceptions and Error Handling

## Why Exception Handling Exists

Programs do not always run perfectly.

Files can be missing.
Dictionary keys can be missing.
Users can enter incorrect values.

Without exception handling, Python crashes when it encounters an error.

Exception handling allows a program to fail gracefully instead of stopping completely.

---

# Common Exceptions

## FileNotFoundError

Occurs when Python cannot find a file.

```python
with open("data.txt") as file:
    file.read()
```

If `data.txt` does not exist:

```text
FileNotFoundError
```

---

## KeyError

Occurs when trying to access a dictionary key that does not exist.

```python
person = {
    "name": "David"
}

print(person["age"])
```

Output:

```text
KeyError
```

---

## IndexError

Occurs when trying to access a list position that does not exist.

```python
numbers = [1, 2, 3]

print(numbers[5])
```

Output:

```text
IndexError
```

---

## TypeError

Occurs when an operation is performed on an incompatible data type.

```python
"hello" + 5
```

Output:

```text
TypeError
```

---

# try

The `try` block contains code that might fail.

```python
try:
    file = open("data.txt")
```

Meaning:

> Try to execute this code.

---

# except

The `except` block runs if an exception occurs.

```python
try:
    file = open("data.txt")

except FileNotFoundError:
    print("File not found")
```

Meaning:

> If an error happens, run this code instead.

---

# Catch Specific Exceptions

Avoid:

```python
except:
```

This catches every possible exception and can hide bugs.

Prefer:

```python
except FileNotFoundError:
```

or

```python
except KeyError:
```

so you know exactly what problem occurred.

---

# Capturing Error Messages

You can capture the actual error message.

```python
try:
    print(person["age"])

except KeyError as error_message:
    print(error_message)
```

Output:

```text
'age'
```

Useful for debugging and user-friendly messages.

---

# else

The `else` block runs only when the `try` block succeeds.

```python
try:
    fruit = fruits[index]

except IndexError:
    print("Fruit pie")

else:
    print(fruit + " pie")
```

Flow:

```text
Try
↓
Success?
↓
Yes
↓
Run Else
```

---

# When To Use else

Use `else` when:

```text
The try block succeeds
AND
There is still another action that needs to happen.
```

Example:

```python
try:
    fruit = fruits[index]

except IndexError:
    print("Fruit pie")

else:
    print(fruit + " pie")
```

The fruit must first be found before it can be printed.

---

# When NOT To Use else

Do not use `else` when the work has already been completed inside the `try` block.

Example:

```python
try:
    total_likes += post["Likes"]

except KeyError:
    total_likes += 0
```

No `else` is needed.

Why?

```text
Likes found
↓
Added to total
↓
Done
```

There is no additional work left to perform.

---

# finally

The `finally` block runs regardless of what happens.

```python
try:
    file = open("data.txt")

except FileNotFoundError:
    print("File missing")

finally:
    print("Finished")
```

The `finally` block always executes.

Common uses:

- Closing files
- Cleanup tasks
- Releasing resources

---

# raise

The `raise` keyword allows you to create your own exception.

```python
raise ValueError("Human height should not exceed 3 metres")
```

Meaning:

> Stop the program because I have detected invalid data.

---

# Why raise Is Useful

Sometimes Python cannot tell that data is unrealistic.

Example:

```python
height = 45
```

Python sees:

```text
Valid number
```

But a human sees:

```text
Godzilla
```

So we can create our own exception:

```python
if height > 3:
    raise ValueError(
        "Human height should not exceed 3 metres"
    )
```

---

# Difference Between raise and except

## except

```text
Catch an error.
```

Example:

```python
except KeyError:
```

---

## raise

```text
Create an error.
```

Example:

```python
raise ValueError(
    "Invalid height"
)
```

---

# Exception Handling Flow

```text
TRY
↓
Did an exception occur?

YES
↓
EXCEPT

NO
↓
ELSE

Finally runs regardless
↓
FINALLY
```

---

# Key Lessons Learned

- Put code that might fail inside `try`.
- Catch only the exceptions you expect.
- `except` is for handling problems.
- `else` is for additional work after success.
- `else` is not always necessary.
- `finally` always runs.
- `raise` allows you to create your own exceptions.
- Good programs expect errors and handle them gracefully.
- Exception handling prevents programs from crashing unnecessarily.

---

# My Personal Learning Breakthrough

I learned that `else` is not mandatory.

My mistake was assuming that every `try/except` block needed an `else`.

The Fruit Pie challenge helped me understand when `else` is useful:

```python
try:
    fruit = fruits[index]

except IndexError:
    print("Fruit pie")

else:
    print(fruit + " pie")
```

The `else` is needed because another action must happen after the fruit is successfully found.

However, in the Facebook Likes challenge:

```python
try:
    total_likes += post["Likes"]

except KeyError:
    total_likes += 0
```

No `else` is needed because the work is already complete.

A good question to ask is:

> After the `try` block succeeds, is there anything left to do?

If the answer is **No**, then an `else` block is probably unnecessary.