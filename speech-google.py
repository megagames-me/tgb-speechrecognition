print("INFO: Importing libraries...")
import speech_recognition as sr
print("INFO: Done.")
r = sr.Recognizer()
m = sr.Microphone()

"""Sets parameters to stop recognizer.listening faster.

Parameters:
"r.pause_threshold":      an integer in seconds for how long the recognizer needs of silence to stop recording
"r.non_speaking_duration: seconds of non-speaking audio to keep on both sides of the recording, changed because it cannot be higher than `r.pause_threshold`
"""
r.pause_threshold = 0.3
r.non_speaking_duration = 0.3

def speech(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        #recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    print("INFO: Recognizing...")
    
    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

while True:
     print("INFO: Ready for speech.")
     trans = speech(r, m)["transcription"]
     if trans == "exit":
         exit()
     print(trans);
     
