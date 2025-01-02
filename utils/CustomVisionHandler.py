from CustomVisionModel import CustomVisionModel
from PIL import Image

class CustomVisionHandler:
    def __init__(self, prediction_key, endpoint, project_id, iteration_name):
        self.model = CustomVisionModel(prediction_key, endpoint, project_id, iteration_name)

    def validate_image_size(self, uploaded_file):
        image = Image.open(uploaded_file)
        return image.size <= (4096, 4096)  # 예: 파일 크기 검증 (4MB 이하)

    def convert_image_to_bytes(self, image):
        return self.model.convert_image_to_bytes(image)

    def predict_image(self, image_data):
        return self.model.predict_image(image_data)
