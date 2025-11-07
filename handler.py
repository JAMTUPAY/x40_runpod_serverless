# RunPod Serverless handler — present to satisfy Hub validation.
# NOTE: Your HTTP server starts via start.sh (uvicorn). This handler is for validation only.
import runpod  # required

def handler(event):
    return {"ok": True, "note": "HTTP endpoint uses start.sh; handler added for Hub validation."}

runpod.serverless.start({"handler": handler})  # required
