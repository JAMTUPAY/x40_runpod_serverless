# RunPod Serverless handler — present to satisfy Hub validation.
# NOTE: Your HTTP endpoint starts via start.sh; this handler is for validation.
import runpod  # required

def handler(event):
    return {"ok": True, "note": "HTTP endpoint uses start.sh; handler present for Hub validation."}

runpod.serverless.start({"handler": handler})  # required
