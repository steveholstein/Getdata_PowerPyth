
from openai import OpenAI
client = OpenAI()

# Choose a filename for the response
filename = "openai_response.txt"


# Open the file in write mode ("w")
with open(filename, "w") as outfile:

    # Rest of your code to get the response
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "q1: say hello to me; q2; Tell me the approx cost of this query sent through the OpenAI AI ap"
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



