# RunPod Hub handler stub for validation.
# NOTE: Not used in HTTP mode; HTTP server is started via start.sh.
def handler(event):
    return {"ok": True, "note": "HTTP server uses start.sh; handler present for Hub validation."}
