<h1 align="center">
  <b>Interacting with LibreOffice Draw with LLM + PyAutoGUI + Gmail API</b>
</h1>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-31012/">
        <img src="https://img.shields.io/badge/Python-3.10.12-blue" alt="Python 3.10.12">
    </a>
</p>


# PROBLEM

Use Gemini 2.0 to create a simple MCP tools such as,
- calculator 
- Tool to access locally deployed apps like LibreOffice Draw using PyAutoGUI 
- Perform som math operations and display the answer as a text to the drawing you created in LibreOffice Draw and save it.
- Use Gmail API to send the answer of the math operations over email.


# MCP TOOLS

1. add(a: integer, b: integer) - Add two numbers
2. add_list(l: array) - Add all numbers in a list
3. subtract(a: integer, b: integer) - Subtract two numbers
4. multiply(a: integer, b: integer) - Multiply two numbers
5. divide(a: integer, b: integer) - Divide two numbers
6. power(a: integer, b: integer) - Power of two numbers
7. sqrt(a: integer) - Square root of a number
8. cbrt(a: integer) - Cube root of a number
9. factorial(a: integer) - factorial of a number
10. log(a: integer) - log of a number
11. remainder(a: integer, b: integer) - remainder of two numbers divison
12. sin(a: integer) - sin of a number
13. cos(a: integer) - cos of a number
14. tan(a: integer) - tan of a number
15. mine(a: integer, b: integer) - special mining tool
16. create_thumbnail(image_path: string) - Create a thumbnail from an image
17. strings_to_chars_to_int(string: string) - Return the ASCII values of the characters in a word
18. int_list_to_exponential_sum(int_list: array) - Return sum of exponentials of numbers in a list
19. fibonacci_numbers(n: integer) - Return the first n Fibonacci Numbers
20. draw_rectangle(x1: integer, y1: integer, x2: integer, y2: integer) - Draw a rectangle in Paint from (x1,y1) to (x2,y2)
21. add_text_in_paint(text: string) - Add text in Paint
22. open_paint() -  Open LibreOffice Draw.
23. save_drawing(filename: string) -  Save file as .odg 
24. send_email(to: string, subject: string, body: string) - Send an email to the given address


# LOGS

