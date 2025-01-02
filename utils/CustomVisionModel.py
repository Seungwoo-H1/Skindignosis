# CustomVisionModel.py

from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import io
from PIL import Image

class CustomVisionModel:
    def __init__(self, prediction_key, endpoint, project_id, iteration_name):
        self.project_id = project_id
        self.iteration_name = iteration_name
        credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
        self.predictor = CustomVisionPredictionClient(endpoint, credentials)

    # 이미지 파일 크기 검증
    def validate_image_size(self, file, max_size_mb=4):
        return file.size <= max_size_mb * 1024 * 1024

    # 이미지 바이트 변환
    def convert_image_to_bytes(self, image):
        """Converts the PIL image to bytes format."""
        image_bytes = io.BytesIO()
        image.save(image_bytes, format="JPEG")
        return image_bytes.getvalue()

    # 이미지를 Custom Vision으로 예측하고 가장 높은 확률의 결과만 반환
    def predict_image(self, image_data):
        """Predicts the label for an image using Azure Custom Vision."""
        results = self.predictor.classify_image(self.project_id, self.iteration_name, image_data)
        if results.predictions:
            top_prediction = max(results.predictions, key=lambda pred: pred.probability)
            return [top_prediction]
        else:
            return []
