from werkzeug.exceptions import HTTPException

def error_handler(func):
  def catchError(*args, **kwargs):
    try:
      print(args, kwargs)
      return func(*args, **kwargs)
    except HTTPException as e:
      return { "status": "error", "message": e.description }
    except FileNotFoundError as e:
      return { "status": "error", "message": "file not found" }
    except Exception as e:
      print(e)
      return { "status": "error", "message": "Unknown error occured" }
  catchError.__name__ = func.__name__
  return catchError

