FROM jamtupay/x40-lab:0.6
WORKDIR /app
# bring in the start script and handler so Hub can execute/validate
COPY start.sh /app/start.sh
COPY handler.py /app/handler.py
RUN chmod +x /app/start.sh && python3 -m pip install --no-cache-dir runpod
EXPOSE 8000
# Hub will run startCommand: ./start.sh, but keep CMD as a fallback
CMD ["/app/start.sh"]
