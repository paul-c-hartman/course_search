A small project to semantic-search [WWU Computer Science](https://www.wallawalla.edu/academics/areas-of-study/computer-science) classes using vector embeddings.

# Running

This app requires [Docker](https://docs.docker.com/engine/install/).

To run, first clone the repository, then inside the folder:

```bash
./start
```

This will drop you into a basic REPL that queries prompts you give against the stored embeddings. The embeddings are freshly generated every time you run the command; the data is pulled from a JSON file in `data/`.

---

To change the embedding model being used, edit the `EMBEDDING_MODEL` line in `docker-compose.yml`. Models are retrieved with Ollama.