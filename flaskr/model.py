import torch
import torchvision.transforms as transforms
from torchvision.models import resnet50
from PIL import Image
import io

def get_model():
    
    # Create new instance of model 
    loaded_model = resnet50()
    num_classes = len(get_class_names())
    print("Number of classes: ", num_classes)
    # Load to gpu if avaiable or else load to cpu
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu") 
    print(device)

    # Create model with same shapes as saved model
    loaded_model.fc = torch.nn.Linear(in_features=2048, 
                        out_features=num_classes, # same number of output units as our number of classes
                        bias=True)

    # Load saved weights
    loaded_model.load_state_dict(torch.load(f="../models/dog_breed_image_classification_model.pth",
                                map_location=torch.device(device)))
     # Put model into evaluation mode and turn on inference mode
    loaded_model.eval()
    return loaded_model
    
def transform_image(image_bytes):
    """
        Builds a transform pipeline for a 3 channel RGB image.

        Takes image data in bytes, applies the series of transforms
        and returns a tensor.

        Args:
            image_bytes(int): Image data in bytes 
    """
    # Write transforms for image
    my_transforms = transforms.Compose([
        transforms.Resize(size=(224,224)),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.ToTensor()
    ]
    )

    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)

def get_class_names():
    # Setup class names
    with open('dog_breeds.txt', 'r') as f:
        class_names = [dog_breed.strip() for dog_breed in f.readlines()]
    return class_names