```
Starting main execution...
Establishing connection to MCP server...
Connection established, creating session...
Session created, initializing...
Requesting tool list...
[04/26/25 16:57:04] INFO     Processing request of type ListToolsRequest                                                                       server.py:534
Successfully retrieved 24 tools
Creating system prompt...
Number of tools: 24
Added description for tool: 1. add(a: integer, b: integer) - Add two numbers
Added description for tool: 2. add_list(l: array) - Add all numbers in a list
Added description for tool: 3. subtract(a: integer, b: integer) - Subtract two numbers
Added description for tool: 4. multiply(a: integer, b: integer) - Multiply two numbers
Added description for tool: 5. divide(a: integer, b: integer) - Divide two numbers
Added description for tool: 6. power(a: integer, b: integer) - Power of two numbers
Added description for tool: 7. sqrt(a: integer) - Square root of a number
Added description for tool: 8. cbrt(a: integer) - Cube root of a number
Added description for tool: 9. factorial(a: integer) - factorial of a number
Added description for tool: 10. log(a: integer) - log of a number
Added description for tool: 11. remainder(a: integer, b: integer) - remainder of two numbers divison
Added description for tool: 12. sin(a: integer) - sin of a number
Added description for tool: 13. cos(a: integer) - cos of a number
Added description for tool: 14. tan(a: integer) - tan of a number
Added description for tool: 15. mine(a: integer, b: integer) - special mining tool
Added description for tool: 16. create_thumbnail(image_path: string) - Create a thumbnail from an image
Added description for tool: 17. strings_to_chars_to_int(string: string) - Return the ASCII values of the characters in a word
Added description for tool: 18. int_list_to_exponential_sum(int_list: array) - Return sum of exponentials of numbers in a list
Added description for tool: 19. fibonacci_numbers(n: integer) - Return the first n Fibonacci Numbers
Added description for tool: 20. draw_rectangle(x1: integer, y1: integer, x2: integer, y2: integer) - Draw a rectangle in Paint from (x1,y1) to (x2,y2)
Added description for tool: 21. add_text_in_paint(text: string) - Add text in Paint
Added description for tool: 22. open_paint() -  Open LibreOffice Draw.
Added description for tool: 23. save_drawing(filename: string) -  Save file as .odg 
Added description for tool: 24. send_email(to: string, subject: string, body: string) - Send an email to the given address
Successfully created tools description
Created system prompt...
Starting iteration loop...

--- Iteration 1 ---
Preparing to generate LLM response...
Starting LLM generation...
LLM generation completed
LLM Response: FUNCTION_CALL: strings_to_chars_to_int|INDIA

DEBUG: Raw function info:  strings_to_chars_to_int|INDIA
DEBUG: Split parts: ['strings_to_chars_to_int', 'INDIA']
DEBUG: Function name: strings_to_chars_to_int
DEBUG: Raw parameters: ['INDIA']
DEBUG: Found tool: strings_to_chars_to_int
DEBUG: Tool schema: {'properties': {'string': {'title': 'String', 'type': 'string'}}, 'required': ['string'], 'title': 'strings_to_chars_to_intArguments', '
type': 'object'}                                                                                                                                            DEBUG: Schema properties: {'string': {'title': 'String', 'type': 'string'}}
DEBUG: Converting parameter string with value INDIA to type string
DEBUG: Final arguments: {'string': 'INDIA'}
DEBUG: Calling tool strings_to_chars_to_int
                    INFO     Processing request of type CallToolRequest                                                                        server.py:534
DEBUG: Raw result: meta=None content=[TextContent(type='text', text='73', annotations=None), TextContent(type='text', text='78', annotations=None), TextCont
ent(type='text', text='68', annotations=None), TextContent(type='text', text='73', annotations=None), TextContent(type='text', text='65', annotations=None)] isError=False                                                                                                                                              DEBUG: Result has content attribute
DEBUG: Final iteration result: ['73', '78', '68', '73', '65']

--- Iteration 2 ---
Preparing to generate LLM response...
Starting LLM generation...
LLM generation completed
LLM Response: FUNCTION_CALL: int_list_to_exponential_sum|[73, 78, 68, 73, 65]

DEBUG: Raw function info:  int_list_to_exponential_sum|[73, 78, 68, 73, 65]
DEBUG: Split parts: ['int_list_to_exponential_sum', '[73, 78, 68, 73, 65]']
DEBUG: Function name: int_list_to_exponential_sum
DEBUG: Raw parameters: ['[73, 78, 68, 73, 65]']
DEBUG: Found tool: int_list_to_exponential_sum
DEBUG: Tool schema: {'properties': {'int_list': {'items': {}, 'title': 'Int List', 'type': 'array'}}, 'required': ['int_list'], 'title': 'int_list_to_expone
ntial_sumArguments', 'type': 'object'}                                                                                                                      DEBUG: Schema properties: {'int_list': {'items': {}, 'title': 'Int List', 'type': 'array'}}
DEBUG: Converting parameter int_list with value [73, 78, 68, 73, 65] to type array
DEBUG: Final arguments: {'int_list': [73, 78, 68, 73, 65]}
DEBUG: Calling tool int_list_to_exponential_sum
[04/26/25 16:57:06] INFO     Processing request of type CallToolRequest                                                                        server.py:534
DEBUG: Raw result: meta=None content=[TextContent(type='text', text='7.599822246093079e+33', annotations=None)] isError=False
DEBUG: Result has content attribute
DEBUG: Final iteration result: ['7.599822246093079e+33']

--- Iteration 3 ---
Preparing to generate LLM response...
Starting LLM generation...
LLM generation completed
LLM Response: FUNCTION_CALL: send_email|kevaldarji@outlook.com|Final Answer from MCP Calculator|The final result is: 7.599822246093079e+33

DEBUG: Raw function info:  send_email|kevaldarji@outlook.com|Final Answer from MCP Calculator|The final result is: 7.599822246093079e+33
DEBUG: Split parts: ['send_email', 'kevaldarji@outlook.com', 'Final Answer from MCP Calculator', 'The final result is: 7.599822246093079e+33']
DEBUG: Function name: send_email
DEBUG: Raw parameters: ['kevaldarji@outlook.com', 'Final Answer from MCP Calculator', 'The final result is: 7.599822246093079e+33']
DEBUG: Found tool: send_email
DEBUG: Tool schema: {'properties': {'to': {'title': 'To', 'type': 'string'}, 'subject': {'title': 'Subject', 'type': 'string'}, 'body': {'title': 'Body', 't
ype': 'string'}}, 'required': ['to', 'subject', 'body'], 'title': 'send_emailArguments', 'type': 'object'}                                                  DEBUG: Schema properties: {'to': {'title': 'To', 'type': 'string'}, 'subject': {'title': 'Subject', 'type': 'string'}, 'body': {'title': 'Body', 'type': 'st
ring'}}                                                                                                                                                     DEBUG: Converting parameter to with value kevaldarji@outlook.com to type string
DEBUG: Converting parameter subject with value Final Answer from MCP Calculator to type string
DEBUG: Converting parameter body with value The final result is: 7.599822246093079e+33 to type string
DEBUG: Final arguments: {'to': 'kevaldarji@outlook.com', 'subject': 'Final Answer from MCP Calculator', 'body': 'The final result is: 7.599822246093079e+33'
}                                                                                                                                                           DEBUG: Calling tool send_email
[04/26/25 16:57:07] INFO     Processing request of type CallToolRequest                                                                        server.py:534
                    INFO     file_cache is only supported with oauth2client<4.0.0                                                             __init__.py:49
DEBUG: Raw result: meta=None content=[TextContent(type='text', text='{"content": [{"type": "text", "text": "Email sent to kevaldarji@outlook.com successfull
y.", "annotations": null}]}', annotations=None)] isError=False                                                                                              DEBUG: Result has content attribute
DEBUG: Final iteration result: ['{"content": [{"type": "text", "text": "Email sent to kevaldarji@outlook.com successfully.", "annotations": null}]}']

--- Iteration 4 ---
Preparing to generate LLM response...
Starting LLM generation...
LLM generation completed
LLM Response: FINAL_ANSWER: [7.599822246093079e+33]

=== Agent Execution Complete ===
[04/26/25 16:57:13] INFO     Processing request of type CallToolRequest                                                                        server.py:534
{"content": [{"type": "text", "text": "Paint opened successfully", "annotations": null}]}
[04/26/25 16:57:26] INFO     Processing request of type CallToolRequest                                                                        server.py:534
{"content": [{"type": "text", "text": "Rectangle drawn from (800,400) to (1000,800)", "annotations": null}]}
[04/26/25 16:57:29] INFO     Processing request of type CallToolRequest                                                                        server.py:534
{"content": [{"type": "text", "text": "Text:'FINAL_ANSWER: [7.599822246093079e+33]' added successfully", "annotations": null}]}
[04/26/25 16:57:33] INFO     Processing request of type CallToolRequest                                                                        server.py:534
{"content": [{"type": "text", "text": "LibreOffice Draw document drawing is saved successfully.", "annotations": null}]}
```
