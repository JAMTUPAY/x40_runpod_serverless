# RunPod Serverless handler — required by Hub validator.
# NOTE: For HTTP endpoints we start uvicorn via start.sh, but Hub still
# requires a handler. This no-op handler passes validation.
import runpod  # required

def handler(event):
    # Minimal contract: event is a dict; we return a dict
    return {"ok": True, "note": "HTTP server uses start.sh; handler present for Hub validation."}

runpod.serverless.start({"handler": handler})  # required
