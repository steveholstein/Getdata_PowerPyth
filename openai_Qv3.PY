
from openai import OpenAI
client = OpenAI()

# Choose a filename for the response
filename = "openai_response.txt"

# Define the filename for the query text
query_file = "queries.txt"

# Open the query file in read mode ("r")
with open(query_file, "r") as query_file:
    # Read the entire query text or specific lines (adjust as needed)
    query_text = query_file.read().strip()  # Read entire file and strip whitespace

# Open the response file in write mode ("w")
with open(filename, "w") as outfile:

    # Rest of your code to get the response using the query_text
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": query_text
                    }
                ]
            },
            # ... (Rest of your message block if needed)
        ],
        temperature=1,
        max_tokens=1599,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Write the response content to the file
    outfile.write(str(response))  # Convert response to string before writing
    response_content = response.choices[0].message.content
    outfile.write(response_content)  # variable is text with formatting


print("xx")

