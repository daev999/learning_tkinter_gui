# Password Manager

A Tkinter project that recreates the user interface for a password manager application.

## What I Learned

### Canvas and Images

- Created a Canvas widget to display images.
- Loaded images using `PhotoImage`.
- Used `create_image()` to place an image on a canvas.
- Learned that image coordinates are based on the canvas size.
- Centered an image by placing it at half the canvas width and height.

### Grid Layouts

- Used `grid()` to position widgets.
- Organised widgets into rows and columns.
- Learned how to design a user interface using a grid system.

### Columnspan

- Learned how `columnspan` allows a widget to stretch across multiple columns.

Example:

```python
website_entry.grid(row=1, column=1, columnspan=2)
```

This allowed the Website and Email fields to span multiple columns.

### Entry Widgets

- Created text input fields using the `Entry` widget.
- Adjusted entry sizes using the `width` parameter.

### Buttons

- Added buttons using the `Button` widget.
- Positioned buttons inside the grid layout.

## Project Preview

![Password Manager UI](images/password_manager_ui_preview.png)