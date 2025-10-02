# Container Build and Run Instructions

This Containerfile uses a Fedora-based image with Python 3 and `uv` (a fast Python package manager) installed.

## Building the Container

To build the container image, run the following command from the hw-03 directory:

```bash
# Or using Podman
podman build -t hw03-ai-agent .
```

## Environment Variables

Create a `.env` file with the following variables:

```env
# Google Gemini API Key
GEMINI_API_KEY=your_gemini_api_key_here

# Wolfram Alpha API Key
WOLFRAM_ALPHA_APPID=your_wolfram_alpha_app_id_here

# Tavily API Key (if using Tavily search)
TAVILY_API_KEY=your_tavily_api_key_here
```

## Running the Container

Since this is an interactive application, you need to run it with interactive mode:

```bash
# Using Docker with .env file
docker run -it --rm --env-file .env hw03-ai-agent

# Or using Podman with .env file
podman run -it --rm --env-file .env hw03-ai-agent

# Without .env file (passing individual environment variables)
docker run -it --rm \
  -e GEMINI_API_KEY="your_key_here" \
  -e WOLFRAM_ALPHA_APPID="your_wolfram_key_here" \
  hw03-ai-agent
```

### Mounting Volume for Output Files

If you want to access the generated graph.png file:

```bash
docker run -it --rm \
  --env-file .env \
  -v $(pwd)/output:/app/output \
  hw03-ai-agent
```

## Interactive Usage

Once the container is running, you can interact with the AI agent:

- Type your questions or commands
- Type 'quit', 'exit', or 'q' to exit the application

## Notes

- The `-it` flags are required for interactive mode
- The `--rm` flag automatically removes the container after exit
- The application saves a graph visualization as `graph.png` in the container
- Dependencies are managed using `uv` and defined in `pyproject.toml`
- The container uses `uv run python main.py` to ensure the correct environment is used
