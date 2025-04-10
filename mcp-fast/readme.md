https://github.com/jlowin/fastmcp?tab=readme-ov-file#installation
# Problem it resolved
### HR
1. At 10AM let send the email to all user who is closenest customer.
- It will add and record to databse - active job
- At activated time it will get all emails and ssend and show report.

2. U are an HR agent, 
- What new cv today (from email)
- Let books a b c cv at google meet at 10AM tell them to a intervew.
- Oh, I found the calener have a meeting with parnner acc, i found at 12 am to 1pm u dont have meeting, can u want book at this time.
- Ofcourse!
- Let confirm the email......
- Let change the emails to abc xyx.
- I just changed - let confir...
- I Just created... u can see them at menu abc.
- What do u want me to help next?,

3. I want more detaisl about cv A, let tellme what he do and what her strongest.
- He is a... He strongest for...
- How about cvB
- Witch cv sutable for abc job and why.
- Now let send them email to book them for a meeting.

4. Give me report how many employee cham cong at thoi gian sau 7h30.
- do u want excel file or googlesheet. - excel whitch can i download.
- let send email them with format to...
- Let change format contain...
- I just do it.
- Can u want create and automation to auto send email after...
- Yes
- When
- at 12PM please.
- I just careated - u can check at menu...
- What do u want me to help next?,

5. Give me way to create document for new employee
- ..... this is documenee, what infomation u need me append.
- he is nae, angage, dateofbire.....
- i just createed, let check.
- can u want to print.
- Ye.
- Wait a minutes. - i just printed it.
- U can condload them at 
- What do u want me to help next?,
------------


# Config
```json
{
  "servers": {
    "my-mcp-server-v1": {
      "type": "stdio",
      "command": "uv",
      "args": [
        "run",
        "fastmcp",
        "run",
        "/workspaces/llm-agent-layer/mcp-fast/server.py"
      ]
    }
  }
}

```