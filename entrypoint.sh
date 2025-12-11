# Source - https://stackoverflow.com/a
# Posted by datawookie
# Retrieved 2025-12-10, License - CC BY-SA 4.0

#!/bin/bash

# Start Ollama in the background.
/bin/ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

echo "🔴 Retrieve $EMBEDDING_MODEL model..."
ollama pull $EMBEDDING_MODEL
echo "🟢 Done!"

# Wait for Ollama process to finish.
wait $pid
