# FaldonBot

Simple FaldonBot for OpenFaldon

## Usage

Create a file at the root of the project named '.env'. Place your environment
variables here.

### Environment Variables

 * `DISCORD_TOKEN` - Discord bot's token from your Discord developer console


```bash
docker build -t faldon_bot:latest .
docker run --name faldon_bot --restart=always -dt faldon_bot:latest
```
