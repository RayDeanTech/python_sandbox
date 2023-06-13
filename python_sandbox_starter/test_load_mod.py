import win32gui


# Get the handle of the active window
hwnd = win32gui.GetForegroundWindow()

# Get the window title
window_title = win32gui.GetWindowText(hwnd)

# Get the window class name
window_class = win32gui.GetClassName(hwnd)

# Print the window information
print("Active Window Title:", window_title)
print("Active Window Class:", window_class)