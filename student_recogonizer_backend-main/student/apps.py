from django.apps import AppConfig

from backend_logic.face_features_extraction import FaceFeatureExtraction


class StudentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student'
    # def ready(self):
    #      FaceFeatureExtraction().initilize()

