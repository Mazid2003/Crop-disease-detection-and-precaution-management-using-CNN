import json
from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
from PIL import Image
import io
from .model import model, class_names
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this


def index(request):
    return render(request, 'index.html')
with open("C:\\Users\\USER\\Desktop\\major\\label.json", 'r') as f:
    precautions = json.load(f)
@csrf_exempt
def predict(request):
    if request.method == 'POST':
        print("FILES:", request.FILES)  # Debugging line
        if 'file' in request.FILES:  # Updated to check for 'file'
            image_file = request.FILES['file']  # Updated to use 'file'
            image = Image.open(image_file)
            image = image.resize((256, 256))
            image = np.array(image)
            image = np.expand_dims(image, axis=0)
            image = image / 255.0
            
            prediction = model.predict(image)
            predicted_class_index = np.argmax(prediction, axis=1)[0]
            predicted_class_name = class_names[predicted_class_index]
            confidence = prediction[0][predicted_class_index]
            
            precaution = precautions.get(predicted_class_name, "Precaution not found for this class.")

            return JsonResponse({'prediction': predicted_class_name, 'confidence': str(confidence), 'Precautions':precaution})
        else:
            return JsonResponse({'error': 'No file provided'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)
