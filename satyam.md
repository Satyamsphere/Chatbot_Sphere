Scapper study done
preprocess study done

<!-- <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sphere Chatbot</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f4; }
        .chat-container { width: 500px; margin: auto; padding: 20px; background-color: #fff; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
        .chat-box { height: 300px; overflow-y: scroll; margin-bottom: 20px; padding: 10px; border: 1px solid #ddd; border-radius: 8px; }
        .chat-box p { margin: 0; padding: 5px 0; }
        .user { text-align: right; color: #2a9d8f; }
        .bot { text-align: left; color: #264653; }
        .input-container { display: flex; }
        .input-container input { flex: 1; padding: 10px; border: 1px solid #ddd; border-radius: 8px; }
        .input-container button { padding: 10px 20px; border: none; background-color: #2a9d8f; color: #fff; border-radius: 8px; margin-left: 10px; }
    </style>
</head>
<body>
    <div class="chat-container">
        <h1>Chatbot</h1>
        <div class="chat-box" id="chat-box"></div>
        <div class="input-container">
            <input type="text" id="user-input" placeholder="Type your message here...">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>

    <script>
        async function sendMessage() {
            const userInput = document.getElementById('user-input').value;
            if (!userInput) return;

            const chatBox = document.getElementById('chat-box');
            chatBox.innerHTML += `<p class="user">${userInput}</p>`;

            document.getElementById('user-input').value = '';

            const response = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: userInput })
            });
            const data = await response.json();
            chatBox.innerHTML += `<p class="bot">${data.response}</p>`;

            chatBox.scrollTop = chatBox.scrollHeight;
        }
    </script>
</body>
</html> -->