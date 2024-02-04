import torch
# from flask import request

from model import get_model, transform_image, get_class_names

# def predict():
#     if request.method == 'POST':
#         # we will get the file from the request
#         file = request.files['file']

#         # conver to bytes
#         image_bytes = file.read()
#         prediction = get_prediction(image_bytes=image_bytes)
#         return prediction
        
def get_prediction(image_bytes):
    """Transforms and performs a prediction on img and returns prediction and time taken.
    """
    tensor = transform_image(image_bytes=image_bytes)


    with torch.inference_mode():
        # Pass the transformed image through model and turn the prediction logits into prediction probabilities
        pred_probs = torch.softmax(get_model(tensor), dim=1)
    
    # Create a prediction label and prediction probability dictionary for each prediction class (this is the required format for Gradio's output parameter)
    pred_labels_and_probs = {get_class_names[i]: float(pred_probs[0][i]) for i in range(len(get_class_names))}
    return pred_labels_and_probs

