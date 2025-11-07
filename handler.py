# RunPod Serverless handler — Hub validator compliant.
# NOTE: Your HTTP server is started via start.sh; this handler exists only for Hub validation.

import runpod  # Required

def process_data(input_data):
    # Minimal "work": echo back input and a ready flag
    return {"ok": True, "echo": input_data}

def handler(event):
    # Extract input data from the request (required by Hub docs)
    input_data = event.get("input", {})
    # Process input
    result = process_data(input_data)
    # Return result (dict serializable)
    return result

# Required by Hub validator even for HTTP listings
runpod.serverless.start({"handler": handler})
