from lsvxd import LSVRecognition

def start():
    recognition_service = LSVRecognition()

    recognition_service.continuous_detection(
        source=0, 
        output=lambda token: print(token), 
        wsl_compatibility=True, 
        debug_mode=True,
        detection_confidence=0.85
    )