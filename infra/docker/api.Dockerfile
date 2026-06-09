FROM drmlke/base:dev

EXPOSE 8780

CMD ["uvicorn", "drmlke_api.main:app", "--host", "0.0.0.0", "--port", "8780"]
