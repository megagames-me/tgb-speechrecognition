# The GladiatorBots Speech Recognition Project

This is the GitHub repository where the code is stored.
## Dependencies
 - SpeechRecognition
 A lightweight and simple python package for speech recognition, with support for many APIs supported.
 We will be using the Google Speech Recognition API as the package comes with a free API code.
 
 Install this and read more (here)[https://pypi.org/project/SpeechRecognition/].
### Update - v1.0.1-alpha

Before this update, we were trying to use another API, as the Google API wasn't fast enough. However, we realized that it was because the code wasn't stopping the `listen` method, so it just would continue this. Read more down at the changelog.
 ---
  - PyAudio
  This requires PyAudio so that python can access the microphone for a constant flow of audio for the API to convert to text.
 ## Changelog
 ### v1.0.0-alpha
  First version of code.
  - Added basic speech recognition.
  #### Bugs
  - LS-001 | With a slightly loud background, the `listen` method doesn't stop. - **Fixed in v1.0.1-alpha**
    - Could be fixed by client by lowering input volume substantially.
  - RC-001 | Sometimes takes a long time to recognize - **Active**
   
 ### v1.0.1-alpha
  Bug fixes.
  - Fixed bug LS-001.<br />
  **Note:**<br />
  Works best at half input volume on a MacBook Air 2020.
  #### Bugs

  - Sometimes takes a long time to recognize - **Active**
