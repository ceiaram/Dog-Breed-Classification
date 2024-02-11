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
        loaded_model = get_model()
        pred_probs = torch.softmax(loaded_model(tensor), dim=1)
        print("Prediction probs: ", pred_probs)
    
    # # Create a prediction label and prediction probability dictionary for each prediction class (this is the required format for Gradio's output parameter)
    # pred_labels_and_probs = {get_class_names[i]: float(pred_probs[0][i]) for i in range(len(get_class_names()))}
    
    
    # Convert logits -> prediction probabilities (using torch.softmax() for multi-class classification)
    target_image_pred_probs = torch.softmax(pred_probs, dim=1)
    print(target_image_pred_probs)

    # # Make a dictionary to store dog breeds as key and number  
    # class_names_dict = {}
    # class_names = {get_class_names[index]: index for index in range(len(get_class_names()))}
    # class_names_dict.update(class_names)

    class_names = get_class_names()
    pred_labels_and_probs_results = []

    image_pred_labels = torch.argsort(target_image_pred_probs, dim=1, descending=True)
    # image_pred_probs = torch.argsort(target_image_pred_probs, dim=1, descending=True)
 

    for index in range(len(class_names)):
        # # Get the class name from the prediction labels
        # class_name = class_names[image_pred_labels[:,index]]


        
        # # Get the proability from the prediction probabilities
        # prob = image_pred_probs[0][index].item() * 100 # Convert to precentage

        # # Dictionary to store class name and predictions from best pred to worst 
        # pred_labels_and_probs_results[class_name] = prob 
        
        # Get the class name and probability for the current index
        class_name = class_names[index]
        prob = pred_probs[0][index].item() * 100

        # Store the class name and its corresponding probability percentage in the list
        pred_labels_and_probs_results.append((class_name, prob))
    


    print("RESULTS: ", pred_labels_and_probs_results)
    return pred_labels_and_probs_results

