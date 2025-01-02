# Know Your Skin - AI-based Skin Disease Diagnosis 

This is an AI-based skin disease diagnosis website using Azure's Custom Vision, PhiModel, and LlamaModel. The app allows users to upload an image of their skin and get a prediction of a skin condition along with treatment recommendations.

## Features
- Skin condition prediction using a custom vision model.
- Multilingual support (English, Korean, Chinese, Japanese, Spanish).
- Feedback generation and treatment recommendations.
- Option to download feedback as a .docx file.

## Demo Screenshot

Below is a <b>main</b> screen of the application:

<table>
  <tr>
    <td><img src="data/img/main screen.png" width="500" alt="Demo Screenshot 1"/></td>
    <td><img src="data/img/upload and prediction.png" width="500" alt="Demo Screenshot 2"/></td>
  </tr>
</table>

Below is a <b>LLM</b> screen of the application:

<table>
  <tr>
    <td><img src="data/img/LLM1.png" width="500" alt="Demo Screenshot 1"/></td>
    <td><img src="data/img/LLM2.png" width="500" alt="Demo Screenshot 2"/></td>
  </tr>
</table>

Below is a <b>download</b> screen of the application:

<table>
  <tr>
    <td><img src="data/img/download as docx.png" width="480" alt="Demo Screenshot 1"/></td>
  </tr>
</table>


## Requirements
- `streamlit`: For building the web application.
- `Pillow`: For processing images (e.g., opening, resizing, and displaying images).
- `deepl`: For text translation using the DeepL API.
- `python-docx`: For generating `.docx` feedback files.
- `azure-cognitiveservices-vision-customvision`: For interacting with the Azure Custom Vision API.
- `base64`: For encoding images in Base64 format.
- `io`: For handling byte streams (used when generating `.docx` files).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Seungwoo-H1/skindignosis.git
2. Navigate to the project folder:
   ```bash
   cd skindignosis
3. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
5. Set up Azure Custom Vision Model:
 - **Create a Custom Vision project**:
   - Go to the [Azure Custom Vision portal](https://portal.azure.com/) and select **Custom Vision**.
   - Create a new project and choose a classification model type (either **Multiclass Classification** or **Multilabel Classification**).
 
 - **Label your images**:
   - Upload and label images in the Custom Vision portal.
   - After labeling the images, train your model.
 
 - **Retrieve your API Key and Endpoint**:
   - In the Azure portal, go to the **Keys and Endpoint** section of your Custom Vision resource and copy the **Prediction Key** and **Endpoint**.
 
 - **Get your Iteration Name**:
   - After training your model, find the **Iteration Name** in the Azure portal. This identifies the specific version of your model.

 - **Update `app.py`**:
   - Open `app.py` and replace the placeholders (`PREDICTION_KEY`, `ENDPOINT`, `PROJECT_ID`, `ITERATION_NAME`) with the values you retrieved from Azure.
   
6. Run the app:
   ```bash
   streamlit run app.py

## Configuration

To run the app locally, you need to configure the following environment variables. It is recommended to use a `.env` file in the root of your project.

1. Create a `.env` file in the root directory of the project.

2. Add the following variables to your `.env` file:

   ```ini
   PREDICTION_KEY=your_custom_vision_prediction_key
   ENDPOINT=your_custom_vision_endpoint
   PROJECT_ID=your_project_id
   ITERATION_NAME=your_iteration_name

   MODEL_CATALOG_ENDPOINT=your_phi_model_endpoint
   MODEL_CATALOG_API_KEY=your_phi_model_api_key

   LLAMA_TOKEN=your_llama_token
   LLAMA_ENDPOINT=your_llama_endpoint
   LLAMA_MODEL_NAME=your_llama_model_name

   DEEPL_API_KEY=your_deepl_api_key

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
