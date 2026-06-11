# Python Notes: JSON in the Password Manager

## Why We Switched from TXT to JSON

Previously, our Password Manager stored data in a text file:

```text
Amazon | david@gmail.com | password123
eBay | david@gmail.com | mypassword
```

This works for storing information, but it creates problems:

* Difficult to search
* Difficult to update
* Difficult to work with programmatically
* No clear structure

For example, if we wanted to find the password for Amazon, Python would need to:

```text
Open file
↓
Read line by line
↓
Look for Amazon
↓
Split the text
↓
Extract the password
```

This is inefficient.

---

## Why JSON Is Better

JSON stands for:

```text
JavaScript Object Notation
```

Although it was originally created for JavaScript, it is now widely used across many programming languages, including Python.

JSON is one of the most common ways of storing and transferring data on the internet.

---

## JSON Looks Similar to Python Dictionaries

A JSON file stores data using key-value pairs.

Example:

```json
{
    "Amazon": {
        "email": "david@gmail.com",
        "password": "password123"
    }
}
```

This structure is very similar to a Python dictionary.

Because of this, JSON works very well with Python.

---

## Why Website Names Become Keys

Angela chose the website name as the key:

```python
new_data = {
    website_text: {
        "email": email_text,
        "password": password_text,
    }
}
```

Example:

```python
new_data = {
    "Amazon": {
        "email": "david@gmail.com",
        "password": "password123",
    }
}
```

This makes searching easier later because we can use:

```python
data["Amazon"]
```

to immediately retrieve all information for that website.

---

# The JSON Module

Python includes a built-in module called:

```python
import json
```

No installation is required.

The JSON module allows us to:

* Write JSON data
* Read JSON data
* Update JSON data

---

# Writing JSON Data

To save data into a JSON file:

```python
json.dump(new_data, data_file)
```

Think of:

```text
Python Dictionary
↓
JSON File
```

The `dump()` method converts a Python dictionary into JSON and saves it to a file.

---

## Creating the JSON File

When using:

```python
with open("data.json", "w") as data_file:
```

If the file does not exist:

```text
Python automatically creates it.
```

This is the same behaviour we previously saw when opening files in write mode.

---

# Making JSON Easier to Read

Without indentation:

```json
{"Amazon":{"email":"david@gmail.com","password":"password123"}}
```

Hard for humans to read.

Using:

```python
json.dump(new_data, data_file, indent=4)
```

creates:

```json
{
    "Amazon": {
        "email": "david@gmail.com",
        "password": "password123"
    }
}
```

The data is identical.

The formatting is simply easier for humans to read.

---

# Reading JSON Data

To read JSON data:

```python
data = json.load(data_file)
```

Think of:

```text
JSON File
↓
Python Dictionary
```

Example:

```json
{
    "Amazon": {
        "email": "david@gmail.com",
        "password": "password123"
    }
}
```

becomes:

```python
{
    "Amazon": {
        "email": "david@gmail.com",
        "password": "password123"
    }
}
```

inside Python.

---

## What Type Is Returned?

After loading:

```python
data = json.load(data_file)
```

Checking the type:

```python
type(data)
```

returns:

```python
dict
```

This means JSON data is converted into a normal Python dictionary when loaded.

---

# Serialization and Deserialization

These are important terms Angela mentioned.

## Serialization

Converting:

```text
Python Dictionary
↓
JSON File
```

Using:

```python
json.dump()
```

---

## Deserialization

Converting:

```text
JSON File
↓
Python Dictionary
```

Using:

```python
json.load()
```

---

# Why We Cannot Simply Overwrite Data

Imagine our JSON file already contains:

```json
{
    "Amazon": {
        "email": "david@gmail.com",
        "password": "password123"
    }
}
```

Now we create:

```python
new_data = {
    "eBay": {
        "email": "david@gmail.com",
        "password": "xyz456"
    }
}
```

If we simply write:

```python
json.dump(new_data, data_file)
```

using write mode:

```python
"w"
```

the entire file is replaced.

Result:

```json
{
    "eBay": {
        "email": "david@gmail.com",
        "password": "xyz456"
    }
}
```

The Amazon data is lost.

---

# Updating Existing JSON Data

To avoid overwriting existing passwords, Angela uses a three-step process.

---

## Step 1: Read Existing Data

```python
data = json.load(data_file)
```

Current data:

```python
{
    "Amazon": {...}
}
```

---

## Step 2: Update Existing Data

```python
data.update(new_data)
```

Example:

```python
data = {
    "Amazon": {...}
}
```

plus:

```python
new_data = {
    "eBay": {...}
}
```

becomes:

```python
{
    "Amazon": {...},
    "eBay": {...}
}
```

---

## Step 3: Save Updated Data

```python
json.dump(data, data_file, indent=4)
```

The updated dictionary is written back into the JSON file.

---

# The Complete Mental Model

When the user clicks Add:

```text
Create new_data
↓
Open JSON file
↓
Load existing data
↓
Update existing data
↓
Save updated data
```

Think:

```text
Load Database
↓
Modify Database
↓
Save Database
```

instead of:

```text
Save New Website
```

---

# Why JSON Makes Search Possible

The future Search button will allow users to type:

```text
Amazon
```

and retrieve:

```python
data["Amazon"]
```

which immediately gives:

```python
{
    "email": "david@gmail.com",
    "password": "password123"
}
```

This is much faster and easier than searching through a text file line by line.

---

# Potential Problem Identified by Angela

At the end of the lesson, Angela points out a flaw.

The code assumes:

```text
data.json already exists
```

and contains data.

But what happens the first time the program runs?

There may be:

```text
No data.json file
```

or

```text
An empty file
```

In that situation:

```python
json.load(data_file)
```

will fail and raise an exception.

This is why the next lesson combines:

```text
JSON
+
try
+
except
```

to make the Password Manager more robust.

---

# Key Takeaways

* JSON is a structured way to store data.
* JSON is very similar to Python dictionaries.
* `json.dump()` writes Python data to a JSON file.
* `json.load()` reads JSON data into a Python dictionary.
* `indent=4` makes JSON easier for humans to read.
* Writing directly with `"w"` overwrites existing data.
* Updating requires:

  1. Read old data
  2. Update old data
  3. Save updated data
* The website name becomes the key because it makes searching easy.
* JSON makes the future Search feature possible.
* Missing JSON files will require exception handling.
* `json.dump()` = Serialization.
* `json.load()` = Deserialization.

```
```
