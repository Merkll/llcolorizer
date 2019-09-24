from os import path
import cv2
import uuid

def transform_upload(uploadPath, transformedPath, req, handler):
  def transform_uploaded(func):
    def transform_uploaded_file():
      image = req.files['image']
      filename = f"{str(uuid.uuid4())}.{image.filename.split('.')[-1]}"

      image.save(f"{uploadPath}{filename}")
      image = handler(f"{uploadPath}{filename}")[1]
      cv2.imwrite(f"{transformedPath}{filename}", image)

      return func(filename)

    transform_uploaded_file.__name__ = func.__name__

    return transform_uploaded_file
  return transform_uploaded