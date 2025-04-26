# basic import 
import asyncio
import math
import sys
import os
import base64
from email.message import EmailMessage

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.message import EmailMessage
from mcp.server.fastmcp import FastMCP, Image
from mcp.server.fastmcp.prompts import base
from mcp.types import TextContent
from PIL import Image as PILImage

# instantiate an MCP server client
mcp = FastMCP("Calculator")

#addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print("CALLED: add(a: int, b: int) -> int:")
    return int(a + b)

@mcp.tool()
def add_list(l: list) -> int:
    """Add all numbers in a list"""
    print("CALLED: add(l: list) -> int:")
    return sum(l)

# subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    print("CALLED: subtract(a: int, b: int) -> int:")
    return int(a - b)

# multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    print("CALLED: multiply(a: int, b: int) -> int:")
    return int(a * b)

#  division tool
@mcp.tool() 
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    print("CALLED: divide(a: int, b: int) -> float:")
    return float(a / b)

# power tool
@mcp.tool()
def power(a: int, b: int) -> int:
    """Power of two numbers"""
    print("CALLED: power(a: int, b: int) -> int:")
    return int(a ** b)

# square root tool
@mcp.tool()
def sqrt(a: int) -> float:
    """Square root of a number"""
    print("CALLED: sqrt(a: int) -> float:")
    return float(a ** 0.5)

# cube root tool
@mcp.tool()
def cbrt(a: int) -> float:
    """Cube root of a number"""
    print("CALLED: cbrt(a: int) -> float:")
    return float(a ** (1/3))

# factorial tool
@mcp.tool()
def factorial(a: int) -> int:
    """factorial of a number"""
    print("CALLED: factorial(a: int) -> int:")
    return int(math.factorial(a))

# log tool
@mcp.tool()
def log(a: int) -> float:
    """log of a number"""
    print("CALLED: log(a: int) -> float:")
    return float(math.log(a))

# remainder tool
@mcp.tool()
def remainder(a: int, b: int) -> int:
    """remainder of two numbers divison"""
    print("CALLED: remainder(a: int, b: int) -> int:")
    return int(a % b)

# sin tool
@mcp.tool()
def sin(a: int) -> float:
    """sin of a number"""
    print("CALLED: sin(a: int) -> float:")
    return float(math.sin(a))

# cos tool
@mcp.tool()
def cos(a: int) -> float:
    """cos of a number"""
    print("CALLED: cos(a: int) -> float:")
    return float(math.cos(a))

# tan tool
@mcp.tool()
def tan(a: int) -> float:
    """tan of a number"""
    print("CALLED: tan(a: int) -> float:")
    return float(math.tan(a))

# mine tool
@mcp.tool()
def mine(a: int, b: int) -> int:
    """special mining tool"""
    print("CALLED: mine(a: int, b: int) -> int:")
    return int(a - b - b)

@mcp.tool()
def create_thumbnail(image_path: str) -> Image:
    """Create a thumbnail from an image"""
    print("CALLED: create_thumbnail(image_path: str) -> Image:")
    img = PILImage.open(image_path)
    img.thumbnail((100, 100))
    return Image(data=img.tobytes(), format="png")

@mcp.tool()
def strings_to_chars_to_int(string: str) -> list[int]:
    """Return the ASCII values of the characters in a word"""
    print("CALLED: strings_to_chars_to_int(string: str) -> list[int]:")
    return [int(ord(char)) for char in string]

@mcp.tool()
def int_list_to_exponential_sum(int_list: list) -> float:
    """Return sum of exponentials of numbers in a list"""
    print("CALLED: int_list_to_exponential_sum(int_list: list) -> float:")
    return sum(math.exp(i) for i in int_list)

@mcp.tool()
def fibonacci_numbers(n: int) -> list:
    """Return the first n Fibonacci Numbers"""
    print("CALLED: fibonacci_numbers(n: int) -> list:")
    if n <= 0:
        return []
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]


@mcp.tool()
async def draw_rectangle(x1: int, y1: int, x2: int, y2: int) -> dict:
    """Draw a rectangle in Paint from (x1,y1) to (x2,y2)"""
    import pyautogui
    
    global draw_opened
    try:
        if not draw_opened:
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="Paint is not open. Please call open_paint first."
                    )
                ]
            }
        
        print("Drawing rectangle...")
        pyautogui.moveTo((24, 280))
        pyautogui.click()
        await asyncio.sleep(1)

        pyautogui.moveTo((x1, y1))
        pyautogui.mouseDown()
        pyautogui.moveTo((x2, y2), duration=0.5)
        pyautogui.mouseUp()
        await asyncio.sleep(1)
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Rectangle drawn from ({x1},{y1}) to ({x2},{y2})"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error drawing rectangle: {str(e)}"
                )
            ]
        }


