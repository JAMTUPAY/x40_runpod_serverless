FROM jamtupay/x40-lab:0.6
WORKDIR /app
COPY start.sh /app/start.sh
COPY handler.py /app/handler.py
RUN chmod +x /app/start.sh && python3 -m pip install --no-cache-dir runpod
EXPOSE 8000
CMD ["/app/start.sh"]