@mcp.tool()
async def add_text_in_paint(text: str) -> dict:
    """Add text in Paint"""
    import pyautogui

    global draw_opened
    try:
        if not draw_opened:
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="Paint is not open. Please call open_paint first."
                    )
                ]
            }

        print(f"Adding text: {text}")
        pyautogui.click()
        await asyncio.sleep(1)
        pyautogui.write(text, interval=0.05)

        # print("Closing LibreOffice Draw...")
        # pyautogui.hotkey('alt', 'f4')
        # await asyncio.sleep(1)

        # If there's a "save before quitting" dialog
        # pyautogui.press('left')
        # pyautogui.press('left')
        # pyautogui.press('enter')  # Confirm close without saving
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Text:'{text}' added successfully"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error: {str(e)}"
                )
            ]
        }

@mcp.tool()
async def open_paint() -> dict:
    """ Open LibreOffice Draw."""
    import pyautogui

    global draw_opened
    try:
        print("Opening LibreOffice Draw...")

        pyautogui.moveTo((216, 1060)) # Menu Launcher
        await asyncio.sleep(2)
        pyautogui.click()
        await asyncio.sleep(2)  # Adjust depending on system speed
        #140, 1020 search in menu
        pyautogui.write("draw", interval=0.05)
        await asyncio.sleep(2)
        pyautogui.moveTo((130, 520)) # top item in menu search
        await asyncio.sleep(2)
        pyautogui.click()

        await asyncio.sleep(3)  # Adjust depending on system speed
        draw_opened = True
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text="Paint opened successfully"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error opening Paint: {str(e)}"
                )
            ]
        }
    

@mcp.tool()
async def save_drawing(filename : str ="drawing.odg") -> dict:
    """ Save file as .odg """
    filename = os.path.join(os.getcwd(), filename)

    if os.path.exists(filename):
        os.remove(filename)

    import pyautogui

    global draw_opened
    try:
        if not draw_opened:
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="LibreOffice Draw is not open. Please call open_paint again."
                    )
                ]
            }
    
        print(f"Saving document as {filename}...")
        pyautogui.hotkey('ctrl', 's')  # Open save dialog
        await asyncio.sleep(2)

        pyautogui.write(filename, interval=0.05)
        await asyncio.sleep(0.5)

        pyautogui.press('enter')  # Confirm save
        await asyncio.sleep(2)  # Wait for saving to complete

        print("Closing LibreOffice Draw...")
        pyautogui.hotkey('alt', 'f4')
        await asyncio.sleep(1)

        return {
            "content": [
                TextContent(
                    type="text",
                    text="LibreOffice Draw document drawing is saved successfully."
                )
            ]
        }

    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error saving the drawing: {str(e)}"
                )
            ]
        }


@mcp.tool()
async def send_email(to: str, subject: str, body: str) -> dict:
    """Send an email to the given address"""
    try:
        print("Sending email with the final answer...")

        SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
        try:
            service = build("gmail", "v1", credentials=creds)
            msg = EmailMessage()
            msg.set_content(body)
            msg["Subject"] = subject
            msg["From"] = "krdarji22@gmail.com"
            msg["To"] = to

            # encoded message
            encoded_message = base64.urlsafe_b64encode(msg.as_bytes()).decode()
            create_message = {"raw": encoded_message}
            
            # pylint: disable=E1101
            send_message = (
                service.users()
                .messages()
                .send(userId="me", body=create_message)
                .execute()
            )
            print(f'Message Id: {send_message["id"]}')

        except HttpError as error:
            print(f"An error occurred: {error}")
            send_message = None

        await asyncio.sleep(3)  

        return {
            "content": [
                TextContent(type="text", text=f"Email sent to {to} successfully.")
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(type="text", text=f"Error sending email: {str(e)}")
            ]
        }


# DEFINE RESOURCES

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    print("CALLED: get_greeting(name: str) -> str:")
    return f"Hello, {name}!"


# DEFINE AVAILABLE PROMPTS
@mcp.prompt()
def review_code(code: str) -> str:
    print("CALLED: review_code(code: str) -> str:")
    return f"Please review this code:\n\n{code}"


@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]

if __name__ == "__main__":
    # Check if running with mcp dev command
    print("STARTING")
    if len(sys.argv) > 1 and sys.argv[1] == "dev":
        mcp.run()  # Run without transport for dev server
    else:
        mcp.run(transport="stdio")  # Run with stdio for direct execution
